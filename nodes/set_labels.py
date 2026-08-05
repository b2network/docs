#!/usr/bin/env python3
"""Advance op-geth's safe/finalized labels to the freshly synced head.

Why: op-node's FindL2Heads walks the L2 chain backwards and uses the engine's
*finalized* label as its backstop. That label was still pinned at 33,666,200
(the pre-outage head) because engine_forkchoiceUpdated IGNORES a zero
finalizedBlockHash rather than clearing it. So the reset walk sailed straight
past one seq_window and dropped below the L1 blob retention boundary
(block 5,969,195), which would have re-created the original deadlock.

Setting the labels to blocks we already have makes the walk terminate near the
tip, where blobs still exist. These blocks came from the canonical B2 network
over devp2p, which is the same trust assumption the whole catch-up rests on.
"""
import base64, hmac, hashlib, json, sys, time, urllib.request

JWT_PATH = "TODO"
ENGINE = "TODO"
LOCAL_RPC = "TODO"
FINALIZED_LAG = 2000  # ~1.1h behind head, comfortably inside blob retention


def b64u(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=")


def make_token():
    with open(JWT_PATH) as f:
        secret = bytes.fromhex(f.read().strip().removeprefix("0x"))
    h = b64u(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    p = b64u(json.dumps({"iat": int(time.time())}, separators=(",", ":")).encode())
    si = h + b"." + p
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


def main():
    token = make_token()
    head = rpc(LOCAL_RPC, "eth_getBlockByNumber", ["latest", False])
    head_num = int(head["number"], 16)
    fin_num = head_num - FINALIZED_LAG
    fin = rpc(LOCAL_RPC, "eth_getBlockByNumber", [hex(fin_num), False])

    print(f"head      {head_num} {head['hash']}")
    print(f"finalized {fin_num} {fin['hash']}")

    fc = {
        "headBlockHash": head["hash"],
        "safeBlockHash": head["hash"],
        "finalizedBlockHash": fin["hash"],
    }
    res = rpc(ENGINE, "engine_forkchoiceUpdatedV3", [fc, None], token)
    st = res["payloadStatus"]
    print(f"forkchoiceUpdatedV3 -> {st['status']} {st.get('validationError') or ''}")
    if st["status"] != "VALID":
        sys.exit(1)

    for label in ("safe", "finalized"):
        b = rpc(LOCAL_RPC, "eth_getBlockByNumber", [label, False])
        print(f"verify {label:9} -> {int(b['number'], 16)}")


if __name__ == "__main__":
    main()
