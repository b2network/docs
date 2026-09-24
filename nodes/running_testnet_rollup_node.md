# Running A B2 TestNet  Node

Learn how to run a node for the B2 TestNet.

## System Requirements

**hardware requirements**

- CPUs: 4 vCPUs
- RAM:  8 GB
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

## Download configuration files
Below is the related files
| Snapshot Data     | Size | Download Link | sha256sum
| ----------- | ----------- | ----------- | ----------- |
| 2024-08-23     | 4.0K     | [rollup.json](https://download.bsquared.network/testnet/rollup.json) | be7a590a5b4eb177c9953132f65be8cb0417ec47ccb2728c143da66a12c9eb2d
| 2024-08-23     | 9.0M     | [genesis.json](https://download.bsquared.network/testnet/genesis.json) | 6dd63965c40280e33e4de48ce97d0f4c49134a008e3d15669d0a110489d9046e

First, Create the ``b2-node`` directory.
the $PWD variable specifies the absolute path which you want.

```sh
mkdir -p $PWD/b2-node
cd $PWD/b2-node
```


Generate JWT Secret, The HTTP connection between your beacon node and execution node needs to be authenticated using a JWT token. This is the way to generate jwt secret by openssl.

```bash
apk add openssl
openssl rand -hex 32 > ./jwt.txt
```

## Setup B2 TestNet Node

Create  a ``docker-compose.yaml`` file and mount the data directory and json files which downloaded above.

```bash
version: "3.9"
services:
  l2:
    image: us-docker.pkg.dev/oplabs-tools-artifacts/images/op-geth:v1.101315.0
    container_name: l2
    environment:
      GETH_VERBOSITY: "3"
      GETH_DATADIR: "/data"
      GETH_ROLLUP_DISABLETXPOOLGOSSIP: "false"
      GETH_ROLLUP_SEQUENCERHTTP: "https://b2-testnet.alt.technology"
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
      GETH_BOOTNODES: "enode://8220fec60370080ba11940bd9b9e5352a8a1436fffe10593d40e21b8c7861ae71fad361cdcf2fadf1188661438556e203b4cf59ef1df91872871e0c6c4a5dfe6@b2-testnet-geth-p2p.altlayer.network:30303"
      GETH_METRICS: "true"
    entrypoint: [ "/bin/sh", "-c" ]
    command:
      - |
        # do geth init if datadir is empty
        if [ ! -d "/data/geth" ]; then
            echo "Initializing geth datadir"
            wget -O /data/genesis.json  https://download.bsquared.network/testnet/genesis.json
            geth init --datadir=/data /data/genesis.json
        else
            echo "geth datadir already initialized, skipping..."
        fi
        exec geth
    restart: always
    network_mode: host
    volumes:
    - ./l2:/data
    - ./jwt.txt:/jwt.txt

  op-node:
    image: us-docker.pkg.dev/oplabs-tools-artifacts/images/op-node:v1.7.7
    container_name: op-node
    environment:
      OP_NODE_SYNCMODE: "execution-layer"
      OP_NODE_L1_TRUST_RPC: "true"
      OP_NODE_SEQUENCER_L1_CONFS: "10"
      OP_NODE_VERIFIER_L1_CONFS:  "10"
      OP_NODE_L1_BEACON: "https://testnet-hub-cl-rpc.bsquared.network"
      OP_NODE_L2_ENGINE_RPC: "ws://127.0.0.1:8551"
      OP_NODE_L2_ENGINE_AUTH: "/jwt.txt"
      OP_NODE_ROLLUP_CONFIG:  "/data/rollup.json"
      OP_NODE_RPC_ADDR: "0.0.0.0"
      OP_NODE_L1_ETH_RPC: "https://testnet-hub-rpc.bsquared.network"
      OP_NODE_L1_RPC_KIND: "standard"
      OP_NODE_METRICS_ENABLED:  "true"
      OP_NODE_P2P_LISTEN_IP: "0.0.0.0"
      OP_NODE_P2P_LISTEN_TCP_PORT: "9222"
      OP_NODE_P2P_LISTEN_UDP_PORT: "9222"
      OP_NODE_P2P_DISCOVERY_PATH: "/data/node/opnode_discovery_db"
      OP_NODE_P2P_PEERSTORE_PATH: "/data/node/opnode_peerstore_db"
      OP_NODE_P2P_PRIV_PATH: "/data/node/opnode_p2p_priv.txt"
      OP_NODE_P2P_STATIC: "/dns/b2-testnet-node-p2p.altlayer.network/tcp/9003/p2p/16Uiu2HAmRdoaMWxvycpYPKx9Knt4pFcLjAUQKujCCDYXrsjwUQKP"
    entrypoint: [ "/bin/sh", "-c" ]
    command:
      - |
        until nc -z -w 5 127.0.0.1  8551; do
            echo "Waiting for geth ..."
            sleep 5
        done
        echo "geth is up"

        if [ ! -f "/data/rollup.json" ]; then
            wget -O /data/rollup.json https://download.bsquared.network/testnet/rollup.json
        fi
        exec op-node


    depends_on:
    - l2
    restart: always
    network_mode: host
    volumes:
    - ./node:/data/node
    - ./jwt.txt:/jwt.txt
```

Now, All preparations are complete, and the data directory structure is as follow:
```bash
tree
.
├── docker-compose.yml
└── jwt.txt

1 directory, 2 files
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
INFO [08-23|10:29:36.676] Loaded most recent local block           number=0 hash=95043f..977eb1 td=0 age=1d1h38m
WARN [08-23|10:29:36.677] Failed to load snapshot                  err="missing or corrupted snapshot"
INFO [08-23|10:29:36.680] Rebuilding state snapshot
INFO [08-23|10:29:36.682] Initialized transaction indexer          range="last 2350000 blocks"
INFO [08-23|10:29:36.682] Initialising Ethereum protocol           network=1123 dbversion=<nil>
INFO [08-23|10:29:36.682] Resuming state snapshot generation       root=c5fa15..8cc03c accounts=0 slots=0 storage=0.00B dangling=0 elapsed=1.570ms
INFO [08-23|10:29:36.685] Entered PoS stage
INFO [08-23|10:29:36.685] Enabled snap sync                        head=0 hash=95043f..977eb1
INFO [08-23|10:29:36.685] Chain post-merge, sync via beacon client
INFO [08-23|10:29:36.686] Gasprice oracle is ignoring threshold set threshold=2
WARN [08-23|10:29:36.690] Engine API enabled                       protocol=eth
INFO [08-23|10:29:36.690] Starting peer-to-peer node               instance=Geth/v1.101315.0-stable-ef178f25/linux-amd64/go1.21.10
INFO [08-23|10:29:36.702] New local node record                    seq=1,724,408,976,702 id=1b6e21b68af9871c ip=127.0.0.1 udp=30303 tcp=30303
INFO [08-23|10:29:36.704] IPC endpoint opened                      url=/data/geth.ipc
INFO [08-23|10:29:36.705] Loaded JWT secret file                   path=/jwt.txt crc32=0xfabe003a
INFO [08-23|10:29:36.705] HTTP server started                      endpoint=[::]:8545 auth=false prefix= cors= vhosts=*
INFO [08-23|10:29:36.706] WebSocket enabled                        url=ws://[::]:8546
INFO [08-23|10:29:36.706] WebSocket enabled                        url=ws://[::]:8551
INFO [08-23|10:29:36.706] HTTP server started                      endpoint=[::]:8551 auth=true  prefix= cors=localhost vhosts=localhost
INFO [08-23|10:29:36.707] Started P2P networking                   self=enode://279e57328fa551d989b33125d432de8abc5c9547940a8871a84683a8e98fa276825f11c0b071cce1bd65dbf18446d7d11a100e7b9dadce9142bb045360984c16@127.0.0.1:30303
INFO [08-23|10:29:36.764] Generated state snapshot                 accounts=2363 slots=2084 storage=393.81KiB dangling=0 elapsed=83.329ms
WARN [08-23|10:29:42.997] Served eth_getBlockByNumber              reqid=2 duration="122.392µs" err="finalized block not found"
WARN [08-23|10:29:42.999] Ignoring payload while snap syncing      number=46151 hash=137a80..c021ad reason="forced head needed for startup"
INFO [08-23|10:29:42.999] Forkchoice requested sync to new head    number=46151 hash=137a80..c021ad
INFO [08-23|10:29:43.778] Syncing beacon headers                   downloaded=512 left=45638 eta=1m9.346s
INFO [08-23|10:29:44.047] Forkchoice requested sync to new head    number=46152 hash=611203..09bed5
INFO [08-23|10:29:46.043] Forkchoice requested sync to new head    number=46153 hash=c32e33..371cc6
INFO [08-23|10:29:48.042] Forkchoice requested sync to new head    number=46154 hash=79a5c8..57c3dd
INFO [08-23|10:29:50.041] Forkchoice requested sync to new head    number=46155 hash=354466..5b5bb6
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
