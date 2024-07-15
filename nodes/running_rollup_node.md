# Running A B2 Node

Learn how to run a node for the B2.

## System Requirements

**hardware requirements**

- CPUs: 16 vCPUs
- RAM:  32 GB
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

## Download Snapshot Data
Below is the releated files
| Snapshot Data     | Size | Download Link | sha256sum
| ----------- | ----------- | ----------- | ----------- |
| 2024-07-15   | 9.4G     | [Mirror](https://download.bsquared.network/db.tar.gz) | 10e55bfa069b180cd611702544c26ae7a59b6538590c14bc79c3fbaf477777db 
| 2024-06-14     | 4.0K     | [rollup.json](https://download.bsquared.network/mainnet/rollup.json) |f54528da6468e0d72b2b8623a3ab87ed509b9910c3109a059c8dc143a1b34b8a
| 2024-06-14     | 9.0M     | [genesis.json](https://download.bsquared.network/mainnet/genesis.json) |fc5aba6864a1123a5f2104283d90ab412238f7abb556d147913f0d990fff7011

First, Create the ``b2-node`` directory.
the $PWD variable specifies the absolute path which you want.

```sh
mkdir -p $PWD/b2-node/data
cd $PWD/b2-node
wget -O ./data/db.tar.gz  https://download.bsquared.network/db.tar.gz
tar -zxvf ./data/db.tar.gz -C ./data/
```


Download the genesis file to `$PWD/b2-node/data`.

```bash
wget -O ./data/rollup.json https://download.bsquared.network/mainnet/rollup.json
wget -O ./data/genesis.json https://download.bsquared.network/mainnet/genesis.json
```
Generate JWT Secret, The HTTP connection between your beacon node and execution node needs to be authenticated using a JWT token. This is the way to generate jwt secret by openssl.

```bash
apk add openssl
openssl rand -hex 32 > ./data/jwt.txt
```

## Setup B2 Node

Create  a ``docker-compose.yaml`` file and mount the data directory and json files which downloaded above.
```bash
version: "3.9"
services:
  l2:
    image: ghcr.io/b2network/op-geth:v1.0
    container_name: l2
    environment:
      GETH_VERBOSITY: "3"
      GETH_DATADIR: "/db"
      GETH_ROLLUP_DISABLETXPOOLGOSSIP: "false"
      GETH_ROLLUP_SEQUENCERHTTP: "https://b2-mainnet.alt.technology/"
      GETH_HTTP: "true"
      GETH_HTTP_ADDR: "0.0.0.0"
      GETH_HTTP_API:  "web3,debug,eth,txpool,net,engine"
      GETH_HTTP_VHOSTS: "*" 
      GETH_WS:  "true"
      GETH_WS_ADDR: "0.0.0.0"
      GETH_WS_API: "web3,debug,eth,txpool,net,engine"
      GETH_AUTHRPC_ADDR:  "0.0.0.0"
      GETH_AUTHRPC_PORT: "8551"
      GETH_AUTHRPC_JWTSECRET: "/jwt.txt"
      GETH_BOOTNODES: "enode://176f80775240c053945d68ba74f87bca5df97a369d2d33f9b93dfb08faddbcdf68eddd19d7fb91089dda38973384d1ef61eb735bfb362986ebe85c57ff94a616@b2-mainnet-geth-p2p.altlayer.network:30303,enode://b6a3dd72aaa5494d7fb79c226af015a8ed515e401c765564d08e6b9b730b3c70e4e66658f1d45a9c62def7e061878a553ff19704b966c9ed98f1ca90eed09b05@b2-mainnet-bootnode1.bsquared.network:30303,enode://a1c925891787aadb1652c424dd3f7f0f037daf1337ffa03db7b70eed9b5c0853828881b487c3e0dd5c677680ec12d072ba772982fd56d86f846e85998b6191de@b2-mainnet-bootnode2.bsquared.network:30303"
      GETH_METRICS: "true"
    restart: always
    network_mode: host
    volumes:
    - ./data/db:/db
    - ./data/genesis.json:/genesis.json
    - ./data/jwt.txt:/jwt.txt

  op-node:
    image: us-docker.pkg.dev/oplabs-tools-artifacts/images/op-node:99a53381019d3571359d989671ccf70f8d69dfd9
    container_name: op-node
    environment:
      OP_NODE_SYNCMODE: "execution-layer"
      OP_NODE_L1_TRUST_RPC: "true"
      OP_NODE_SEQUENCER_L1_CONFS: "10"
      OP_NODE_VERIFIER_L1_CONFS:  "10"
      OP_NODE_L1_BEACON: "https://hub-cl-rpc.bsquared.network"
      OP_NODE_L2_ENGINE_RPC: "ws://127.0.0.1:8551"
      OP_NODE_L2_ENGINE_AUTH: "/jwt.txt"
      OP_NODE_ROLLUP_CONFIG:  "rollup.json"
      OP_NODE_RPC_ADDR: "0.0.0.0"
      OP_NODE_L1_ETH_RPC: "https://hub-rpc.bsquared.network"
      OP_NODE_L1_RPC_KIND: "standard"
      OP_NODE_METRICS_ENABLED:  "true"
      OP_NODE_P2P_LISTEN_IP: "0.0.0.0"
      OP_NODE_P2P_LISTEN_TCP_PORT: "9222"
      OP_NODE_P2P_LISTEN_UDP_PORT: "9222"
      OP_NODE_P2P_DISCOVERY_PATH: "/data/node/opnode_discovery_db"
      OP_NODE_P2P_PEERSTORE_PATH: "/data/node/opnode_peerstore_db"
      OP_NODE_P2P_PRIV_PATH: "/data/node/opnode_p2p_priv.txt"
      OP_NODE_P2P_STATIC: "/dns/b2-mainnet-node-p2p.altlayer.network/tcp/9003/p2p/16Uiu2HAmGM3EGwU7LBz64y2dc9RzUNNBSNeuNbrCXUnxxGQLgXST,/dns/b2-mainnet-bootnode1.bsquared.network/tcp/9222/p2p/16Uiu2HAm4AvoW3JmjHBswqCyf9fA91GDQNZQPt2ZM5bTWASMGmQS,/dns/b2-mainnet-bootnode2.bsquared.network/tcp/9222/p2p/16Uiu2HAmGJ7doABBynM5yn5CncicqwizY8xWPTXJTojm9BpS7N4x"
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
├── data
│   ├── db
│   │   ├── geth
│   │   └── keystore
│   ├── db.tar.gz
│   ├── genesis.json
│   ├── jwt.txt
│   └── rollup.json
└── docker-compose.yml
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
