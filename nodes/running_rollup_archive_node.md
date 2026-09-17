# Running A B2 Archive Node

Learn how to run a Archive node for the B2.

## System Requirements

**hardware requirements**

- CPUs: 4vCPUs
- RAM:  8GB
- Storage: 1 TB NVMe Storage
- 100MBps bidirectional internet connection

You can run B2 on lower-spec hardware, but you may find that it is not highly performant or prone to crashing.

**software requirements**


OS：As long as Docker Engine can be installed, the operating system will suffice.

## Pre-install

### Install Docker

Please refer to the [Install Docker Engine](https://docs.docker.com/engine/install/)

### Install Docker-compose

Please refer to the [Install Docker Compose](https://docs.docker.com/compose/install/standalone/)

## Import Blocks With `geth import`

Use `geth import` instead of downloading a full archive snapshot of the data directory. Import is incremental and more flexible: if the local node is missing a block range, download only that range and import it.

Block files are published at [https://rlp.bsquared.network/](https://rlp.bsquared.network/). Each file is named `block-<start>-<end>.rlp` (about 500,000 blocks per file).

Import archive data with `--syncmode=full --gcmode=archive` so historical state is retained. Matching flags are already set in the `docker-compose.yaml` below (`GETH_SYNCMODE` / `GETH_GCMODE`).

### List files, then paginate and sort

Fetch the file list as JSON:

```bash
curl -H 'Accept: application/json' https://rlp.bsquared.network/
```

Sort by start block and print name and size:

```bash
curl -sS -H 'Accept: application/json' https://rlp.bsquared.network/ \
  | jq -r 'sort_by(.name | capture("block-(?<start>[0-9]+)-") | .start | tonumber)[]
           | "\(.name)\t\(.size)"'
```

Paginate after sorting by start block (example: first 10 files):

```bash
curl -sS -H 'Accept: application/json' https://rlp.bsquared.network/ \
  | jq -r 'sort_by(.name | capture("block-(?<start>[0-9]+)-") | .start | tonumber)[0:10][]
           | "\(.name)\t\(.size)"'
```

The listing API also accepts `offset` / `limit` and `sort` (`name` or `size`):

```bash
curl -sS -H 'Accept: application/json' 'https://rlp.bsquared.network/?offset=0&limit=10'
curl -sS -H 'Accept: application/json' 'https://rlp.bsquared.network/?sort=size'
```

### Download configuration files and RLP ranges

```bash
mkdir -p data rlp
curl -fsSL -o data/genesis.json https://raw.githubusercontent.com/b2network/docs/main/nodes/genesis.json
curl -fsSL -o data/rollup.json https://raw.githubusercontent.com/b2network/docs/main/nodes/rollup.json
```

Download a range (example: genesis through block 500,000):

```bash
wget -P rlp https://rlp.bsquared.network/block-0-500000.rlp
```

If a later range is missing locally, download only that file:

```bash
wget -P rlp https://rlp.bsquared.network/block-1000000-1500000.rlp
```

### Initialize the datadir and import RLP files

Initialize once, then import files **in block order** (low to high). You can import one file at a time.

```bash
docker run --rm \
  --volume ./data/db:/db \
  --volume ./data/genesis.json:/genesis.json \
  us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101315.2 \
  init --datadir=/db /genesis.json

docker run --rm \
  --volume ./data/db:/db \
  --volume ./rlp:/rlp \
  us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101315.2 \
  --syncmode=full --gcmode=archive import --datadir=/db /rlp/block-0-500000.rlp
```

Import every downloaded file in height order:

```bash
for f in $(ls rlp/block-*.rlp | sort -t- -k2 -n); do
  docker run --rm \
    --volume ./data/db:/db \
    --volume ./rlp:/rlp \
    us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101315.2 \
    --syncmode=full --gcmode=archive import --datadir=/db "/rlp/$(basename "$f")"
done
```

After import, start the node with docker-compose. Any blocks after the last imported file will sync from the network.

## Setup B2 Archive Node
Generate jwt secret:
```bash
openssl rand -hex 32 > ./data/jwt.txt
```

Create  a ``docker-compose.yaml`` file and mount the data directory and json files prepared above.

**Changelog for the ``docker-compose.yaml``:**

**Users who have already been set up can also upgrade,The upgrade will improve block synchronization.**

- L2 image change to ``us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101315.2``
- OP image change to ``us-docker.pkg.dev/oplabs-tools-artifacts/images/op-node:v1.7.7``
- OP_NODE_P2P_STATIC,GETH_BOOTNODES (See below)
```bash
version: "3.9"
services:
  l2:
    #image: ghcr.io/b2network/op-geth:v1.101311.0
    image: us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101315.2 
    container_name: l2
    environment:
      GETH_VERBOSITY: "3"
      GETH_DATADIR: "/db"
      GETH_ROLLUP_DISABLETXPOOLGOSSIP: "false"
      GETH_ROLLUP_SEQUENCERHTTP: "https://b2-mainnet.alt.technology/"
      GETH_HTTP: "true"
      GETH_HTTP_ADDR: "0.0.0.0"
      GETH_HTTP_VHOSTS: "*"
      GETH_HTTP_API: "web3,debug,eth,txpool,net,engine"
      GETH_WS: "true"
      GETH_WS_ADDR: "0.0.0.0"
      GETH_WS_API: "web3,debug,eth,txpool,net,engine"
      GETH_AUTHRPC_ADDR: "0.0.0.0"
      GETH_AUTHRPC_PORT: "8551"
      GETH_BOOTNODES: "enode://01c15b6db86024b708a3f3e2cdea2769264bc81dc8997752b44b904daff98f2ca15ca1e3096ed601debe7ad0f057c12d30bf93aeaeb227a59443059402c57dec@b2-mainnet-bootnode2.bsquared.network:30303,enode://c6dc84f7885be7520fcd18ef1db35bc810d1402b9f8bd76871745ac760eb51deeed161a6ef49d05bb77ee0aabe3ace02800dea409ebfce623ac56291458cb132@b2-mainnet-bootnodes.alt.technology:10200,enode://4faae95a039ccb4eb27d1692709fd8646dc323c4d039c3db7870f77af2a2cdddad1feb8290b32070e1da3894fb1a78d8d23a1d1169939331da44e3816ec8d6ad@b2-mainnet-bootnodes.alt.technology:10210"

      GETH_METRICS: "true"
      GETH_SYNCMODE: "full"
      GETH_GCMODE: "archive"
      GETH_RPC_ALLOW_UNPROTECTED_TXS: "true"
    restart: always
    network_mode: host
    volumes:
    - ./data/db:/db
    - ./data/genesis.json:/genesis.json
    - ./data/jwt.txt:/jwt.txt

  op-node:
    #image: us-docker.pkg.dev/oplabs-tools-artifacts/images/op-node:99a53381019d3571359d989671ccf70f8d69dfd9
    image: us-docker.pkg.dev/oplabs-tools-artifacts/images/op-node:v1.7.7 
    container_name: op-node
    environment:
      OP_NODE_SYNCMODE: "execution-layer"
      OP_NODE_L1_TRUST_RPC: "true"
      OP_NODE_SEQUENCER_L1_CONFS: "10"
      OP_NODE_VERIFIER_L1_CONFS: "10"
      OP_NODE_L1_BEACON: "https://hub-cl-rpc.bsquared.network"
      OP_NODE_L2_ENGINE_RPC: "ws://127.0.0.1:8551"
      OP_NODE_L2_ENGINE_AUTH: "/jwt.txt"
      OP_NODE_ROLLUP_CONFIG: "rollup.json"
      OP_NODE_RPC_ADDR: "0.0.0.0"
      OP_NODE_L1_ETH_RPC: "https://hub-rpc.bsquared.network"
      OP_NODE_L1_RPC_KIND: "standard"
      OP_NODE_METRICS_ENABLED: "true"
      OP_NODE_P2P_LISTEN_IP: "0.0.0.0"
      OP_NODE_P2P_LISTEN_TCP_PORT: "9222"
      OP_NODE_P2P_LISTEN_UDP_PORT: "9222"
      OP_NODE_P2P_DISCOVERY_PATH: "/data/node/opnode_discovery_db"
      OP_NODE_P2P_PEERSTORE_PATH: "/data/node/opnode_peerstore_db"
      OP_NODE_P2P_PRIV_PATH: "/data/node/opnode_p2p_priv.txt"
      OP_NODE_P2P_STATIC: "/dns/b2-mainnet-bootnodes-v2.altlayer.network/tcp/20202/p2p/16Uiu2HAm1oTTtY6QkUdVUY8qn86Aa6MPR8FxMR4VQzXKT6tCPEun,/dns/b2-mainnet-bootnodes-v2.altlayer.network/tcp/20203/p2p/16Uiu2HAmJhSCro27M9ZQ4yPkEQjYcRx1QJ9BmzfunNPPHbJsXnGV,/dns/b2-mainnet-bootnodes.alt.technology/tcp/20200/p2p/16Uiu2HAmBVxo37r3gVjK6P5m1cao5Y6UrXUu7EYd6xF4mBSVMraF,/dns/b2-mainnet-bootnodes.alt.technology/tcp/20210/p2p/16Uiu2HAmUXcXMoesAN5AjpkpYsTTHs2GWXvEEs7iRjNaL3A7WCSH"

    depends_on:
    - l2
    restart: always
    network_mode: host
    volumes:
    - ./data/node:/data/node
    - ./data/jwt.txt:/jwt.txt
    - ./data/rollup.json:/rollup.json
```

Now, All preparations are complete, and the data directory structure is as follow:
```bash
tree -L 3
.
|-- data
|   |-- db
|   |   |-- geth
|   |   `-- keystore
|   |-- genesis.json
|   |-- jwt.txt
|   `-- rollup.json
|-- rlp
|   `-- block-0-500000.rlp
`-- docker-compose.yml
```

The next step is to start the service.

## Start The Node

```bash
docker-compose up -d
```
## Verify Result

Watch the L2 container logs

```bash
docker logs -f l2
```
```bash
l2  | INFO [06-17|09:45:07.841] Merge configured:
l2  | INFO [06-17|09:45:07.841]  - Hard-fork specification:    https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/paris.md
l2  | INFO [06-17|09:45:07.841]  - Network known to be merged: true
l2  | INFO [06-17|09:45:07.841]  - Total terminal difficulty:  0
l2  | INFO [06-17|09:45:07.841]  - Merge netsplit block:       #0
l2  | INFO [06-17|09:45:07.841]
l2  | INFO [06-17|09:45:07.841] Post-Merge hard forks (timestamp based):
l2  | INFO [06-17|09:45:07.841]  - Shanghai:                    @0          (https://github.com/ethereum/execution-specs/blob/master/network-upgrades/mainnet-upgrades/shanghai.md)
l2  | INFO [06-17|09:45:07.841]  - Cancun:                      @0
l2  | INFO [06-17|09:45:07.841]  - Regolith:                    @0
l2  | INFO [06-17|09:45:07.841]  - Canyon:                      @0
l2  | INFO [06-17|09:45:07.841]  - Ecotone:                     @0
l2  | INFO [06-17|09:45:07.841]
l2  | INFO [06-17|09:45:07.841] ---------------------------------------------------------------------------------------------------------------------------------------------------------
l2  | INFO [06-17|09:45:07.841]
l2  | INFO [06-17|09:45:07.877] Loaded most recent local block           number=2,593,146 hash=12c9b9..19e5d4 td=0 age=3d2h17m
l2  | INFO [06-17|09:45:07.877] Loaded most recent local finalized block number=2,592,324 hash=5dd607..3a9f3c td=0 age=3d2h44m
l2  | INFO [06-17|09:45:07.879] Loaded last snap-sync pivot marker       number=2,190,015
```

Block synchronization takes some time, please wait patiently.
After some while，can check the syncing process by below command:

```bash
curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}' http://localhost:8545 | jq '.result'
```

The block will catch up to the latest block once the request returns `false`.

```bash
# curl -s -X POST -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}' http://localhost:8545 | jq '.result'
false
```
