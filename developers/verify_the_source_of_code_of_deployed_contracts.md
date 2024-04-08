# Install plugin
1. `npm install --save-dev @nomicfoundation/hardhat-verify`
2. And add the following statement to your hardhat.config.js:
    ```js
    require("@nomicfoundation/hardhat-verify");
    ```
    Or, if you are using TypeScript, add this to your hardhat.config.ts:
    ```ts
    import "@nomicfoundation/hardhat-verify";
    ```
# Config hardhat.config.js or hardhat.config.ts
```js
module.exports = {
  networks{
    habitat: {
      url: 'https://habitat-rpc.bsquared.network',
      chainId: 1123,
      accounts: {
        mnemonic: process.env.MNEMONIC,
        path: "m/44'/60'/0'/0",
        initialIndex: 0,
        count: 20,
      },
    },
  },
  etherscan: {
    apiKey: {
      habitat: "abc"
    },
    customChains: [
       {
        network: "habitat",
        chainId: 1123,
        urls: {
          apiURL: "https://habitat-backend.bsquared.network/api",
          browserURL: "https://habitat-explorer.bsquared.network"
        }
      },
      }
    ]
  },
```

# Verify
1. Assuming we have deployed the Counter contract [B² Network address details for 0xbcd2B61F456CB5D07bEf2B0eD5f5B9D5ED84C1c6 | Blockscout](https://habitat-explorer.bsquared.network/address/0xbcd2B61F456CB5D07bEf2B0eD5f5B9D5ED84C1c6?tab=contract)
1. We can use the following cli to verify
    ```bash
    npx hardhat --network habitat --verbose --show-stack-traces verify --contract contracts/Counter.sol:Counter 0xbcd2B61F456CB5D07bEf2B0eD5f5B9D5ED84C1c6
    hardhat:core:vars:varsManager Creating a new instance of VarsManager +0ms
    hardhat:core:vars:varsManager Loading ENV variables if any +1ms
    hardhat:core:global-dir Client Id found: 30b00202-0ea3-4d3d-abad-b9daa04e0407 +0ms
    hardhat:core:analytics Sending hit for task +0ms
    hardhat:core:analytics Hit payload: {"client_id":"30b00202-0ea3-4d3d-abad-b9daa04e0407","user_id":"30b00202-0ea3-4d3d-abad-b9daa04e0407","user_properties":{"projectId":{"value":"hardhat-project"},"userType":{"value":"Developer"},"hardhatVersion":{"value":"Hardhat 2.19.5"},"operatingSystem":{"value":"linux"},"nodeVersion":{"value":"v20.12.1"}},"events":[{"name":"task","params":{"engagement_time_msec":"10000","session_id":"0.29463604401884913"}}]} +0ms
    hardhat:core:hre Creating HardhatRuntimeEnvironment +0ms
    hardhat:core:hre Running task verify +4ms
    hardhat:core:hre Running task verify:get-constructor-arguments +1ms
    hardhat:core:hre Running task verify:get-libraries +1ms
    hardhat:core:hre Running task verify:verify +0ms
    hardhat:core:hre Creating provider for network habitat +27ms
    hardhat:core:analytics Hit for task sent successfully +673ms
    hardhat:core:hre Running verify:verify's super +1s
    hardhat:core:hre Running task verify:get-compiler-versions +2ms
    hardhat:core:hre Running task verify:get-etherscan-endpoint +1ms
    The contract 0xbcd2B61F456CB5D07bEf2B0eD5f5B9D5ED84C1c6 has already been verified
    hardhat:core:cli Killing Hardhat after successfully running task verify +0ms
    ```
1. For more features, please refer to
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
# Reference
1. [hardhat/packages/hardhat-verify at main · NomicFoundation/hardhat](https://github.com/nomicfoundation/hardhat/tree/main/packages/hardhat-verify)