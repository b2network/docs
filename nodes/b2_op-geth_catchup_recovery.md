# B2 op-geth Catch-Up & Recovery Runbook

## 1. Background

When an op-geth node has been offline long enough that the L1 blobs
covering the gap have expired (L1 blob retention is a fixed number of
epochs, typically on the order of days), `op-node` may fail to catch it up
normally:

- `op-node` sees a `finalized` block already present in the datadir and
  chooses to CL-sync instead of EL-sync. CL-sync needs the (now expired)
  blobs for the gap, so it deadlocks permanently.
- Separately, `engine_forkchoiceUpdated` **ignores** a zero
  `finalizedBlockHash` instead of clearing it, so the engine's `finalized`
  label stays pinned at whatever it was before the outage. If `op-node`'s
  `FindL2Heads` walk ever starts from that stale label, it can walk back
  past a full `seq_window` and drop below the L1 blob retention boundary,
  reproducing the same deadlock.

The fix bypasses `op-node` entirely and drives `op-geth`'s execution layer
straight from a healthy public B2 peer via the **Engine API**, then repairs
the `safe`/`finalized` labels so that once `op-node` is turned back on, its
backward walk terminates near the new head instead of at the stale
pre-outage `finalized` block.

Two scripts implement this:

| Script | Purpose |
|---|---|
| `drive_sync.py` | Feeds the current network tip to geth (`engine_newPayloadV3` + `engine_forkchoiceUpdatedV3`) so geth's BeaconSync walks backward from the tip and fills in the gap. |
| `set_labels.py` | Once geth is caught up, advances the `safe`/`finalized` labels to blocks near the new head so `op-node`'s backstop is no longer stale. |

## 2. Symptoms

- `op-node` logs show it stuck on CL sync / waiting on blob retrieval that
  will never succeed.
- `eth_getBlockByNumber("finalized")` on geth returns a very old block
  compared to `"latest"`.
- geth's head is not advancing even though the network `tip` (from a public
  peer) is far ahead.

## 3. Prerequisites
- [drive_sync.py](drive_sync.py)
- [set_labels.py](set_labels.py)
- Network access from wherever `drive_sync.py` and `set_labels.py` run to:
  - the public B2 RPC endpoint: `https://b2-mainnet.alt.technology`
    (this is the fixed value for `PUBLIC_RPC` in `drive_sync.py`)
  - the local geth node's Engine API and RPC ports (values depend on the
    deployment — host networking, Docker Compose service name, or
    Kubernetes pod/service, etc.)
- Read access to whatever Engine API JWT secret file geth was started
  with, from the same execution context that will run the scripts.
- **`op-node` must be stopped for the entire duration of this procedure.**
  `op-node`, `drive_sync.py`, and `set_labels.py` all issue
  `engine_forkchoiceUpdated` calls; running any of them concurrently races
  and can corrupt the sync state.
- Before running either script, set its constants to match the execution
  context it will actually run from — these are deployment-specific and
  will differ between environments/incidents:
  - `drive_sync.py`: `JWT_PATH`, `ENGINE`, `LOCAL_RPC` (`PUBLIC_RPC` is
    fixed, see above).
  - `set_labels.py`: `JWT_PATH`, `ENGINE`, `LOCAL_RPC`, `FINALIZED_LAG`.
  - If a script is copied into a different host/container than the one it
    was last configured for, verify connectivity (e.g. a simple RPC call)
    before trusting any output it produces — a wrong `ENGINE`/`LOCAL_RPC`
    value will just fail to connect rather than silently doing the wrong
    thing, but a wrong `JWT_PATH` pointing at the *right host's* JWT for
    the *wrong* geth instance would not necessarily fail loudly.
  - example: 
    ```py
    JWT_PATH = "/jwt.txt"
    ENGINE = "http://127.0.0.1:8551"
    PUBLIC_RPC = "https://b2-mainnet.alt.technology"
    LOCAL_RPC = "http://127.0.0.1:8545"
    FINALIZED_LAG = 2000  # ~1.1h behind head, comfortably inside blob retention
    ```
## 4. Procedure

### Step 0 — Stop op-node

