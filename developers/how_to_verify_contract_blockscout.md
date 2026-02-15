# Verify a Smart Contract with hardhat in Blockscout

## Install plugin

1. `npm install --save-dev @nomicfoundation/hardhat-verify`

2. And add the following statement to your hardhat.config.js:

    ```js
    require("@nomicfoundation/hardhat-verify");
    ```

    Or, if you are using TypeScript, add this to your hardhat.config.ts:

    ```ts
    import "@nomicfoundation/hardhat-verify";
    ```

## Config hardhat.config.js or hardhat.config.ts

```js
module.exports = {
  solidity: "0.8.28",
  networks: {
    b2: {
      url: "https://rpc.bsquared.network",
      chainId: 223,
      accounts: PRIVATE_KEY ? [PRIVATE_KEY] : [],
    },
  },
  etherscan: {
    apiKey: {
      b2: "no-api-key",
    },
    customChains: [
      {
        network: "b2",
        chainId: 223,
        urls: {
          apiURL: "https://12d6a1773a-backend-blockscout.bsquared.network/api/",
          browserURL: "https://explorer.bsquared.network",
        },
      },
    ],
  },
  sourcify: {
    enabled: false,
  },
}
```

## Verify

1. Assuming we have deployed the Locker contract [B² Network address details for 0xc1189535d0De120b5DeA3704BEa0e29af0715433 | Blockscout](https://explorer.bsquared.network/address/0xc1189535d0De120b5DeA3704BEa0e29af0715433?tab=contract)

2. We can use the following cli to verify

    ```bash
    npx hardhat verify --network b2 0xc1189535d0De120b5DeA3704BEa0e29af0715433 1893456000
    
    [dotenv@17.3.1] injecting env (2) from .env -- tip: 🔐 prevent committing .env to code: https://dotenvx.com/precommit
    [WARNING] Network and explorer-specific api keys are deprecated in favour of the new Etherscan v2 api. Support for v1 is expected to end by May 31st, 2025. To migrate, please specify a single Etherscan.io api key the apiKey config value.
    Successfully submitted source code for contract
    contracts/Lock.sol:Lock at 0xc1189535d0De120b5DeA3704BEa0e29af0715433
    for verification on the block explorer. Waiting for verification result...

    Successfully verified contract Lock on the block explorer.
    https://explorer.bsquared.network/address/0xc1189535d0De120b5DeA3704BEa0e29af0715433#code
    ```

3. For more features, please refer to

    ```bash
    t14p hardhat-etherjs-v5-js git:(main) ✗ npx hardhat verify --help
    Hardhat version 2.19.5

    Usage: hardhat [GLOBAL OPTIONS] verify [--constructor-args <INPUTFILE>] [--contract <STRING>] [--libraries <INPUTFILE>] [--list-networks] [--no-compile] [address] [...constructorArgsParams]

    OPTIONS:

      --constructor-args	File path to a javascript module that exports the list of arguments. 
      --contract        	Fully qualified name of the contract to verify. Skips automatic detection of the contract. Use if the deployed bytecode matches more than one contract in your project. 
      --libraries       	File path to a javascript module that exports the dictionary of library addresses for your contract. Use if there are undetectable library addresses in your contract. Library addresses are undetectable if they are only used in the constructor for your contract. 
      --list-networks   	Print the list of supported networks 
      --no-compile      	Don't compile before running this task 

    POSITIONAL ARGUMENTS:

      address              	Address of the smart contract to verify 
      constructorArgsParams	Contract constructor arguments. Ignored if the --constructor-args option is used. (default: [])

    verify: Verifies contract on Etherscan

    For global options help run: hardhat help

    ```

## Reference

1. [hardhat/packages/hardhat-verify at main · NomicFoundation/hardhat](https://github.com/nomicfoundation/hardhat/tree/main/packages/hardhat-verify)