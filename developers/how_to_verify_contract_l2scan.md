# Verify a Smart Contract with hardhat

This section is a guide on how to verify a smart contract on the B² Network using [Hardhat](https://hardhat.org/).
Hardhat is a popular smart contract development frameworks. It is used in the B² rollup as a default for deploying and automatically verifying smart contracts.

# Step-by-Step Guide

## 1. Install the hardhat-verify Plugin

Run the following command in the command line to install the hardhat-verify plugin:
`npm install --save-dev @nomicfoundation/hardhat-verify`

## 2. Configure the hardhat-verify Plugin

```js
require("@nomicfoundation/hardhat-verify");

module.exports = {
  // ...
  networks: {
    B2Mainnet: {
      url: 'https://rpc.bsquared.network',
      chainId: 223,
      accounts: {
        "your_private_key",
      },
    },
  },
  etherscan: {
    apiKey: {
      B2Mainnet: "no-api-key-needed"
    },
    customChains: [
       {
        network: "B2Mainnet",
        chainId: 223,
        urls: {
          apiURL: "https://explorer.bsquared.network/api",
          browserURL: "https://explorer.bsquared.network/"
        }
       },
    ]
  },
  // ...
};
```

## 3. Compile Your Smart Contract

Compile your smart contract using Hardhat by running the following command:
`npx hardhat compile`

## 4. Deploy Your Smart Contract

Deploy your smart contract using Hardhat as you normally would.

## 5. Verify Your Smart Contract

Run the following command to verify your smart contract:
`npx hardhat verify --network B2Mainnet CONTRACT_ADDRESS "Constructor argument 1" "Constructor argument 2" ...`

Replace `CONTRACT_ADDRESS` with the address of your deployed contract. If your contract has constructor arguments, include them after the contract address.

## 6. Check Your Verification Status

After running the verification command, you will receive a verification request ID. You can use this ID to check the status of your verification on the block explorer.
