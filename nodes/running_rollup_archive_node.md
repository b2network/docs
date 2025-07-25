# Running A B2 Archive Node

Learn how to run a Archive node for the B2.

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

## Download Snapshot Archive Data
```bash
docker run \
  --rm \
  --volume ./data:/data \
  ghcr.io/b2network/bsquared-snapshpt-download:20250707-160537 \
  mainnet-archivenode-snapshot /data
```

**The snapshot file will be updated every Friday. The download will be temporarily unavailable. Please wait a while and try again.**

## Setup B2 Archive Node
Generate jwt secret:
```bash
openssl rand -hex 32 > ./data/jwt.txt
```

Create  a ``docker-compose.yaml`` file and mount the data directory and json files which downloaded above.

**Changelog for the ``docker-compose.yaml``:**

**Users who have already been set up can also upgrade,The upgrade will improve block synchronization.**

- L2 image change to ``us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101315.2``
- OP image change to ``us-docker.pkg.dev/oplabs-tools-artifacts/images/op-node:v1.7.7``
- OP_NODE_P2P_STATIC: "/dns/b2-mainnet-bootnodes.altlayer.network/tcp/32046/p2p/16Uiu2HAm1hkacTvu8HzwPs2Mv8cHo6RfMX9vbEi4T8FuXFRK7VEM,/dns/b2-mainnet-bootnodes.altlayer.network/tcp/32048/p2p/16Uiu2HAm1oTTtY6QkUdVUY8qn86Aa6MPR8FxMR4VQzXKT6tCPEun,/dns/b2-mainnet-bootnodes.altlayer.network/tcp/32050/p2p/16Uiu2HAmJhSCro27M9ZQ4yPkEQjYcRx1QJ9BmzfunNPPHbJsXnGV,/dns/b2-mainnet-bootnode1.bsquared.network/tcp/9222/p2p/16Uiu2HAkwyquyg55Jnmo97czvXfB6Evove1C4jUdMoFRQEQkgbnn,/dns/b2-mainnet-bootnode2.bsquared.network/tcp/9222/p2p/16Uiu2HAmSP44jYc7aJVXJhKVoYUFqkotwpEU1zqxYCksvUWwcyFT"
- GETH_BOOTNODES: "enode://55b79017f15cad10bb8ad433fb991e6a0d0ca5ccef3f9123618869ee405d61b564a44dee1b87c47e62dba51e63a9172e356714a7ecdf20594d041ddf9013136c@b2-mainnet-bootnodes.altlayer.network:32045,enode://ad371eb83f665586985f4482adc8bb7fff793370843d73124e8b23c7aa69f01b6db93e5782ccbf7524d04aa5345e6bd1feeca4ec7bb1a515c3af67484604a5a8@b2-mainnet-bootnodes.altlayer.network:32047,enode://274310e51ffbc42167dbf1adbcf0ef43f50db9f8f0c84d9f25ac6cf1659ca57b09c9398fbc881485865170c8090250b8b803cb2f1be11aa65b488b3c8337be2d@b2-mainnet-bootnodes.altlayer.network:32049,enode://7ddd900597dde5cca6508cf33264dd528b945563d3d6ff5d0d2b16ecf8e14ca92ebf44fdabe9ecef44532aa0caeb54945c7d40af9d5a08e4b81853308a91ed27@b2-mainnet-bootnode1.bsquared.network:30303,enode://01c15b6db86024b708a3f3e2cdea2769264bc81dc8997752b44b904daff98f2ca15ca1e3096ed601debe7ad0f057c12d30bf93aeaeb227a59443059402c57dec@b2-mainnet-bootnode2.bsquared.network:30303" 
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
      GETH_BOOTNODES: "enode://55b79017f15cad10bb8ad433fb991e6a0d0ca5ccef3f9123618869ee405d61b564a44dee1b87c47e62dba51e63a9172e356714a7ecdf20594d041ddf9013136c@b2-mainnet-bootnodes.altlayer.network:32045,enode://ad371eb83f665586985f4482adc8bb7fff793370843d73124e8b23c7aa69f01b6db93e5782ccbf7524d04aa5345e6bd1feeca4ec7bb1a515c3af67484604a5a8@b2-mainnet-bootnodes.altlayer.network:32047,enode://274310e51ffbc42167dbf1adbcf0ef43f50db9f8f0c84d9f25ac6cf1659ca57b09c9398fbc881485865170c8090250b8b803cb2f1be11aa65b488b3c8337be2d@b2-mainnet-bootnodes.altlayer.network:32049,enode://7ddd900597dde5cca6508cf33264dd528b945563d3d6ff5d0d2b16ecf8e14ca92ebf44fdabe9ecef44532aa0caeb54945c7d40af9d5a08e4b81853308a91ed27@b2-mainnet-bootnode1.bsquared.network:30303,enode://01c15b6db86024b708a3f3e2cdea2769264bc81dc8997752b44b904daff98f2ca15ca1e3096ed601debe7ad0f057c12d30bf93aeaeb227a59443059402c57dec@b2-mainnet-bootnode2.bsquared.network:30303" 
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
      OP_NODE_P2P_STATIC: "/dns/b2-mainnet-bootnodes.altlayer.network/tcp/32046/p2p/16Uiu2HAm1hkacTvu8HzwPs2Mv8cHo6RfMX9vbEi4T8FuXFRK7VEM,/dns/b2-mainnet-bootnodes.altlayer.network/tcp/32048/p2p/16Uiu2HAm1oTTtY6QkUdVUY8qn86Aa6MPR8FxMR4VQzXKT6tCPEun,/dns/b2-mainnet-bootnodes.altlayer.network/tcp/32050/p2p/16Uiu2HAmJhSCro27M9ZQ4yPkEQjYcRx1QJ9BmzfunNPPHbJsXnGV,/dns/b2-mainnet-bootnode1.bsquared.network/tcp/9222/p2p/16Uiu2HAkwyquyg55Jnmo97czvXfB6Evove1C4jUdMoFRQEQkgbnn,/dns/b2-mainnet-bootnode2.bsquared.network/tcp/9222/p2p/16Uiu2HAmSP44jYc7aJVXJhKVoYUFqkotwpEU1zqxYCksvUWwcyFT"
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
|   |-- archive-data.tar.gz
|   |-- db
|   |   |-- geth
|   |   `-- keystore
|   |-- genesis.json
|   |-- jwt.txt
|   `-- rollup.json
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
