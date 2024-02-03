# Account Abstraction with Particle Network


[Particle Network](https://particle.network) is the Intent-Centric, Modular Access Layer for Web3 applications. While Particle Network offers a range of solutions (including Modular Smart Wallet-as-a-Service) across the Web3 ecosystem, their flagship Bitcoin product is BTC Connect.


BTC Connect is the first account abstraction protocol for the Bitcoin ecosystem, unifying the experience between smart accounts on Bitcoin Layer-2s and standard BTC accounts through existing wallet interfaces. Particle Network has deployed ERC-4337 AA infrastructure natively on B², which developers can tap into to leverage smart accounts. This is achieved by having users connect to your application (through BTC Connect) with their UniSat, OKX, or Bitget wallet (with more on the way, such as Xverse, Leather, etc.). Upon connecting, a smart account will be generated and assigned to their BTC account on B². This smart account can then be used and authenticated directly through their native Bitcoin wallet.


Currently, BTC Connect has been deployed on the B² testnet, alongside native support for B² within its primary SDK, `@particle-network/btc-connectkit`.


Building an AA-enabled application on B² using BTC Connect only takes a few lines of code. This document will provide a high-level overview of this integration process, although for a detailed tutorial, visit the [Particle Network documentation](https://developers.particle.network/reference/btc-connect-web). 


## Introduction to BTC Connect: Configuration


BTC Connect is primarily available through its React-based JS library, `@particle-network/btc-connectkit`. To install it, run one of the two commands at the root of your project:


```shell=
yarn add @particle-network/connectkit @particle-network/chains


# OR


npm install @particle-network/connectkit @particle-network/chains
```


`@particle-network/btc-connectkit` needs to be initialized and configured through the `ConnectProvider` component (generally within your `index` file), wrapping the primary application component in which you intend to use BTC Connect.


This configuration process contains two halves, `options` and `connectors`. The first will be used to customize and authenticate the SDK through your `projectId`, `clientKey`, and `appId` from the [Particle dashboard](https://dashboard.particle.network), while the second will be used to define the wallets you'd like to be supported (currently, BTC Connect supports UniSat (`UnisatConnector`), Bitget (`BitgetConnector`), or OKX (`OKXConnector`)).


The following snippet is an example of what your `index` file _may_ look like once you've configured `ConnectProvider`.


```typescript=
import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  ConnectProvider,
  OKXConnector,
  BitgetConnector,
  UnisatConnector,
} from '@particle-network/btc-connectkit';


import { BSquaredTestnet } from '@particle-network/chains';


import App from './App';


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ConnectProvider
      options={{
        projectId: process.env.REACT_APP_PROJECT_ID, // --
        clientKey: process.env.REACT_APP_CLIENT_KEY, // Retrieved from https://dashboard.particle.network
        appId: process.env.REACT_APP_APP_ID, // --
        aaOptions: {
          accountContracts: {
            BTC: [
              {
                chainIds: [BSquaredTestnet.id],
                version: '1.0.0', // Will always be 1.0.0 for now
              },
            ],
          },
        },
        walletOptions: {
          visible: true, // Determines whether or not a dedicated wallet interface for the smart account is shown
        }
      }}
      connectors={[new UnisatConnector(), new OKXConnector(), new BitgetConnector()]}
    >
      <App />
    </ConnectProvider>
  </React.StrictMode>
);
```


With this complete, BTC Connect will be ready to use through the component you wrapped with `ConnectProvider` (`App` in the example above).You can nowbegin driving wallet connection and deploying smart accounts on B².


## Introduction to BTC Connect: General Usage


The BTC Connect SDK, `@particle-network/btc-connectkit`, can be used in three primary ways:
1. Facilitation of wallet connection through a built-in modal.
2. Execution of operations with the native Bitcoin account (inscriptions, P2P BTC transactions).
3. Execution of operations with the associated smart account (any contract call or transaction on B²).


Each type of operation has corresponding hooks exported by `@particle-network/btc-connectkit`, such as:
- `useConnectModal`, for wallet connection.
- `useAccounts`, to retrieve active Bitcoin addresses (after wallet connection).
- `useBTCProvider`, for controlling the native Bitcoin account.
- `useETHProvider`, for controlling the associated smart account on B².


Wallet connection is initiated through one primary function within BTC Connect, `openConnectModal()` from `useConnectModal`. Upon calling this function, the user will be shown a standardized connection interface containing the wallets previously defined within `connectors`.


After connecting with their wallet of choice, a smart account will be automatically generated and assigned to the user’s Bitcoin public key and address. For this, both `sendBitcoin` from `useBTCProvider` and `smartAccount` from `useETHProvider` will be available.


`smartAccount` from `useETHProvider` will act as the central object controlling the underlying smart account, handling everything from the conversion of transactions to UserOperations, the execution of UserOperations, etc.


In the example application shown below, we call `openConnectModal()` to onboard a user into the application. We then focus on two functions: `executeTxEvm`, which uses `smartAccount` to construct and execute a gasless transaction, and `executeTxBtc`, which uses `sendBitcoin` to transfer 1 satoshi back to the sender.


```typescript=
import React, { useState, useEffect } from 'react';
import { useETHProvider, useBTCProvider, useConnectModal } from '@particle-network/btc-connectkit';


import { notification } from 'antd'; // Optional, just a frontend component to indicate successful transactions
import './App.css';


const App = () => {
  const { smartAccount } = useETHProvider(); // For handling the smart account
  const { openConnectModal } = useConnectModal(); // For facilitating wallet connection
  const { accounts, sendBitcoin } = useBTCProvider(); // To send native Bitcoin and track active addresses


  const executeTxEvm = async () => {
    const tx = {
      to: "0x00000000000000000000000000000000000dEAD0", // Sample recipient, burn address
      value: '100000000000', // wei value, 0.0000001 BTC
      data: "0x" // Leave as 0x unless you're calling a contract
    };


    const feeQuotes = await smartAccount.getFeeQuotes(tx); // Converts tx to a list of potential UserOperations
    const { userOp, userOpHash } = feeQuotes.verifyingPaymasterGasless; // Chooses a gasless UserOperation (sponsored for free as this is on the bSquared testnet)
    const hash = await smartAccount.sendUserOperation({ userOp, userOpHash }); // Executes the UserOperation
    
    notification.success({
      message: 'Transaction Successful',
      description: (
        <div>
          Transaction Hash: <a href={`https://testnet.bsquared.network/tx/${hash}`} target="_blank" rel="noopener noreferrer">{hash}</a>
        </div>
      )
    });
  };




  const executeTxBtc = async () => {
    const hash = await sendBitcoin(accounts[0], 1); // Sends 1 satoshi back to the sender (the connected wallet)
    
    notification.success({
      message: 'Transaction Successful',
      description: (
        <div>
          Transaction Hash: <a href={`https://live.blockcypher.com/btc-testnet/tx/${hash}`} target="_blank" rel="noopener noreferrer">{hash}</a>
        </div>
      )
    });
  };


  return (
      // Your JSX
    );
};


export default App;
```


## Learn More


To learn more about the process covered above, Particle Network has a variety of content covering the implementation of BTC Connect, including:
- The GitHub repository for the code covered in this document: https://github.com/TABASCOatw/particle-btc-connect-demo
- The official `@particle-network/btc-connectkit` repository: https://github.com/Particle-Network/particle-btc-connect
- Tutorial video (covering the code on this document): https://twitter.com/TABASCOweb3/status/1750072016076464467
- Documentation: https://developers.particle.network/reference/btc-connect-web
- Blog post: https://blog.particle.network/btc-connect-bitcoin-account-abstraction