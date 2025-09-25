# Core Module Overview

## Mining Squared

* Mission and Positioning:

  Upgrade traditional Bitcoin mining to a "yield as liquidity" channel, automatically injecting real-time BTC rewards into programmable contracts and staking pools.

* Key Features

  1. Mining rewards can be directly diverted to user or AI Agent wallets.

  2. One-click earnings: Mining pool rewards can be obtained through DeFAI by selecting different strategies.

  3. Supports computing power NFTs/derivatives, providing a secondary market for BTC Hashrate.

* Coupling with Other Modules

  Provides BTC staking and fee funds to B² Hub; invests assets into different strategies for yield through B² Rollup; conducts strategy evaluation and selection through AI Signal, and automates participation in various strategies.

## B² Hub

* Mission and Positioning

  A Layer 1.5 between Bitcoin Layer 1 and Rollup, serving as a consensus and data availability center, providing blockchain infrastructure for AI Signal.

* Key Features

  1. PoSg (Proof of Signal + Stake): BTC/B2 staking + verified AI signals jointly determine voting power.

  2. Application Sharding: Multiple applications run in parallel, with state isolation but shared security.

  3. Threshold signature lightweight clients.

  4. Taproot commitment to Bitcoin.

* Coupling with Other Modules

  Provides final confirmation and DA for B² Rollup.

  Collects AI Signal signals to enhance consensus security.

## B² Rollup

* Mission and Positioning

  A high-throughput, EVM smart contract execution layer, anchored to Bitcoin through validity proofs.

* Key Features

  1. ZK/Validity batching + proof - data and state roots submitted to B² Hub, with finality periodically written to Bitcoin.

  2. Low fees & high performance.

  3. Supports EVM addresses and Bitcoin addresses.

* Coupling with Other Modules

  Relies on B² Hub's DA and PoSg final confirmation.

  Provides a scalable execution environment for DeFi, NFTs, RWA, and other applications.

## AI Signal

* Mission and Positioning

  A signal-driven Agentic AI layer that allows AI to natively hold, earn, and spend digital assets.

* Key Features

  Agent-Native Account Abstraction (A-AA): Modular permissions, multi-signature, social recovery.

  Signal bus: On-chain AI behavior, generating quantifiable signals.

  MoE/Dispatcher routes complex reasoning tasks.

* Coupling with Other Modules

  The signals generated are used by B² Hub to weight PoSg.

  On-chain native payments for AI-to-AI through U2.

## U2

* Mission and Positioning

  U2 is a native stablecoin of the B² Network, optimized for Agent workloads: target price 1 U2 ≈ 1 USD, serving as a stable unit for AI tasks, data subscriptions, and service settlements. U2 combines the high security of BTC with the usability of USD within the same technology stack of B² Network, providing a predictable settlement currency for Agentic AI, offering efficient capital utilization and hedging tools for miners and stakers, and feeding back every economic activity of the stablecoin into the network security of PoSg through Signal scoring.

* Key Features

  1. Over-collateralization: Supports native BTC as collateral. Target collateralization ratio CR >= 150%, governance adjustable.

  2. Anchoring Mechanism:

      1. Minting/Redeeming: Users deposit collateral to open a vault to mint U2; U2 can be redeemed by destroying it at any time at the oracle price + fees.

      2. AMO Market Making: The protocol's self-operated market making (AMO) maintains a buy-sell band of 1±ε (default ε=0.5%) across various DEXs.

      3. Stability Fee: Interest is charged based on the debt size (annualized can be dynamically adjusted by RL-Tuner), used for risk and liquidity management.

  3. Liquidation and Insurance: When CR falls below the liquidation line (e.g., 130%), auctions/buybacks are triggered; part of the penalty is injected into the insurance pool, shared with the PoSg Slash pool for risk control reserves.

* Coupling with Other Modules

  PoSg / Signal: The minting, redeeming, liquidation, and AMO transactions of U2 will generate Signal events and count towards the SignalScore of the corresponding delegated validators (fees are still paid in BTC/B2), mapping stablecoin usage behavior to consensus activity.

  Mining Squared: Miners can choose to automatically convert a portion of their earnings into U2 for AI task budgeting or hedging; rBTC collateral can be used to mint U2 with one click, improving capital utilization.

  AI Signal / A-AA: Agents can set stable budgets in U2 within the A-AA wallet (e.g., "daily 50 U2 model expenses"); during execution, the router converts U2 <-> BTC as needed to pay for Gas, reducing price volatility's impact on workflows.

  B² Rollup Applications: DeFi, payment, and subscription dApps can use U2 as a user-facing pricing currency while enjoying the PoW finality and cross-Shard atomic interoperability of the Hub.
