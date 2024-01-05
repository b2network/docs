# Rollup Layer

ZK-Rollup consists of several components, including Account Abstraction Module, RPC Service, Mempool, Sequencers, zkEVM, Aggregators, Synchronizers, and Prover.

## Account Abstraction Module

B² Network implements native account abstraction at Rollup Layer in Figure [B² Network Account Abstraction](https://ipfs.io/ipfs/QmVnG1MLdx8X8Wwk4Vxjooei7tw297wTtAWRpvWezwNDdZ). B² Network creates contract accounts controlled by users in the zkEVM. Contract accounts for Bitcoin address accounts are controlled by the user's Bitcoin private key, those for Ethereum address accounts by the user's Ethereum private key, and for Email accounts by the user's email. Users can generate sub-accounts through their contract account for different devices or DApps. Sub-accounts can have controlled permissions, like only sending standard transactions and not managing assets of the contract account. The controlling account can remove sub-accounts at any time. The contract account features a modular execution layer, which performs default operations or checks based on B² Network's and users' settings, such as account initialization, email account DKIM verification, transaction validation, account recovery, permission management, and asset locking. This execution layer is expandable and upgradable. Users' on-chain assets in B² Network are attributed to the contract account and can be managed through the controlling account (Bitcoin address account, Ethereum address account, or Email account).

The Account Abstraction module of B² Network, through its Transaction Bundler service, can implement a gas payment function on behalf of users. Upon receiving transaction messages signed by the user's controlling account or sub-accounts, the Transaction Bundler, based on the user's settings for gas payment or the interacting contract's settings, pays the gas for the user. It then collects other assets from the user or the interacting contract as compensation.

![B² Network Account Abstraction](https://ipfs.io/ipfs/QmVnG1MLdx8X8Wwk4Vxjooei7tw297wTtAWRpvWezwNDdZ)

## RPC Service

Users initiate transactions or send signed messages through wallets or services provided by DApps to B² RPC Service. Once these transactions or signed details are received, B² RPC Service performs preliminary validation, either directly sending them to the Mempool service or processing them for account abstraction before dispatch. B² RPC Service internally integrates the Transaction Bundler service of the Account Abstraction Module, which validates message signatures and generates corresponding transaction information based on the message content. The Transaction Bundler service offers gas payment on behalf of users, using BRC20 assets on  Bitcoin like ORDI, SATS, or directly deducting gas from the interacting contracts, facilitating gas-free functionalities for DApps. By employing horizontal scaling, B² RPC Service can enhance the performance of Rollup Layer. Third-party entities and developers can operate B² RPC Service and provide related services.

## Mempool

The Mempool serves as the storage for all pending transactions. Sequencers can access and order these transactions from the Mempool.

## Sequencer

The Sequencer in B² Network is responsible for ordering and packaging the transactions submitted by users, and then handing them over to the zkEVM for specific transaction execution. B² Network implements a Decentralized Sequencer service through B² Nodes, which update the Sequencer Set via a mechanism similar to DPoS. The Sequencers within the Sequencer Set provide transaction ordering and packaging services in sequence.

## zkEVM

The zkEVM, compatible with EVM, facilitates developers in constructing secure DeFi, NFTs, and other DApps. It also aids developers in migrating DApps from other EVM-compatible chains to B² Network. Combined with the Bitcoin Indexer Module of the B² Nodes, the zkEVM stores Bitcoin's state data, enabling developers to integrate the Bitcoin network into DApp development.

## Aggregators

The Aggregators access the sequencer's post-ordered transaction information and state information from the zkEVM. They either generate zero-knowledge proofs via the Prover or aggregate transactions and collate proof details from the Prover, formulating a transaction batch hash tree. This tree is then sent to the data availability layer for backup, ensuring rollup transaction data availability.

## Prover

The Prover's role is to generate validity proofs, representing the authenticity of a batch of user-submitted transactions. Initially, the Prover creates multiple ZK-STARK proofs based on the transaction batch and state information acquired from the Aggregator. By leveraging STARK Recursion, these ZK-STARKs are bundled to produce a single, extensive ZK-STARK. This ZK-STARK, being sizeable, is channeled out via the CIRCOM component to the SNARK builder, which in turn generates a ZK-SNARK validity proof, drastically reducing Gas costs. Finally, the generated proof returns to the Aggregator.

## Synchronizer

The Synchronizer ensures that information from B² Nodes is synchronized into the Rollup Layer, encompassing details like sequencer information, Bitcoin transaction data, and more.



In conclusion, the Rollup Layer procures user transactions via the RPC Service and stores them in the Mempool. Once sequencers have ordered these transactions, the zkEVM processes the transaction batch. The Prover then produces a zero-knowledge proof of transaction authenticity. Through the Aggregator, transaction and proof details are summarized and synchronized to B² Network's data availability layer, ensuring transaction veracity, data security, and data availability.