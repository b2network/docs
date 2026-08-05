#!/usr/bin/env python3
"""Drive op-geth's beacon sync toward the B2 network tip via the Engine API.

op-node refuses to EL-sync this datadir (it sees a finalized block and jumps
straight to CL sync, which is deadlocked on expired L1 blobs). So we feed geth
the tip payload ourselves:

  engine_newPayloadV3  -> geth caches the header (parent missing => SYNCING)
  engine_forkchoiceUpdatedV3 -> geth starts BeaconSync toward that header

Raw transaction bytes come from a public B2 node's debug_getRawBlock, so the
payload reproduces the canonical block hash exactly.
"""
import base64, hmac, hashlib, json, sys, time, urllib.request

JWT_PATH = "TODO"
ENGINE = "TODO"
PUBLIC_RPC = "TODO"
LOCAL_RPC = "TODO"


def b64u(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=")


def make_token():
    with open(JWT_PATH) as f:
        secret = bytes.fromhex(f.read().strip().removeprefix("0x"))
    header = b64u(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    payload = b64u(json.dumps({"iat": int(time.time())}, separators=(",", ":")).encode())
    si = header + b"." + payload
    return (si + b"." + b64u(hmac.new(secret, si, hashlib.sha256).digest())).decode()


def rpc(url, method, params, token=None):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as r:
        res = json.loads(r.read())
    if "error" in res:
        raise RuntimeError(f"{method}: {res['error']}")
    return res["result"]


def rlp_item(b, i):
    """Return (kind, content_start, content_end, item_end) for the RLP item at i."""
    p = b[i]
    if p <= 0x7F:
        return "str", i, i + 1, i + 1
    if p <= 0xB7:
        n = p - 0x80
        return "str", i + 1, i + 1 + n, i + 1 + n
    if p <= 0xBF:
        k = p - 0xB7
        n = int.from_bytes(b[i + 1 : i + 1 + k], "big")
        s = i + 1 + k
        return "str", s, s + n, s + n
    if p <= 0xF7:
        n = p - 0xC0
        return "list", i + 1, i + 1 + n, i + 1 + n
    k = p - 0xF7
    n = int.from_bytes(b[i + 1 : i + 1 + k], "big")
    s = i + 1 + k
    return "list", s, s + n, s + n


def raw_transactions(block_rlp_hex):
    """Extract each transaction's canonical raw bytes from a block's RLP."""
    b = bytes.fromhex(block_rlp_hex.removeprefix("0x"))
    _, cs, ce, _ = rlp_item(b, 0)          # outer block list
    _, _, _, hdr_end = rlp_item(b, cs)     # header
    kind, tcs, tce, _ = rlp_item(b, hdr_end)
    assert kind == "list", "expected transaction list"
    txs, i = [], tcs
    while i < tce:
        kind, ics, ice, iend = rlp_item(b, i)
        # legacy tx = RLP list (keep the list prefix); typed tx = byte string
        # whose *content* is the 0x02/0x7e.. envelope (drop the string prefix).
        txs.append("0x" + (b[i:iend] if kind == "list" else b[ics:ice]).hex())
        i = iend
    return txs


def build_payload(blk, txs):
    return {
        "parentHash": blk["parentHash"],
        "feeRecipient": blk["miner"],
        "stateRoot": blk["stateRoot"],
        "receiptsRoot": blk["receiptsRoot"],
        "logsBloom": blk["logsBloom"],
        "prevRandao": blk["mixHash"],
        "blockNumber": blk["number"],
        "gasLimit": blk["gasLimit"],
        "gasUsed": blk["gasUsed"],
        "timestamp": blk["timestamp"],
        "extraData": blk["extraData"],
        "baseFeePerGas": blk["baseFeePerGas"],
        "blockHash": blk["hash"],
        "transactions": txs,
        "withdrawals": blk.get("withdrawals", []),
        "blobGasUsed": blk.get("blobGasUsed", "0x0"),
        "excessBlobGas": blk.get("excessBlobGas", "0x0"),
    }


def main():
    token = make_token()
    # Pin both fetches to one block by hash, so the header JSON and the raw
    # transaction bytes can never come from different blocks.
    blk = rpc(PUBLIC_RPC, "eth_getBlockByNumber", ["latest", False])
    raw = rpc(PUBLIC_RPC, "debug_getRawBlock", [blk["hash"]])
    txs = raw_transactions(raw)

    payload = build_payload(blk, txs)
    tip = int(blk["number"], 16)

    res = rpc(ENGINE, "engine_newPayloadV3",
              [payload, [], blk["parentBeaconBlockRoot"]], token)
    status = res["status"]
    print(f"newPayloadV3   tip={tip} -> {status} {res.get('validationError') or ''}")
    if status == "INVALID":
        sys.exit(1)

    fc = {"headBlockHash": blk["hash"],
          "safeBlockHash": "0x" + "00" * 32,
          "finalizedBlockHash": "0x" + "00" * 32}
    res = rpc(ENGINE, "engine_forkchoiceUpdatedV3", [fc, None], token)
    print(f"forkchoiceV3   -> {res['payloadStatus']['status']}")

    head = int(rpc(LOCAL_RPC, "eth_blockNumber", []), 16)
    print(f"local head={head}  behind={tip - head}")


if __name__ == "__main__":
    main()
