# Deploy a contract with Hardhat

This section is a guide on how to deploy a smart contract on the B² Network using [Hardhat](https://hardhat.org/).

Hardhat is a popular smart contract development frameworks. It is used in the B² rollup as a default for deploying and automatically verifying smart contracts.

## Initial setup

- Get some test BTC from Bitcoin testnet faucet, and cross chain the test BTC from Bitcoin testnet to B² Network Testnet by test bridge.

- Install Hardhat and dependencies

    ```
    npm install --save-dev ethers hardhat @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers dotenv
    ```
    
- Run ***npx hardhat init*** to init a new project, and you will be shown some options to facilitate project creation:

    ```
    $ npx hardhat init
    888    888                      888 888               888
    888    888                      888 888               888
    888    888                      888 888               888
    8888888888  8888b.  888d888 .d88888 88888b.   8888b.  888888
    888    888     "88b 888P"  d88" 888 888 "88b     "88b 888
    888    888 .d888888 888    888  888 888  888 .d888888 888
    888    888 888  888 888    Y88b 888 888  888 888  888 Y88b.
    888    888 "Y888888 888     "Y88888 888  888 "Y888888  "Y888
    
    Welcome to Hardhat v2.19.3
    
    ? What do you want to do? …
    ▸ Create a JavaScript project
      Create a TypeScript project
      Create a TypeScript project (with Viem)
      Create an empty hardhat.config.js
      Quit
    ```

- Open the hardhat.config.js file and paste the below code:

    ```
    require("dotenv").config();
    require("@nomicfoundation/hardhat-toolbox");
    
    /** @type import('hardhat/config').HardhatUserConfig */
    module.exports = {
        solidity: "0.8.9",
        paths: {
            artifacts: "./src",
        },
        networks: {
            b2Testnet: {
                url: `https://zkevm-rpc.bsquared.network`,
                accounts: [process.env.ACCOUNT_PRIVATE_KEY],
            },
        },
    };    
    ```
    
## Add contract code and scripts

- Create a new contract code file, in the contracts folder, named Storage.sol

- Copy the below code and paste it in the Storage contract code:

    ```
    //SPDX-License-Identifier: MIT
    pragma solidity ^0.8.9;
    
    contract Storage {
        uint256 _count = 0;
    
        function set(uint256 count) public {
            _count = count;
        }
    
        function get() public view returns (uint256){
            return _count;
        }
    }
    ```
    
- Create a new file in the scripts folder deploy-storage.js

- Add the code below to the deploy-counter.js file:

    ```
    const hre = require("hardhat");
    
    async function main() {
        const deployedContract = await hre.ethers.deployContract("Storage");
        await deployedContract.waitForDeployment();
        console.log(
            `Storage contract deployed to https://testnet.bsquared.network/address/${deployedContract.target}`
        );
    }
    
    main().catch((error) => {
        console.error(error);
        process.exitCode = 1;
    });
    ```
    
- Before compiling the contract, you need to install the toolbox. You may need to change directory to install outside the project. Use this command:

    ```
    npm install --save-dev @nomicfoundation/hardhat-toolbox
    ```
    
- Compile your contract code (i.e., go back to the project root in the CLI):

    ```
    npx hardhat compile
    ```

- Now run the scripts:

    ```
    npx hardhat run scripts/deploy-storage.js --network b2Testnet
    ```
    
