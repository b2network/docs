# Add Validator Node

Before starting a new validator node, we need to generate the initial configuration file and create an account.

Use the following command to generate the default configuration file:

```
$ ethermintd init NODE_NAME --chain-id CHAIN_ID
```

The node startup requires the same initialization configuration file `genesis.conf`, which can be obtained from [here](https://github.com/b2network/b2-node.git) and copied to the configuration file directory.

If you don't have an account yet, you need to create an account with the following command:
```
$ ethermintd keys add --keyring-backend=test
```

Before doing the following, you need to make sure that you have enough tokens in your account to complete the pledge and as Gas fee.

Use the following command to add a new validator node:

```
ethermintd tx staking create-validator \\
  --amount=1000000bsq \\
  --pubkey=$(ethermintd tendermint show-validator --home <HOME>) \\
  --moniker="choose a moniker" \\
  --chain-id=<chain_id> \\
  --keyring-backend=test \\
  --commission-rate="0.05" \\
  --commission-max-rate="0.10" \\
  --commission-max-change-rate="0.01" \\
  --min-self-delegation="1000000" \\
  --gas=auto \\
  --gas-prices="1bsq" \\
  --from=<key_name> \\
  --home=<HOME>
```