Stop whatever supervises `op-node` in the target deployment (e.g. its
Docker Compose service, Kubernetes deployment, or systemd unit).

Confirm it is actually stopped (no process issuing `forkchoiceUpdated`)
before continuing.

### Step 1 — Run drive_sync.py

Deploy `drive_sync.py` to wherever it can reach both the public RPC and the
local geth Engine API (copy method depends on the environment — `scp`,
`kubectl cp`, etc.), configure its constants per Step 3 above, then run:

```sh
python3 drive_sync.py
```

This pulls the current tip block and its raw transactions from
`PUBLIC_RPC`, submits the tip via `engine_newPayloadV3`, and points
`engine_forkchoiceUpdatedV3` at it. This kicks off (or continues) geth's
BeaconSync, which then backfills from its peers on its own.

A `SYNCING` status in the output is expected and fine. An `INVALID` status
is fatal — the script exits non-zero; stop and investigate (mismatched
JWT, wrong RPC endpoint, or a bad payload) before retrying.

Since the tip keeps advancing and geth may lose peers over time, re-run
this script as needed until the local head has caught up to (or is
acceptably close to) the network tip — compare the `local head=` /
`behind=` values it prints, or query `eth_blockNumber` directly against
both the local node and `PUBLIC_RPC`.

### Step 2 — Run set_labels.py

Once geth's head is caught up, deploy `set_labels.py` to an execution
context that can reach the local geth Engine API and RPC (configure its
constants per Step 3 above — this may be a different execution context
than `drive_sync.py`, e.g. a container on the geth's own network rather
than the host), then run:

```sh
python3 set_labels.py
```

It will:
1. Read the current `latest` head.
2. Compute `finalized = head - FINALIZED_LAG`.
3. Call `engine_forkchoiceUpdatedV3` with `head = safe = latest`,
   `finalized` = the computed block.
4. Read back and print the `safe` and `finalized` labels to confirm they
   moved.

If the resulting status is not `VALID`, the script exits non-zero — stop
and investigate before restarting `op-node`.

### Step 3 — Start op-node

Start `op-node` back up under its normal supervision (Docker Compose,
Kubernetes, systemd, etc.).

## 5. Verification / Success Criteria

- `eth_getBlockByNumber("finalized")` and `("safe")` on geth now return
  recent blocks, not the stale pre-outage `finalized` block.
- `op-node` logs show it deriving/verifying new L2 blocks rather than
  stalling on blob retrieval.
- geth's `latest` head continues to advance in step with the network after
  `op-node` resumes control of forkchoice updates.

## 6. Rollback / Troubleshooting

- **`newPayloadV3` returns `INVALID`**: stop immediately (the script
  already exits `1`). Re-check that the block header and raw RLP came
  from the same block (the script pins both fetches to one block hash)
  and that the JWT secret matches the target geth instance.
- **geth has too few devp2p peers**: manually re-dial known bootnodes for
  the network (e.g. via `admin.addPeer(...)` on the geth console) and
  re-run `drive_sync.py` afterward.
- **A script can't connect to the configured `ENGINE`/`LOCAL_RPC`**:
  double check which host/container it's actually running from vs. the
  one its constants were set for (see Step 3 in Prerequisites) — the two
  scripts may need different values depending on where each is executed.
- **Accidentally ran `op-node` at the same time as `drive_sync.py` or
  `set_labels.py`**: stop everything, re-check the current
  `latest`/`safe`/`finalized` labels, and re-run from Step 0 — do not
  assume the state is consistent.

## 7. Safety Notes

- `op-node` **must never run at the same time** as `drive_sync.py` or
  `set_labels.py` — all of them issue competing `engine_forkchoiceUpdated`
  calls.
- All block data driving the recovery comes from the canonical B2 network
  over devp2p/RPC (a public peer and the local peer set) — the same trust
  assumption the rest of the node already relies on. No new trust boundary
  is introduced.
- `FINALIZED_LAG` must stay small enough to land after the L1 blob
  retention boundary and after any node offline gaps, but large enough to
  give a safety margin behind the head. Choose its value per incident —
  do not set it to `0`, given `engine_forkchoiceUpdated`'s known behavior
  of ignoring a zero `finalizedBlockHash` instead of clearing it.
