# Local Single Node

In this chapter, we will introduce how to run a local single node service, which can facilitate testing on your local machine. If you want to run multiple node services locally, please refer to [Multi Nodes](./multi-nodes.md).

Below are two ways to run a local node: manual and script automation.

## Script Automation

We have a script file in the code repository that can quickly start the local B^2 Node. To do this, simply go to the root directory of the repository and run the following command:

```
$ ./init.sh
```

This script will first compile the executable file, then initialize the startup configuration file using the executable file, and finally start the node. After a successful startup, you can find the generated configuration file in the `~/.ethermintd` directory.

## Manual Startup

Before starting manually, we need to compile and obtain the executable file. First, we need to get the code from the B^2 Node repository:

```
$ git clone https://github.com/b2network/b2-node.git
```

### Compile the Executable File

Enter the code repository and compile the executable file:

```
$ cd b2-node
$ make build
```

After a successful compilation, you can find the compiled executable file `ethermintd` in the `build` directory of the code repository:

```
$ ls build

ethermintd
```

### Initialize the Configuration File

Execute the following command to initialize the configuration file required for starting the chain locally:

```
$ ethermintd init mynode --chain-id ethermint_9000-1
```

Where `mynode` is the node name and `ethermint_9000-1` is the chain ID. You can find the generated configuration file in the `~/.ethermintd` directory.

### Create Initial Account

Before starting the chain, we need to create an account to perform on-chain operations later:

```
$ ethermintd keys add mykey --keyring-backend=test

- address: ethm15sne9wetu29qmcneyu9zsazmeshnjldkmw4dwq
  name: mykey
  pubkey: '{"@type":"/ethermint.crypto.v1.ethsecp256k1.PubKey","key":"A2EjD/hL8v3B9856wfBmch4pNwpUwHPN+3rs6e7OyDVE"}'
  type: local
```

After the above operation, you will see a newly generated keyring-test folder in the configuration file directory, which contains the files of the account you just created:

```
$ ls ~/.ethermintd/keyring-test
069ccfa78d67aeaf2f1f42508b1a7bf5baa08e37.address mykey.info
```

This account is not yet on-chain, so we need to add it to the initialization configuration file:

```
$ ethermintd add-genesis-account mykey 10000000000bsq --keyring-backend=test
```

Now your account has some tokens. You need to add a validator to the chain. A validator can be declared before the chain starts for the first time through a special transaction, which is included in a genesis file named genx:

```
$ ethermintd gentx mykey 10000000000stake,10000000000bsq --keyring-backend=test
```

### Collect gentx

By default, the genesis file does not contain any `gentxs`. A `gentx` is a transaction that bonds staking tokens present in the genesis file under `accounts` to a validator, essentially creating a validator at genesis. The chain will start as soon as more than 2/3rds of the validators (weighted by voting power) that are the recipient of a valid `gentx` come online after `genesis_time`.

A `gentx` can be added manually to the genesis file, or via the following command:

```
# Add the gentx to the genesis file
$ ethermintd collect-gentxs
```

This command will add all the gentxs stored in `~/.ethermintd/config/gentx` to the genesis file.

### Run Single Node

Finally, check the correctness of the genesis.json file:

```
$ ethermintd validate-genesis
```

Now that everything is set up, you can finally start your node:

```
$ ethermintd start
```
