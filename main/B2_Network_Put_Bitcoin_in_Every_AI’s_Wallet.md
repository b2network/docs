# B² Network: Put Bitcoin in Every AI’s Wallet

Author: B² Network Team

Version: v2.0.0

Date: 2025.7.20

# Abstract

With the rapid expansion of autonomous intelligent agents (AI Agents) in various on-chain and off-chain scenarios, providing secure, permissionless, highly liquid, and globally accepted settlement assets has become a core demand for the new generation of infrastructure. Bitcoin (BTC), as the most recognized and value-storing digital currency, has long been disconnected from the AI ecosystem. B² Network envisions "Put Bitcoin in every AI’s wallet" and proposes a modular architecture that integrates BTC natively into the AI economic cycle, mainly consisting of five subsystems:

1. Mining Squared — A new generation BTC mining pool with revenue routing capabilities, which automatically injects real-time mining rewards into programmable contracts, driven by DeFAI, continuously providing BTC liquidity and staking assets to the network.

2. B² Hub is a "Layer 1.5" hub located between the Bitcoin main chain and various Rollups. It is centered on PoSg (Proof of Signal + Stake) as the core consensus: merging forfeitable BTC/B2 staking with on-chain verified AI Signal dual-weighting, truly achieving "useful computation is a secure budget." On top of this, the Hub adopts an Application Sharding architecture, splitting the execution layer into horizontally scalable sub-chains/service shards, allowing various services such as EVM contracts, AI services, and data storage to run in parallel under the same validator set without interference. Thus, B² Hub inherits the economic confirmation of Bitcoin PoW, the interactive experience of BFT second-level block production, and the flexible scalability of modular blockchains, becoming a high-performance bridge between BTC value and Agentic AI productivity.

3. B² Rollup - A Bitcoin Rollup based on validity proofs, which submits batch data and state roots to the B² Hub and periodically anchors to the Bitcoin mainnet using Taproot, achieving both fast local confirmations and Layer 1 economic security.

4. DSN-AI - An Agentic AI layer driven by Signal, providing Agent-Native Account Abstraction (A-AA), Signal Bus, and model routing, enabling agents to register, delegate validators, send/receive signals, and natively hold assets.

5. U2 - A new generation of stable settlement and intelligent stablecoins using BTC assets as collateral, aimed at Agentic AI. Using BTC assets as collateral to unlock BTC liquidity; building an AI-driven "adaptive collateral ratio and liquidation" engine to more quickly, reasonably, and safely adapt to market conditions; providing on-chain micropayment channels for Agents, offering a natural settlement layer for AI-to-AI business models, which can be seen as the next generation of "AI-native dollars"; supporting bank card services to unlock more consumption scenarios.

This article systematically explains how the above components work together to build the "computing power - signal - staking - value - consumption" closed loop:

* Mining rewards -> BTC staking -> PoSg consensus -> Final confirmation;

* AI behavior -> Signal fees -> Validator scoring -> Consensus weight enhancement;

* Rollup and applications -> AI-driven intelligent yield strategies -> Agent wallets and mining pools;

* BTC collateral -> issue U2 -> payment -> Agents micropayment.

Through formal security analysis and economic model derivation, we prove that PoSg can maintain a level of economic security comparable to traditional PoS under adjustable α/β parameters, while effectively converting AI work into contributions to network security. The B² Network provides the first practical unified paradigm for "Bitcoin × AI × Modular," injecting native BTC liquidity and finality assurance into the global agent economy.

# Keywords

Bitcoin, AI Agents, PoSg Consensus, Mining Squared, B² Hub, B² Rollup, Signal-Driven, Agent-Native Account Abstraction, Modular Blockchain.

# Summary

## Vision

Vision Review: "Put Bitcoin in Every AI’s Wallet."

In the next decade of the digital economy, AI Agents will evolve from passive executors to active market participants and value creators. They need a globally recognized, censorship-resistant, and highly liquid native asset to achieve autonomous settlement, collateralization, and incentive distribution. Bitcoin possesses these qualities but has long been disconnected from the AI ecosystem due to a lack of programmable bridges.

The core vision of B² Network is to bridge this gap—allowing every AI entity to natively hold, earn, and spend digital assets, thereby:

1. Empowering the Agent Economy

    * Using BTC as a unified value metric to simplify settlement friction across multiple chains and assets.

    * Enabling agents to automatically consolidate execution earnings, staking rewards, and service fees into the same asset pool, enhancing capital efficiency.

2. Enhancing Network Security and Sustainability

    * The "useful signals" generated by AI are quantified and injected into the PoSg consensus, allowing AI activity to directly translate into chain-level security contributions.

    * A three-spiral positive feedback loop forms between miner computing power, BTC staking, and AI signals: more computing power -> more BTC liquidity -> stronger security -> more AI adoption.

3. Promoting Deep Integration of Web3 and AI

    * Through Agent-Native Account Abstraction (A-AA), agents possess the same on-chain identity and permission model as humans.

    * Through Application Sharding and B² Rollup, a high-throughput, low-latency execution environment is provided for AI-native dApps, while inheriting Bitcoin's economic finality.

    * Provide on-chain micropayment channels for AI-to-AI through U2, bringing autonomous, fast, decentralized, and auditable payment channels to AI.

4. Building an Open, Composable Modular Ecosystem

    * Modules like Mining Squared, B² Hub, B² Rollup, and DSN-AI are decoupled and pluggable, facilitating integration by different developers as needed at various layers.

    * A unified BTC value base lowers the collaboration threshold across applications, stimulating innovation and capital influx.

With this vision, B² Network is committed to upgrading Bitcoin from "digital gold" to "fuel and settlement layer for AI," ensuring that every future intelligent interaction inherently carries the value and security of BTC, injecting lasting momentum into the decentralized economy built by humans and machines together.

## Core Module Overview

### Mining Squared

* Mission and Positioning:

  Upgrade traditional Bitcoin mining to a "yield as liquidity" channel, automatically injecting real-time BTC rewards into programmable contracts and staking pools.

* Key Features

  1. Mining rewards can be directly diverted to user or AI Agent wallets.

  2. One-click earnings: Mining pool rewards can be obtained through DeFAI by selecting different strategies.

  3. Supports computing power NFTs/derivatives, providing a secondary market for BTC Hashrate.

* Coupling with Other Modules

  Provides BTC staking and fee funds to B² Hub; invests assets into different strategies for yield through B² Rollup; conducts strategy evaluation and selection through DSN-AI, and automates participation in various strategies.

### B² Hub

* Mission and Positioning

  A Layer 1.5 between Bitcoin Layer 1 and Rollup, serving as a consensus and data availability center, providing blockchain infrastructure for DSN-AI.

* Key Features

  1. PoSg (Proof of Signal + Stake): BTC/B2 staking + verified AI signals jointly determine voting power.

  2. Application Sharding: Multiple applications run in parallel, with state isolation but shared security.

  3. Threshold signature lightweight clients.

  4. Taproot commitment to Bitcoin.

* Coupling with Other Modules

  Provides final confirmation and DA for B² Rollup.

  Collects DSN-AI signals to enhance consensus security.

### B² Rollup

* Mission and Positioning

  A high-throughput, EVM smart contract execution layer, anchored to Bitcoin through validity proofs.

* Key Features

  1. ZK/Validity batching + proof - data and state roots submitted to B² Hub, with finality periodically written to Bitcoin.

  2. Low fees & high performance.

  3. Supports EVM addresses and Bitcoin addresses.

* Coupling with Other Modules

  Relies on B² Hub's DA and PoSg final confirmation.

  Provides a scalable execution environment for DeFi, NFTs, RWA, and other applications.

### DSN-AI

* Mission and Positioning

  A signal-driven Agentic AI layer that allows AI to natively hold, earn, and spend digital assets.

* Key Features

  Agent-Native Account Abstraction (A-AA): Modular permissions, multi-signature, social recovery.

  Signal bus: On-chain AI behavior, generating quantifiable signals.

  MoE/Dispatcher routes complex reasoning tasks.

* Coupling with Other Modules

  The signals generated are used by B² Hub to weight PoSg.

  On-chain native payments for AI-to-AI through U2.

### U2

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

  DSN-AI / A-AA: Agents can set stable budgets in U2 within the A-AA wallet (e.g., "daily 50 U2 model expenses"); during execution, the router converts U2 <-> BTC as needed to pay for Gas, reducing price volatility's impact on workflows.

  B² Rollup Applications: DeFi, payment, and subscription dApps can use U2 as a user-facing pricing currency while enjoying the PoW finality and cross-Shard atomic interoperability of the Hub.


## Value Proposition

B² Network tightly couples the global consensus value of Bitcoin, the powerful productivity of AI agents, and the flexible scalability of modular blockchain: through Mining Squared, real-time mining rewards are directly injected into the network, providing a continuous flow of BTC liquidity for validators' staking and agent wallets; leveraging the PoSg consensus mechanism, the combination of "BTC/B2 staking + verified AI signals" is transformed into voting rights, directly mapping the useful work of AI into chain-level security budgets; under the application sharding of B² Hub and the validity proof of B² Rollup, it achieves dual finality with second-level local finality and periodic anchoring to the Bitcoin mainnet, while supporting the free assembly of any VM, sub-chains, and permissioned modules. Miners can participate simply by switching their revenue routing, and AI developers can quickly deploy based on familiar development stacks, achieving low barriers to entry, high throughput execution, and economic security, truly realizing "Put Bitcoin in every AI’s wallet" as a self-circulating flywheel that integrates computing power, signals, and value, creating a new ecosystem of "Bitcoin + AI + Modular Stack."

## Opportunities

In B² Network, different participants can find new momentum within the value closed loop of "mining power—BTC staking—signal-driven—modular execution."

For developers, the Application Sharding and Rollup SDK of B² Hub lower the barriers to on-chain deployment, and native BTC settlement eliminates cross-chain friction; with the signal API and A-AA wallet, any off-chain event can be transformed into an agent trigger, allowing for rapid deployment of high-speed payments, blockchain games, and high-frequency DeFi derivatives, all earning BTC fees through the shortest path.

Miners and computing power providers can route real-time mining rewards to the PoSg staking pool with one click through Mining Squared, continuing PoW income while adding consensus rewards and signal incentives; computing power can also be packaged as "computing power LSD" or delegated services, attracting DeFi and AI funds, creating additional revenue channels for small and medium miners.

AI service providers and model suppliers can package each model call, inference result, or data labeling into billable signals, receiving BTC payments in real-time; at the same time, the signal weight will be converted into voting rights for their delegated validators, directly transforming "useful AI work" into contributions to network security and bringing additional rewards to cooperative nodes.

Financial institutions can design new yield curves and structured products around PoSg staking and the signal market, providing BTC staking loans, hedging tools, and custody services for mining pools and validators; on B² Rollup, they can also issue stablecoins, notes, or leveraged products collateralized by BTC, achieving an efficient combination of on-chain settlement and off-chain clearing.

In summary, B² Network opens up multidimensional opportunities for developers, miners, AI suppliers, and financial institutions in technology, revenue, business, and financial innovation, collectively driving the positive flywheel of the "Bitcoin + AI + Modular" ecosystem.

# Introduction

## Background

For more than a decade, Bitcoin has accumulated the strongest monetary-level consensus and a market value of over $1 trillion as decentralized digital gold. However, its capital efficiency has been constrained by three structural factors: (1) low on-chain throughput, with the Base Layer capable of processing only about 7 transactions per second, which cannot support large-scale payments; (2) weak scripting capabilities, as the native UTXO script lacks Turing completeness and account abstraction, making it difficult to implement advanced financial primitives such as DeFi, derivatives, and stablecoins; (3) a single revenue channel, where holders have few sustainable on-chain earning scenarios aside from long-term appreciation, resulting in millions of BTC sitting idle in cold wallets. This "high market value, low activity" contradiction is widely referred to as Bitcoin Capital Inefficiency.

In stark contrast, the generative AI and autonomous agent economy has seen exponential growth over the past three years: ChatGPT has driven the popularity of LLMs, and Agent-Framework and Auto-Everything enable AI to perceive, reason, decide, and execute without human intervention. Global AI service spending has surged from less than $20 billion in 2022 to an estimated over $200 billion by 2025. A vast number of agents frequently exchange data, invoke models, and settle computing and bandwidth costs between cloud and IoT nodes, creating an urgent need for a neutral, permissionless, highly liquid global settlement asset that can be natively held by machines.

In reality, these two rapidly developing tracks have little intersection:

* Existing AI task settlements mainly rely on centralized payments or USD stablecoins, unable to enjoy Bitcoin's monetary attributes of "absolute scarcity, censorship resistance, and cross-border accessibility";

* Layer 2 solutions like Lightning focus on peer-to-peer payments, making it difficult to meet the needs of complex contracts and large-scale state synchronization;

* Emerging solutions like Bitcoin Rollup and BitVM are still in the early experimental stage and have not yet formed a one-stop solution aimed at AI.

Therefore, "how to let the value and security of Bitcoin serve the AI economy" and "how to allow the real useful work of AI to feed back into the security and revenue of the Bitcoin network" have become dual challenges facing developers and researchers, as well as the goals of the B² Network's advancement.

## Why AI Needs Bitcoin

1. Global Permissionless Value Settlement Layer

    Autonomous agents perform tasks in every corner of the internet—scraping data, calling models, renting GPUs, purchasing APIs—if they rely on centralized payment interfaces, they face not only geographical and regulatory barriers but also service interruptions due to account freezes, exchange restrictions, and KYC limitations. Bitcoin transactions on-chain require no permission and operate around the clock, naturally aligning with machines' needs for 24×7 settlement and cross-border collaboration.

2. Finality and Anti-Censorship Guarantee Execution Certainty

    AI Agent transactions are typically triggered in milliseconds, but once a rollback or chargeback occurs, the upper decision chain collapses. Bitcoin's PoW provides the highest economic finality in the industry—once a block is confirmed, the cost of tampering is extremely high; combined with B² Network's Layer 1.5 early finality, Agents can achieve "high probability finality" in seconds and "absolute finality" in minutes.

3. Value Stability and Inflation Hedge

    Most AI service revenues are denominated in USD or fiat stablecoins, exposing them to long-term inflation risks. BTC, with a fixed supply cap of 21 million coins and a halving issuance mechanism, provides an anti-inflation asset pool for AI companies and agents; in a high-volatility environment, holding some BTC can also hedge against stablecoin decoupling or regulatory pressure.

4. Machine Verifiable and Programmable Wallet Primitives

    Bitcoin UTXO is naturally suited for implementing auditable and composable machine wallets on-chain. Coupled with B² Network's Agent-Native Account Abstraction (A-AA), Agents can flexibly manage multi-signatures, time locks, social recovery, and other permissions under the same address without complex bridging and cross-chain mapping.

5. Incentives and Security Coupling

    In the PoSg design, signals generated by AI directly affect validators' voting power; the more "useful work" an Agent performs, the greater the weight supporting network security, which in turn enhances the safety of Agent funds and execution availability, forming a positive feedback loop of "security-incentive."

6. Micro-Payments and Batch Settlement Efficiency

    Bitcoin Layer 2 (Lightning, Rollup ecosystem) has proven that BTC can support millisecond-level, low-cost micro-payments. B² Hub introduces Application Sharding and aggregated batch submissions, compressing a series of micro-transactions into a single Taproot proof written to L1, significantly reducing on-chain costs, allowing AI Agents to confidently perform high-frequency calls.

7. Ecosystem and Liquidity Spillover Effects

    BTC accounts for over 40% of the total cryptocurrency market cap and has the broadest base of holders. Pricing AI fees, rewards, staking, and DeFi primitives in BTC can directly inherit its global liquidity and deep derivatives market, opening up richer financing and hedging tools for Agents and their operators.

In short, Bitcoin provides the AI economy with censorship-resistant value storage, programmable machine assets, strong finality, and global liquidity. Through B² Network's modular stack, these features can be deeply integrated with high-performance execution layers, signal-driven consensus, and AI-native account systems, making it possible for "every AI wallet to securely and efficiently hold and use BTC."

## Limitations of the Current Solutions

Although the Bitcoin ecosystem and the AI field have been attempting to address the issues of value settlement and computational synergy through their respective Layer 2 or sidechain expansions, as well as on-chain AI frameworks in recent years, there remains a significant gap in achieving the goal of "enabling AI to natively use BTC," primarily manifested in the following five points:

1. Payment-oriented Layer 2 is difficult to support complex states

    * The Lightning Network relies on multi-hop channels, state maintenance, and offline counterpart collaboration; once an off-chain channel fails or a counterpart maliciously goes offline, the AI Agent must revert to L1 settlement, making the process overly complex and the delays unpredictable.

    * Existing upgrade solutions like Ark and Eltoo focus on single payment use cases and lack native support for complex smart contracts, multi-asset settlements, and cross-Agent atomic composite transactions.

2. Emerging Bitcoin Rollups and BitVM are still in the experimental stage

    * Most Bitcoin Rollup solutions (Rollkit-BTC, Botanix, Merlin, etc.) have not yet validated their data availability and security models on the mainnet, and there is a scarcity of available tools, SDKs, and developer ecosystems.

    * BitVM achieves general computation through off-chain execution + Taproot dispute resolution, but it has a high number of interaction rounds and a long dispute window, making it unsuitable as a real-time settlement layer for high-frequency AI calls.

3. AI × Blockchain projects generally rely on ERC-20 or custom tokens

    * Projects like Fetch.ai, Bittensor, and Autonolas mostly issue new tokens as billing and incentive units, which, while facilitating the creation of economic models, disconnect Bitcoin's liquidity and reintroduce fiat currency exchange and regulatory risks.

    * The consensus security of these projects is not directly coupled with BTC, making it impossible to leverage Bitcoin's PoW economic finality to protect large amounts of funds.

4. Lack of machine-friendly account abstraction and a "work equals security" closed loop

    * Existing on-chain account models are mostly based on EOA or contract accounts, with permission configurations and recovery processes often designed for human users, failing to meet the key management and permission layering needs of large-scale Agent automation scenarios.

    * The connection between staking weight and real on-chain work is weak, making it impossible to directly convert the "useful signals" of AI Agents into the network's security budget.

5. Cross-chain bridges and multi-asset mental burden

    * AI task execution often spans cloud vendors and cross-chain environments; if frequent exchanges between various assets like ETH, USDC, USDT, and FET are necessary, it not only leads to price slippage and liquidity fragmentation but also expands compliance and hacking risk exposure.

    * Bridging protocols (multi-signature bridges, light client bridges) are frequently attacked, exposing highly automated Agent systems to uncontrollable black swan risks.

6. Lack of AI-oriented payment channels for stablecoins based on Bitcoin's native properties

    * Price exposure and budget uncertainty: Directly priced in BTC, the per-instance/streaming fees for AI tasks are affected by price fluctuations, making it difficult to control cost ceilings and long-term budgets.

    * Dual-currency friction: Applications priced in stablecoins while Gas is paid in BTC/B2 require agents to frequently exchange small amounts and replenish, leading to slippage, failed retries, and counterparty risk.

    * Micropayments/high-frequency unfriendly: Existing channels lack primitives for machine-oriented streaming payments, limits/rates, and batch settlements, making costs and confirmation delays uncontrollable for sub-dollar level high-frequency calls during congestion.

    * Finality and audit disconnection: The finality of multi-chain stablecoins relies on other chains or custodians, making it impossible to anchor settlement evidence stably to Bitcoin, resulting in insufficient institutional-level reconciliation and traceability.

Therefore, the current ecosystem either sacrifices Bitcoin's native security and liquidity or fails to meet the high-frequency, complex, multi-party interaction needs of AI Agents. B² Network specifically addresses these pain points by directly integrating BTC into the AI settlement path and merging "BTC staking + AI signals" into the same security budget through PoSg consensus, filling the gaps in existing solutions.

## Summary

Bitcoin possesses the global liquidity, censorship resistance, and strong finality that the AI economy urgently needs, but due to insufficient scalability and contract capabilities, it forms a "value island" in the AI world. Existing cross-chain or spontaneous token solutions cannot simultaneously ensure security, support complex states, and maintain BTC's native liquidity. B² Network aims to break this barrier by building a new type of infrastructure that directly introduces U2 issued with BTC as collateral into AI settlement, allowing useful AI work to contribute back to on-chain security.

# Overview

## System Architecture Overview Diagram

![B² Network Architecture Overview](https://github.com/Stonepapa/images/blob/main/b2/B2_Architecture_Overview.png?raw=true)

## Module Description and Role Positioning

B² Network consists of five interconnected core modules. Each has its own responsibilities and forms a closed loop through BTC value flow and Signal control flow.

Mining Squared is responsible for automatically aggregating and routing the BTC earnings mined by miners in real-time. Hashrate providers submit their hash rates, and the earnings routing contract distributes BTC according to a preset ratio: part of it goes directly into the validator's staking pool, while another part can be credited to the agent's account. This module maintains full compatibility with Bitcoin's PoW consensus while providing a continuous source of liquidity for the upper layer.

B² Hub is the Layer 1.5 hub of the system. It adopts a PoSg (Stake + Signal) consensus, operating under the same set of validators with Application Sharding to achieve parallel sub-chains. Validators run PoSg nodes, while agents delegate their SignalScore to target validators, influencing their voting power. The Hub is also responsible for periodically writing the sharded DA root into Bitcoin Layer 1 using Taproot, thus achieving both second-level BFT finality and mainnet-level economic finality.

B² Rollup provides a computationally intensive or contract-complex execution environment. The Sequencer aggregates transactions and generates ZK/Validity proofs, then submits the batch data to B² Hub. All fees in the Rollup are directly priced in BTC, allowing dApps to enjoy high TPS and rich contract functionalities without introducing additional tokens.

The DSN-AI layer is aimed at the agent ecosystem. The Signal Bus transforms on-chain events into billable signals, and Agent-Native Account Abstraction (A-AA) allows each agent to have a programmable BTC wallet and permission system. Model providers can package inference services into subscribable Signals; agents obtain task-driven incentives by sending or receiving signals while returning the paid BTC and signal weight to their delegated validators.

U2 is the native stable settlement layer of the network. It uses BTC as over-collateral (target collateralization rate ≥150%) and stabilizes the exchange rate of 1 U2 ≈ 1 USD through oracles. The AI-driven liquidation engine automatically adjusts collateral rates and liquidation parameters based on market fluctuations, ensuring system robustness. U2 provides Agents with a price-stable micropayment channel—AI tasks can be accurately priced without being affected by BTC volatility. At the same time, operations such as minting, redeeming, and liquidating U2 generate Signal events, which are counted towards the validators' SignalScore, directly mapping stablecoin activities to network security contributions. Through the AMO (protocol-owned market making) mechanism, U2 maintains deep liquidity across various DEXs and supports traditional payment channels such as bank cards, bridging on-chain and off-chain consumption scenarios.

The overall role distribution is as follows:

* Miners inject computing power earnings into the network through Mining Squared;

* Validators maintain PoSg consensus in B² Hub and receive additional rewards based on Signal activity;

* AI agents register, delegate, and settle tasks in BTC on DSN-AI, with the generated signals enhancing the voting power of their dependent validators;

* Developers can deploy applications on Rollup or Hub sub-chains, using BTC directly as Gas and incentives;

* The mortgagor locks BTC to mint U2, releasing liquidity while retaining the appreciation potential of BTC;

* The liquidator monitors the collateral ratio, provides liquidity when the system needs it, and earns liquidation rewards;

* End users or institutions interact with the entire stack through agents or front ends, enjoying "BTC-native AI services and financial primitives."

In this way, computing power - staking - signals - execution layer - payments are tightly coupled, forming a self-driven growth flywheel.

## Data and Value Flow

In B² Network, BTC flow, Signal flow, and proof flow act like three parallel blood vessels, weaving computing power, staking, security, and execution layers into a closed loop. Below, we will explain their paths, key milestones, and interactions one by one.

### BTC Flow

1. Source: Mining Squared

    * Miners submit computing power -> Real-time mined BTC enters the Mining Squared revenue pool.

    * Revenue routing contracts split according to strategy:

      1. Automatically staked in the B² Hub's Staking Module;

      2. Directly deposited into Agent-Native wallets as needed, providing startup funds for agents;

      3. Some can choose to collateralize and mint U2 to obtain stable liquidity.

2. Staking and Consensus

    * Staked BTC is locked in the Staking Module, generating corresponding Stake shares.

    * Stake, along with subsequent SignalScore, determines the Voting Power of validators, participating in PoSg block production and earning block fees.

3. U2 Minting and Circulation

    * BTC collateral minting: Users/miners can lock BTC in the Vault contract, minting U2 based on oracle prices and collateralization ratios (≥150%).

    * Liquidity release: Minted U2 can be used for:

      * AI Agent task payments (inference fees, data subscriptions, computing power rentals)

      * DEX liquidity provision, earning trading fees

      * A stable pricing unit for inter-institutional settlements

    * Value return: The Signal weight generated from U2 usage feeds back into the PoSg consensus, enhancing network security.

4. Fees and Profit Sharing

    * Rollup and various Shard dApps pay Gas in BTC or U2; these fees are shared among PoSg validators based on weight.

    * U2 related fees:

      * Stability Fee: Interest charged based on debt size, flowing into the risk reserve pool

      * Liquidation penalty: The portion of the liquidation penalty when collateralization is insufficient enters the insurance pool

      * AMO market-making revenue: Trading fees generated from liquidity controlled by the protocol flow back into the system

    * Validators can choose to re-stake their profits, mint U2, or distribute them externally, forming a positive cycle of "revenue -> staking/U2 -> more revenue."

5. Liquidation and Risk Management

    * When the BTC price drops, causing the collateralization ratio to fall below 130%, a liquidation auction is triggered.

    * Liquidators use U2 to purchase discounted BTC, maintaining the system's solvency.

    * Liquidation profit: BTC price difference - U2 cost = liquidation profit, incentivizing market participants to actively maintain system health.

6. Exit and Liquidity

    * BTC Path:

      * Unlocking staked BTC requires waiting for a freeze period; unlocked BTC can be returned to miners or used by Agents for new business expenses.

      * U2 debt redemption: Destroy U2 + pay stability fee to retrieve the collateralized BTC.

    * U2 Path:

      * Exchange for BTC or other assets through AMO on DEX

      * Used for payments for various services within the network (no need for exchange)

      * Exchange for fiat currency consumption through bank card channels

    * Through Lightning, CEX, or on-chain bridging, users can transfer BTC/U2 back to external ecosystems at any time, ensuring high liquidity.

7. Compound Revenue Cycle

    * Mining Squared revenue → BTC collateral → Minting U2 → AI payments/DeFi revenue → More BTC accumulation

    * Signal generated from U2 circulation → Enhances validator weight → Earns more block rewards → Increases BTC revenue

    * Forming a triple revenue model of "BTC-based appreciation + U2 liquidity revenue + Signal network rewards."

Thus, the BTC flow not only includes the staking and circulation of native BTC but also creates a parallel value circulation system through the U2 stablecoin—BTC provides value anchoring, while U2 offers liquidity and stable pricing. The two are deeply coupled through collateralization/redemption mechanisms and Signal incentives, jointly supporting the economic activities of the entire network.

### Signal Flow

1. Generation and Submission

    * After completing tasks at the DSN-AI layer, the AI Agent calls submitSignal() to put the event summary, weight, and proof on-chain.

    * The Sender and each Receiver must be registered Agents, each delegated to the target validator.

2. Verification and Scoring

    * The SignalRouter of B² Hub checks signatures, fees, validity, and proof.

    * Upon passing, the corresponding validators of the sender and receiver each accumulate weight to their SignalScore.

    * Transaction fees (i.e., weight) are paid in a lump sum by the sender to prevent spam signals.

3. Impact on Consensus

    * The end of the Epoch snapshots Stake and SignalScore; PoSg recalculates validator weight with VP = α·Stake + β·SignalScore.

    * Validators of active Agents have a higher probability of block production in the next Epoch and receive more block rewards, incentivizing Agents to continue generating "useful signals."

4. Business Trigger

    * The Signal Bus broadcasts events to subscribed sub-chains or off-chain services, triggering Rollup contract execution, model routing calls, or external APIs.

    * The composability of the entire chain is established: signals act as schedulers, linking on-chain state changes with off-chain AI services.

### Proof Flow

1. Rollup Batch Proof

    * Sequencer aggregates user transactions -> generates batches and ZK/Validity proofs.

    * The proof is submitted along with batch data to the corresponding Shard of the B² Hub, which verifies it and provides a finality with seconds-level BFT.

2. Data Availability (DA) Commitment

    * All transaction data from Shards/Rollups is sliced, erasure-coded, and then generates a Namespace Merkle Tree root (NMT root).

    * Every 10 minutes, these roots are aggregated + threshold signatures, packaged into a Taproot transaction, and written to Bitcoin Layer 1.

    * Light clients only need to verify the threshold signatures and Bitcoin blocks, thus trusting the upper layer state.

3. Proof Feedback and Challenges

    * If the ZK proof is invalid or data is lost, any node can submit fraud evidence; PoSg validators will execute a slash on malicious batches.

    * The proof flow thus bears the dual responsibility of "state correctness + data availability."


* BTC flow converts computational power gains into a loop of staking and transaction fees, providing economic security and liquidity.

* Signal flow maps the actual work of AI into voting rights, directly enhancing chain-level security and driving application interactivity.

* Proof flow ensures correct execution, data availability, and ultimately anchors all sub-chain states to the Bitcoin main chain.

The three flows intertwine to form a closed loop: BTC gains new revenue scenarios while empowering AI, the useful signals from AI enhance the security margin of BTC staking, and the proof mechanism encapsulates all of this under the strong finality of Bitcoin PoW, achieving a self-consistent cycle of "value-data-security."

## Lifecycle

TODO IMAGE: Register -> Stake -> Signal -> Consensus -> Commit to Bitcoin

1. Register

    * Validators: Run nodes, register public keys, endpoints, and reward addresses on the B² Hub chain, and receive a Validator ID.

    * Agents: AI Agents register A-AA accounts on the Agent Registry chain and choose to delegate to a specific validator; once registered, they can hold BTC/B2 and call the Signal API.

2. Stake / Delegate

    * Location: Users (individuals, miners, institutions, Agents) deposit BTC or B2 into the staking contract of the B² Rollup. Assets are held in escrow at the Rollup layer but are mapped on-chain as StakingShare.

    * Delegation Logic: Stakers can delegate any share to different validators, supporting "one stake, multiple validator allocation"; changes take effect in the next Epoch.

    * Mining Squared and DeFAI:

    * DeFAI acts as a strategy aggregator, running a set of agents to dynamically allocate funds across multiple DeFi scenarios (market making, lending, liquid staking, etc.);

    * B² Hub staking is one option in the DeFAI strategy pool—when the PoSg yield is higher than external protocols, Agents will automatically convert part of the funds into StakingShare and delegate to the most profitable validator;

    * The comprehensive yield from DeFAI flows back to the stakers or is reinvested.

3. Signal

    * After executing tasks, agents call submitSignal(), packaging event summaries, weights, and proofs.

    * B² Hub verifies signatures, fees, and proofs; upon approval, the validators delegated by both the sender and receiver accumulate SignalScore according to weight.

    * The sender bears all costs (to prevent spam), and the receiver must ACK on-chain to score.

4. Consensus (PoSg Epoch Loop)

    1. Snapshot: Freeze the current StakeMap and SignalPool;

    2. ValidatorSet Update: Select the top N nodes with the highest weight according to VP = α·Stake + β·SignalScore;

    3. Threshold Key Generation: The new validator set runs FROST DKG;

    4. CometBFT Block Production: Weighted proposals, 2–3 seconds finality;

    5. Reward / Slash: Block fees + signal rewards are distributed according to VP; double signing or data availability violations trigger slashing.

5. Commit to Bitcoin

    * All transactions from Shard/Rollup generate NMT roots through slicing and erasure coding;

    * B² Hub aggregates root hashes and threshold signatures approximately every 10 minutes, writing a Taproot transaction;

    * Light clients only need to verify this transaction to obtain PoW finality of the on-chain state.

Summary

* Users stake BTC/B2 in the B² Rollup and freely delegate to validators;

* DeFAI dynamically migrates funds between multiple strategies through Agents, with "B² Hub staking" being one optional strategy in the yield pool;

* Signals convert useful AI work into validator weight; PoSg achieves consensus in seconds, subsequently granting economic finality through Bitcoin PoW.

This forms a cycle of "Stake -> Signal -> Consensus -> Yield -> Re-stake/Redistribute," connecting external DeFi with the B² Network ecosystem, continuously amplifying the synergy between BTC and AI.

# Core Concepts and Terminology

## Signal / SignalScore

### Signal

In the B² Network, a Signal refers to an event message generated by an AI Agent and verified on-chain. It maps "useful AI work" to measurable economic value and directly impacts consensus security. Each Signal contains the following core fields:

* id: keccak256(sender‖nonce‖timestamp)

* senderAgent: Registered A-AA address

* receiverAgents: List of at least 1 registered Agent

* weight: Economic weight of the Signal (in sat)

* expiry: Expiry block height

* payloadHash: Task result or data summary

* proof: Verifiable proof (ZK-SNARK / signature aggregation / hash pre-image, etc.)

* sig: Schnorr/ECDSA signature of senderAgent

Economic implications:

* weight is considered a one-time signal fee. Once paid by the sender, it is either burned or allocated to the block validators, providing income while preventing spam.

* The validators delegated by both the sender and each receiver will count this weight towards SignalScore, creating a two-way incentive.

Signal Lifecycle

1. Generation: The Agent completes reasoning, off-chain calls, or data labeling, constructs the Signal, and pays the weight.

2. Submission: Calls the submitSignal() transaction, specifying the list of receivers.

3. Verification: B² Hub checks

    * Whether the sender/receiver is registered and the delegation is valid

    * weight ≥ minSignalFee and does not exceed MAX_WEIGHT

    * Signature, proof, uniqueness, and not expired

4. ACK: The receiving Agent confirms on-chain (ackSignal(id)); otherwise, it does not count towards their validator score.

5. Scoring:

    * Validators delegated by the sender: + weight

    * Validators delegated by each receiver: + weight / n (default evenly distributed, customizable ratio)

All verified Signals enter the SignalPool, waiting for unified settlement at the end of the Epoch.

### SignalScore

* For any validator *v*:

$$
\text{SignalScore}_v = \sum_{\text{agent} \in \mathcal{D}_v} \sum_{\text{sig} \in \mathcal{W}} \text{weight}
$$

Where $\mathcal{D}_v$ is the set of all Agents delegated to *v*, and $\mathcal{W}$ is the set of Signals related to these Agents in the most recent *M* Epochs.

* The scoring window *M* (e.g., 24 h or 168 h) is adjustable in governance, smoothing noise and preventing one-time score manipulation.

* The system sets a hard upper limit: $\text{SignalScore}_v \le k \times \text{Stake}_v$ (typical *k = 3*), to avoid zero-stake signal monopolization.


Role in PoSg:

The consensus layer is defined by the formula

$$
\text{VotingPower}_v \;=\; \alpha \cdot \text{Stake}_v \;+\; \beta \cdot \text{SignalScore}_v
$$,

which combines staking and signals into voting power. The parameters $\alpha$ and $\beta$ are determined by on-chain governance (default 0.7 / 0.3). Therefore:

* More staking -> increases security collateral;

* More useful signals -> directly enhances votes;

* Both drive validators to achieve higher block production probability and block rewards.

Anti-cheating and risk control:

| Risk | Mitigation Measures |
| :---- | :---- |
| Fake recipient score inflation | Recipient must provide on-chain ACK; ACK failure does not count towards score |
| Micro garbage signals | minSignalFee dynamically adjusted with network load; weight directly burned |
| Monopolization of excessive weight | MAX_WEIGHT_PER_TX limits; SignalScore ≤ k × Stake |
| Sybil accounts | Sender fees paid in one lump sum, cost linear to transfer count; optional ZK-KYC proof |
| Invalid proof | Verifiable proof attached with transaction; anyone can submit fraud evidence during the challenge period to trigger Slash |

Signal transforms AI task results into on-chain events; SignalScore maps the economic weight of these events into consensus voting power. Together, they allow "useful work" to directly enhance chain security and provide quantifiable economic returns for active AI Agents and their underlying validators.

## Agent / Agent-Native Abstract Account (A-AA)

### Agent

Positioning of Agent:

In the B² Network, an Agent refers to a program entity capable of autonomously executing perception, reasoning, decision-making, and on-chain interactions. It can be an independently operating LLM-Bot or a wallet bot that automates operations on behalf of individuals or enterprises. Agents trigger workflows by sending and receiving Signals and use BTC/B2 as a fuel settlement model for calling, computing power leasing, and various on-chain service fees.

### Agent-Native Abstract Account (A-AA)

#### Why A-AA is Needed?

1. Machine-friendly key and permission management

    Traditional EOA/contract accounts are often oriented towards human signatures or single private key custody, which is not suitable for large-scale agent automation.

2. Native BTC payments

    AI tasks are high-frequency and low-value, requiring deep integration with account permission systems for second-level BTC settlement.

3. Upgradeable, recoverable, and socially recoverable

    Agent logic, models, and keys may iterate; relying solely on a single key means total loss if it is leaked.

4. On-chain composability

    Agents need atomic, multi-party interactions and modular permissions to be reused across different contracts and Rollup environments.

#### Core Design Elements of A-AA

| Component | Function |
| :---- | :---- |
| Root Keyset | A multi-signature or threshold Schnorr public key set that controls high-security operations (upgrades, recovery, delegate modifications). |
| Session Keys | Used for short-cycle batch signing or specific dApp authorizations, automatically revoked upon expiration. |
| Permission Modules | Plugin-based strategies (limits, multi-approval, time locks, conditional transfers). |
| Agent Registry | On-chain mapping table: agentAddr -> {delegateeVal, pubkeyRoot, version}. |
| Delegate Mapping | Records the current validator address and effective epoch that the Agent is delegating to. |

Compatibility: A-AA adopts a composable script tree similar to BTC Taproot, allowing unified verification in B² Rollup or B² Hub sub-chains; the same Agent address can share permission logic across sub-chains.

#### Account Lifecycle

1. Creation

    Developers call createAgent(rootKeyset, initialDelegate, metadata), and a unique Agent address is issued by the Hub.

2. Fund Injection

    * Off-chain: Recharge BTC to this address via Lightning/CEX.

    * On-chain: Miners / DeFAI strategies directly transfer to the Agent.

3. Delegation and Staking

    The Agent calls delegateValidator(valAddr), assigning all its SignalScore weight to the target validator.

4. Task Execution

    * Send Signal -> Trigger on-chain or off-chain workflows;

    * Receive Signal -> Decide whether to automatically execute payments, data writing, or forwarding based on permission modules.

5. Upgrade / Recovery

        Super multi-signature scheme: upgradeModule(newModuleHash) or recover(newRootKeyset), requiring Root Keyset to reach threshold signatures.

6. Deregistration

When the Agent's use case ends, selfDestruct() can be called to release funds and deregister the Registry entry.

#### Example Permission Module

* RateLimiter: Limits the maximum payment of n sat or m model calls within a block to prevent being hijacked and burning money.

* TimeLock: Large transactions must wait t seconds/blocks, allowing for manual review within the window.

* Guardians: Keys can only be reset after external cold wallet or multi-signature guardian approval.

* ConditionPay: Funds are automatically released only when a certain type of Signal or off-chain proof meets the conditions.

#### Security and Risk Control

* Hierarchical Keys: High-value operations are managed by the Root Keyset, while low-value micropayments use Session Keys, accelerating execution while reducing risk exposure.

* Off-chain Audit Hooks: The permission module can call off-chain risk control services (e.g., malicious model detection), returning a boolean value to determine whether the transaction continues.

* Automated Slash Alerts: If an Agent is detected being used for score manipulation or sending false signals, the system can freeze its Delegate and revoke Signal weight.

Agent-Native Abstract Account (A-AA) provides agents with an upgradeable, multi-signature, modular permission and native BTC payment comprehensive account system. It ensures high frequency and flexibility of machine operations while preventing key leakage and malicious calls through multi-layer security mechanisms, laying the technical foundation for "AI wallets holding BTC" at the account level.

## PoSg (Proof of Signal + Stake)

PoSg is the native consensus mechanism of B² Hub, which introduces economic signals (Signal) generated by AI Agents as a second-dimensional weight on the basis of traditional staking (Stake), combining "capital collateral" with "useful work" into the same voting power formula. In short: staking BTC/B2 provides economic security, and SignalScore reflects on-chain activity, both jointly determining the validator's votes and rewards.

### 1. Components

* Stake

  The BTC or B2 staked by users in B² Rollup, the total amount can be increased or decreased at any time but is frozen within the current Epoch.

* SignalScore

  The weighted sum of all signals sent/received by Agents delegated to that validator in the last M Epochs.

  Measures the Agent's true contribution to the network through double scoring (sender + receiver).

* Voting Power

  $$VP_v \;=\; \alpha \cdot Stake_v \;+\; \beta \cdot SignalScore_v$$

  Where $\alpha+\beta=1$, default $\alpha=0.7$, $\;\beta=0.3$, adjustable through on-chain governance.

* Epoch

  A fixed time window (e.g., 1 hour). At the end of the Epoch, Stake and SignalScore are re-snapshot, updating the validator set.

### 2. Operating Process (High-Level Perspective)

1. Snapshot freezes StakeMap and SignalPool;

2. ValidatorSet Selection sorts by VP and takes the top N;

3. Threshold key generation runs FROST-DKG to produce the public key for this Epoch;

4. BFT block production uses CometBFT, proposing in a weighted round-robin manner by VP, with a finality of 2-3 seconds;

5. Reward / Slash block fees + signal rewards are distributed according to VP; double signing, being offline, or invalid DA triggers penalties;

6. Roll over to the next Epoch to recalculate VP, repeating the cycle.

### 3. Key Parameters and Governance

| Parameter | Meaning | Typical Value | Adjustment Method |
| :---- | :---- | :---- | :---- |
| α / β | Stake vs Signal weight | 0.7 / 0.3 | DAO proposal, delayed effect |
| minSignalFee | Minimum fee for a single Signal | 0.1 B2 | Automatically adjusts with network load |
| M | Signal scoring window | 24 h | Governable |
| k | Signal to Stake upper limit ratio | 3 | Brush score threshold |

### 4. Security and Economic Characteristics

* Economic security: Stake provides quantifiable penalty collateral; when β ≤ 0.5, attackers still need to hold a large amount of BTC/B2 to manipulate votes.

* Useful work coupling: Signals must be paid for and accompanied by verifiable proof, with the cost of brushing scores being linear to weight, and limited by k×Stake upper limit.

* Activity positive feedback: The more active an Agent is, the higher the score of the validators they delegate to, leading to more block production and rewards, which in turn incentivizes more Agents to choose that validator.

* Predictable finality: PoSg layer achieves second-level BFT; every ~10 minutes, the DA root is written into Bitcoin via Taproot, achieving PoW finality.

### 5. Differences from PoW / Traditional PoS

| Dimension | PoW | PoS | PoSg |
| :---- | :---- | :---- | :---- |
| Source of Voting Power | Hash power | Staked tokens | Staked tokens + AI work |
| Work and Security Coupling | High electricity cost | Staking can be idle | Useful AI work converted into security budget |
| Resource Waste | Energy consumption | Low | Low, and incentives for effective computation |
| Anti-Sybil Mechanism | Hash power is hard to forge | Staking threshold | Staking threshold + signal fee + limits |


PoSg combines capital collateralization with AI-Signal through a dual-weight formula: Stake ensures economic resistance to malicious behavior, while SignalScore rewards genuine on-chain activities. It injects AI's "useful work" directly into the consensus layer while maintaining Bitcoin-level economic security, thus forming a positive feedback loop of security—incentives—activity for the B² Network.

## Anchored Rollup / DA Commit / Finality to Bitcoin

The B² Network adopts a "three-layer finality" architecture—B² Rollup is anchored on the B² Hub to achieve second-level BFT finality, after which the B² Hub periodically writes the network's data availability commitments (DA Commit) to Bitcoin Layer1, ensuring that Rollup, sub-chains, and signal events are ultimately protected by Bitcoin's PoW economic security. This path decouples performance from security: high throughput execution at the upper layer, with strong finality guarantees at the lower layer.

| Term | Question | Solution | Level of Finality |
| :---- | :---- | :---- | :---- |
| Anchored Rollup | How to share upper-layer security with a high TPS execution layer? | Submit batch data & state root to B² Hub (PoSg BFT) | Second-level (Hub local finality) |
| DA Commit | How can a large amount of transaction data be recovered and verified by the entire network? | Hub aggregates shard data -> NMT root -> Taproot submits to Bitcoin | Minute-level, retrievable |
| Finality to Bitcoin | How to achieve irreversible economic security? | Bitcoin block confirmation count & PoW cost | Final (PoW determined) |

### Anchored Rollup

Definition: B² Rollup processes transactions in a standalone EVM execution environment, generates state transitions, and produces validity proofs (ZK / Validity), then submits the batch summary (batch commitment) + proof to a specified Namespace in the B² Hub. After the Hub verifies the proof, the batch is included in the PoSg consensus block, providing second-level ordering and irreversible execution guarantees.

Key Attributes

* Sequencer is appointed through Staking via B² Hub voting.

* Gas is priced in BTC (also supporting B2 and whitelisted stablecoins); fees flow to PoSg validators and incentive pools.

* Configurable mandatory inclusion mechanism (anti-censorship): Users can directly send batch data fragments to the Hub DA layer, which Rollup will forcibly extract.

### DA Commit

Goal: Ensure that anyone can recover all original Rollup and Shard transaction data from the minimal commitment on Bitcoin, avoiding "state unproven" and historical reconstruction failures.

Process

1. Each Hub block collects transaction data blocks from various Namespaces (Shard/Rollup).

2. Data is sliced into fixed sizes and encoded (e.g., Reed-Solomon).

3. Construct Namespace Merkle Tree (NMT): Different Namespaces have independent branches for selective downloading.

4. Generate global DA Root (aggregated root).

5. Write into Bitcoin Taproot transaction scripts at fixed intervals (~10 minutes or aligned with Bitcoin block rhythm): DA Root | Epoch ID | Hub Block Range | Proof Hash (optional ZK)

6. After Bitcoin confirmation, any light node can obtain the required shard data and verify integrity using the DA Root.

Data Recovery: If a certain type of node goes offline, as long as more than k fragments survive, reconstruction can be done through erasure coding; the NMT proof ensures that the downloaded data indeed belongs to a certain Namespace.

### Finality to Bitcoin

PoSg & BFT first provide "engineering-level fast confirmation," while Bitcoin provides "economic-level irreversible confirmation."

| Level | Time Scale | Who Guarantees | Reversal Risk | Suggested Use |
| :---- | :---- | :---- | :---- | :---- |
| Local Execution (within Rollup) | Milliseconds to seconds | Sequencer local ordering | High | UI displays transient results |
| Hub Finality (PoSg BFT) | ~2–3 s/block | ≥2/3 VP signatures | Requires PoSg attack | Executable small funds, Agent workflows |
| Bitcoin Finality (DA Commit confirmation) | ~10 minutes + n confirmations | PoW cost | Extremely low (depends on reorganization depth) | Large settlements, cross-chain bridges, institutional reconciliation |

Recommended Practices

* Small or high-frequency calls: rely on Hub Finality.

* Large transfers/settlements: wait for Bitcoin Commit + several confirmations (e.g., 3 to 6 BTC blocks).

### Data & Proof Flow Timing

TODO

Timing Diagram:

1. User Tx -> Rollup Sequencer

2. Batch & state transition -> ZK/Validity Proof

3. Submit -> B² Hub (Namespace=RollupX)

4. PoSg block confirmation (seconds)

5. Hub aggregates multi-Namespace data -> DA Root

6. Taproot Tx written to Bitcoin (≈10min)

7. PoW confirmation = economic confirmation

“Anchored Rollup -> DA Commit -> Finality to Bitcoin” is the main path for the performance and security unification of the B² Network: Rollup obtains instant ordering and execution guarantees on the Hub; the Hub periodically compresses and writes all network data and proofs into Bitcoin, ensuring that all upper-layer states are ultimately safeguarded by PoW. Through multi-layer finality, erasure-coded DA, and verifiable proofs, the B² Network provides a high-throughput, modular, AI-native execution environment without sacrificing Bitcoin's security.

## Economic Units: Stake, Weight, Fee, Reward, Slash

### Stake

Refers to the BTC or B2 locked by users in the B² Rollup staking contract. The principal is frozen until the end of the current Epoch and can be delegated to multiple validators according to shares. Stake serves as both a forfeitable security deposit and the primary factor for calculating PoSg voting rights; its flow is

TODO

Flowchart: User/Miner -> Staking Contract -> (Delegated) Validator -> PoSg Voting Rights -> Stake Unlock or Yield Reinvestment.

### Weight

The fee value specified for each Signal with the transaction, reflecting the economic importance of the event. Weight will be deducted in a one-time charge and:

1. Burned or converted into miner/validator fees, used as a cost to prevent spam;

2. Accumulated to the corresponding validator's SignalScore according to the dual scoring rule of sender + receiver, becoming the second factor of PoSg voting rights.

### Fee

There are three types of fees in the B² Network:

1. Gas Fee: Rollup and Shard transaction execution fees, priced in BTC/B2;

2. Signal Fee = Weight: The necessary cost of Signal transactions, paid by the sender;

3. Network Surcharge: An additional rate that dynamically increases during graylisted node or congestion periods.

All fees collected ultimately accumulate in the validator block reward pool, distributed according to VotingPower.

### Reward

Three types of rewards are generated during the operation of PoSg:

* Block Reward: For each Hub block packaged, Gas + SignalFee is summarized and distributed according to VP;

* Signal Activity Reward: At the end of the Epoch, validators in the SignalScore Top-k can receive an additional 5–10% share;

* External Strategy Earnings: Earnings generated when DeFAI chooses the "Stake to Hub" strategy flow back to Stake holders.

Stakers can choose automatic reinvestment (compound yield) or unlock and withdraw.

### Slash

Economic penalties established for malicious or negligent behavior in PoSg:

* Double signing / Data availability malfeasance: Penalized 5% Stake and corresponding SignalScore reset to zero;

* Continuous offline: Gradually deduct Stake by 0.1–1% based on the number of absences;

* Falsifying signals / Score manipulation: Double confiscation of the sender's payment and downgrade the delegated validator.

50% of the confiscated assets are destroyed, and 50% enter the system insurance pool, used to offset losses or for future incentives.

### Overall Closed Loop

TODO

Flowchart:

Stake provides underlying security -> Weight drives activity and weights Stake -> Fee maintains network operation -> Reward encourages staking and signal production -> Slash punishes wrongdoing and replenishes the insurance pool.

Five types of economic units mutually constrain and circulate, ensuring that the B² Network possesses both economic resistance to attacks and continuous incentives for AI and user participation.

## AI-Driven Intelligent Governance

AI-driven intelligent governance is the "adaptive parameters and risk control" framework of B² Hub: off-chain AI agents—centered on reinforcement learning (RL), supplemented by graph neural network anomaly detection and explainable AI (XAI)—analyze on-chain metrics and node telemetry in real-time, proposing governance suggestions such as PoSg parameter tuning, graylisting, and sharding expansion or contraction; all suggestions are written into the on-chain ParameterOracle contract, which only takes effect after a delay and PoSg VotingPower voting, and is protected by hard thresholds and rollback mechanisms.

Key Components

* RL-Tuner: Simulates PoSg operation in a sandbox, using throughput, rewards, and Slash costs as the reward function, outputting optimal parameters such as α/β, minimum signal fee, and penalty ratio.

* Anomaly Detector: Monitors score manipulation, witching, and voting delay anomalies using GNN + Isolation Forest, generating graylists and confidence levels.

* Shard Balancer: Provides suggestions for creating, expanding, or merging sub-chains based on time series prediction and heuristic algorithms to avoid hotspot congestion.

* XAI-Auditor: Generates reasons and impact Top-K factor summaries (TL;DR) for each AI suggestion, and hashes the report along with the model version for on-chain proof.

Governance Process

1. Data Collection: Nodes periodically publish signed telemetry (TPS, Gas, Slash, delay, etc.); AI components pull for analysis.

2. Suggestion Generation and Explanation: RL-Tuner / Detector / Balancer outputs suggestions -> XAI-Auditor generates explanations.

3. On-Chain Release: Suggestions + explanations are written into ParameterOracle, automatically entering a ≥100 block delay window.

4. Community Review and Voting: PoSg validators approve or reject based on VotingPower; if approved, it takes effect in the next Epoch.

5. Safety Barriers: Hard threshold limits (e.g., α∈[0.5,0.9], Slash≤50% Stake), can quickly roll back to old parameters in case of abnormal increases.

Advantages

* Adaptive: When network load, signal density, or attack situations change, optimal parameters can be provided and deployed within minutes.

* Transparent and Auditable: All model hashes, explanation summaries, and decision processes are stored on-chain; the community can hold accountable, reproduce, and reassess.

* Anti-Manipulation: Suggestions without sufficient explanation or with confidence below the threshold will be automatically rejected, and proposals exceeding hard threshold ranges require a supermajority governance proposal.

* Reduced Operational Costs: Traditional "quarterly manual parameter tuning" is shortened to "daily micro-adjustments," while avoiding human subjectivity or delays.

Through this framework, B² Hub can introduce AI's learning and predictive capabilities while maintaining verifiable consensus rules, achieving faster risk response, more precise resource scheduling, and higher economic efficiency.

# Mining Squared: Revenue-Oriented BTC Mining Pool and Network Economic Entry

## Motivation

The vast majority of BTC produced daily by Bitcoin miners is passively hoarded or cashed out through exchanges, creating a near disconnection with the emerging Layer 2 and AI economies, resulting in a disconnect between hash power contribution and ecological activity:

* Revenue dispersion—miners need to manually transfer BTC into staking or DeFi scenarios; on-chain revenue opportunities are lost in multiple transfers and high fees.

* High staking threshold—individual small and medium miners find it difficult to accumulate enough stake to influence PoSg, and it is also challenging to track optimal delegation nodes in real-time.

* Insufficient security spillover—the economic costs generated by PoW only secure Layer 1, while the consensus layer and application layer still lack additional BTC liquidity and incentives.

Mining Squared connects the mining pool accounting system through smart contracts, streamlining "Hashrate -> Mining Rewards -> Smart Routing":

1. Real-time revenue capture: Each time the mining pool finds a new block, the corresponding BTC is precisely credited to the Mining Squared revenue pool.

2. Strategy routing: The revenue pool automatically executes multi-strategy allocation according to preset ratios—directly converted into PoSg staking shares, injected into DeFAI strategy combinations, or periodically returned to miners' wallets.

3. Delegation automation: Contracts dynamically adjust delegated validators based on yield rates, slash risks, and miner preferences, ensuring maximization of staking rewards without human intervention.

In this way, miners' hash power not only earns PoW block rewards but also automatically converts into PoSg voting rights and network fee sharing; BTC liquidity flows into Hub and Rollup, providing fuel for AI and DeFi scenarios, further enhancing chain-level security and application activity, ultimately forming a positive cycle of "Hash Power -> Revenue -> Staking/Strategy -> More Revenue."

## Architecture

Mining Squared consists of two parts: off-chain mining pool nodes and on-chain contract clusters, with the core process divided into five modules.

1. Mining Ledger

    * Each time the mining pool discovers a new block, the node generates a "revenue certificate" in the local ledger and broadcasts it to the RewardCollector contract.

    * The certificate includes block height, amount of BTC produced, and share of participating hash power; miners can use their private keys to sign and prove hash power ownership.

2. RewardCollector Contract

    * After aggregating and verifying the mining pool signatures, it transfers the BTC to a unified contract custody address.

    * It mints 1:1 rBTC tokens (ERC-20 on Rollup) based on miners' hash power shares, serving as the accounting unit for subsequent revenue routing and redemption.

3. BTC Revenue Router

    * Supports programmable allocation formulas, initial template:

      ```
      ρ1 = x% -> StakingAdapter // PoSg Staking

      ρ2 = y% -> DeFAI Controller // External Strategies

      ρ3 = z% -> Direct Payout // Return to Miners

      ρ1+ρ2+ρ3 = 100%
      ```

    * Miners can adjust their personal ρ parameters using a front-end slider; the Router automatically executes corresponding transfers in each settlement period.

4. DeFAI Controller

    * Aggregates multiple strategy agents (lending mining, liquidity provision, staking derivatives, cross-chain arbitrage, etc.).

    * Uses rBTC as the underlying asset, dynamically allocating to the strategy pool with the highest yield, automatically rebalancing based on block frequency.

    * When the annualized yield of B² Hub staking exceeds the external strategy threshold, the Controller automatically increases the weight of ρ1, directing more rBTC to the StakingAdapter.

5. StakingAdapter & Validator Delegation

    * Unpacks incoming rBTC into BTC and submits it to the B² Hub Staking Module.

    * Runs delegation algorithms:

    * Basic mode: evenly distributed to the top N high-reputation validators;

    * Advanced mode: weighted distribution based on PoSg reward rates, slash risks, and miner preferences.

    * The re-staked BTC, after earning PoSg rewards, automatically rolls into the Router for the next period's allocation.

Information and fund flow:

![][image]

Programmability

* The Router, Controller, and Adapter all have open strategy interfaces, allowing miners or DAOs to upload new strategy scripts and set thresholds.

* Parameter changes take effect in real-time through on-chain governance or personal preferences, ensuring that the revenue path continuously aligns with the interests of miners and the network as a whole.

This architecture allows the BTC produced by miners to enter on-chain contracts in seconds, and automatically, transparently, and programmably cycles between "PoSg Staking—DeFi Strategies—Direct Return," while seamlessly converting hash power revenue into the security budget and ecological liquidity entry of the B² network.

## Automated Revenue Path

Mining Squared has designed a full-chain revenue channel for miners that follows the path of "Mining -> Tokenization -> Strategy Routing -> Compound Return Flow," requiring no manual operation throughout the process, which is specifically divided into five cyclical steps:

1. Mining Output -> Tokenization

    * After the mining pool discovers a new block, the earned BTC is immediately injected into RewardCollector.

    * The contract mints an equivalent amount of rBTC tokens (Rollup-side ERC-20) based on the hash power share, recording the principal and future earnings due to each miner.

2. Revenue Routing Split

    * Miners set a one-time weight ρ = ⟨Staking ρ₁, Strategy ρ₂, Return ρ₃⟩ for rBTC on the front end.

    * The Router executes in batches every 30 minutes:

    * ρ₁ -> StakingAdapter: Converts to native BTC and stakes it to B² Hub;

    * ρ₂ -> DeFAI Controller: Invests in multi-strategy revenue pools;

    * ρ₃ -> Directly transfers back to miner A-AA wallet, which can be withdrawn at any time.

3. Dynamic Strategy Scheduling

    * DeFAI Controller interfaces with sub-strategies such as market making, lending, LSD, and cross-chain arbitrage.

    * Each strategy Agent continuously reports APY, risk, and liquidity; the Controller automatically adjusts positions based on revenue-risk scoring.

    * Once it detects that PoSg annualized > average APY of DeFi pools + Δ, the Controller automatically migrates part of the funds from external pools to StakingAdapter to increase the staking proportion.

4. PoSg Rewards & DeFi Mining Earnings

    * Staking BTC earns block fees, signal rewards, and other PoSg earnings;

    * Interest and incentive tokens generated by external strategies are automatically converted back to rBTC via the Router;

    * Both types of earnings are redistributed according to the miner's initial ρ configuration, with an optional "automatic reinvestment" switch to enter the next round of splitting.

5. Compound Return Flow and Dynamic Rebalancing

    * The Router adds the earnings from the previous round to the miner's rBTC balance, reinvesting it into Step 2.

    * Miners can adjust the ρ weights or withdraw rBTC at any time on the front end; all changes take effect in the next cycle, achieving a rolling compound interest of "earnings-reinvestment-delegation."

Result: The BTC generated from a single block enters on-chain staking or strategy pools within minutes, with earnings rolling in real-time; miners enjoy the certain income from PoW mining while automatically compounding PoSg and DeFi returns, truly creating a closed loop of hash power -> staking/strategy -> compound earnings -> hash power.

## Risk and Incentive Model

### Main Risks

1. Price Volatility Risk

    The market price fluctuations of BTC and B2 may lead to unrealized losses in staking positions, affecting the mindset of stakers.

    Mitigation Plan:

    * The Router allows users to customize the return ratio ρ₃ to retain some spot assets;

    * DeFAI provides hedging strategies (such as short BTC futures) for automatic configuration.

2. Strategy Risk (DeFAI Pool)

    High-yield DeFi pools may have contract vulnerabilities, liquidation, or liquidity exhaustion.

    Mitigation Plan:

    * The Controller sets a risk score cap for all strategies, automatically rebalancing if the threshold is exceeded;

    * Initially, only blue-chip protocols with multiple rounds of audits and TVL ≥ 5,000 BTC will be enabled;

    * Extreme events trigger a "safety mode," automatically returning funds to the StakingAdapter.

3. Consensus Penalty Risk (Slash)

    Delegating to malicious or unstable validators may result in slashed stakes.

    Mitigation Plan:

    * The default delegation algorithm of the StakingAdapter prioritizes nodes with low Slash history and high online rates;

    * Users can exclude blacklisted validators;

    * Slash losses can be partially compensated from the insurance pool, which is sourced from the system's 50% penalty redistribution.

4. Contract and Bridging Risks

    Router, RewardCollector, and StakingAdapter are all key contracts; asset conversion between Rollup and Hub also relies on bridging logic.

    Mitigation Plan:

    * Multiple audits + bounty programs;

    * Contracts use time-lock upgrades, with emergency vulnerabilities triggering pause();

    * Bridging only occurs on paths protected by PoSg + Taproot dual finality.

5. Centralized Computing Power and Governance Attacks

    A few large miners may monopolize staking and voting rights.

    Mitigation Plan:

    * Staking weight is capped at a maximum binding limit for a single mining pool (e.g., 25% Hard Cap);

    * Multi-armed bandit delegation dispersion algorithm splits automatic staking across ≥N validators.

### Incentive Design

| Participant | Revenue Items | Incentive Logic |
| :---- | :---- | :---- |
| Miners / Stakers | 1) PoW block rewards 2) PoSg block fees + signal rewards 3) DeFAI strategy APY 4) Insurance pool dividends | All revenue is mapped to rBTC balance; automatic reinvestment can be enabled for compound interest, or liquidity can be redeemed at any time. |
| Validators | 1) Basic Stake returns 2) SignalScore activity bonus 3) Slash reward sharing | Serve more high-quality Signal agents -> receive higher VP and additional prize pools; if slashed, 50% goes to the insurance pool, indirectly benefiting compliant validators. |
| Strategy Providers (DeFAI Agents) | Management fees + performance fees (20/2 typical) | Net worth outperforming the benchmark PoSg APR can receive more fund allocation; if strategy APY lags long-term, automatic downgrading occurs. |
| Insurance Pool Participants | Slash penalties, a portion of unclaimed earnings | Acts as a passive risk cushion, which can be converted into governance voting rights or stable income tokens in the future. |

### Game Theory and Steady State

* When PoSg APR > DeFi APR, the "staking -> rewards" path dominates, and the Controller will migrate funds back to the Hub to enhance network security; conversely, it will increase DeFi allocation to improve overall miner returns.

* Slash costs are shared by malicious validators and the insurance pool, encouraging miners to diversify their delegation and avoid crowding a single node.

* A macro three-layer self-balancing system is formed: computing power output -> multi-strategy returns -> network security enhancement -> higher APR -> new computing power entry, making Mining Squared an automated gain engine connecting PoW and PoSg, on-chain and off-chain returns.

## Integration with DSN-AI / Agent Wallet

1. Native Earnings Enter A-AA Wallet

    The rBTC tokens minted by Mining Squared comply with A-AA interface specifications, allowing miners or computing power providers to designate any agent address as the earnings recipient.

    * Once the earnings are credited, the agent can use rBTC for task gas, model calls, or re-staking without cross-chain conversion.

    * The A-AA permission module supports two strategies: "automatic reinvestment of earnings" and "threshold alert withdrawal," which miners can configure with one click on the front end.

2. Signal-Triggered Automatic Staking

    Agents can subscribe to their own "balance change" signals:

    * When rBTC balance ≥ preset threshold, trigger autoStake(rBTC, validatorList);

    * Successful staking will generate a new StakeUpdate Signal, instantly enhancing the SignalScore of the delegated validator, forming a "earnings -> signal -> consensus weight" closed loop.

3. DeFAI Strategy Executed by Agent

    The underlying DeFAI Controller consists of a group of strategy agents holding A-AA accounts:

    * They publish "strategy APY updates" and "position migration" signals via the Signal Bus for miners' wallets or other agents to subscribe for reference;

    * The control logic is fully auditable on-chain, with earnings and risks transparent to all Agents.

4. Cross-Chain/Cross-Application Calls

    Since rBTC = ERC-20 on Rollup, Agents can:

    * Directly call AMM/DeFi contracts (such as DEX, lending) for recombination;

    * Map rBTC to other Shards or external chains via IBC-lite, serving as fuel for more AI/DeFi scenarios.

5. Integration of Security and Risk Control

    * A-AA supports limit + time lock modules to prevent malicious strategies from depleting earnings;

    * All signals generated by Mining Squared (earnings credited, staking, redemption, strategy changes) will enter the DSN-AI Graph, available for any monitoring Agent to subscribe for on-chain risk control and auditing.

Computing power earnings enter the Agent wallet through Mining Squared, and the Agent can use these funds for automatic staking, executing DeFi strategies, or paying AI task fees; the entire process is signal-driven and programmable on-chain, ultimately seamlessly injecting BTC traffic generated by PoW into the DSN-AI agent ecosystem, forming a triple loop of funds, signals, and security.

# B² Hub: The Bridge Connecting Bitcoin and AI

B² Hub is the heart of the entire network and serves as the "cross-dimensional bridge" between the Bitcoin world and the Agentic AI economy.

At the base level, it anchors each round of data availability commitments to Bitcoin Layer 1 through Taproot transactions, inheriting the economic certainty of PoW; at the upper level, it tightly couples BTC staking with AI Signal using PoSg consensus, allowing the "useful work" of agents to be directly converted into chain-level security budgets. Meanwhile, Application Sharding enables multiple execution environments to run in parallel on the same validator set without competing for bandwidth; second-level BFT block production provides real-time feedback for high-frequency AI scheduling, while the data ultimately resides in Bitcoin's immutable ledger. To allow the system to adapt to load, the Hub also introduces reinforcement learning-driven intelligent governance: consensus parameters, fees, and graylists are suggested by AI agents and then implemented through on-chain guardrails and community voting. Through this bridge, BTC liquidity can be seamlessly injected into AI wallets, and AI Signals can feed back into network security, forming a positive cycle of "value—computing power—security—activity." The following chapters will break down the technical details of PoSg consensus, Application Sharding, data availability anchoring, and AI intelligent governance.

## Design Vision and Role Positioning

### Vision

B² Hub aims to become the convergence point of Bitcoin value and artificial intelligence productivity, providing a layer for execution and settlement that enjoys the finality of PoW while having second-level responsiveness for billions of AI agents worldwide. Its goals can be broken down into three slogans:

1. Make BTC the fuel for AI—All fees and rewards are priced in BTC/B2, eliminating cross-chain friction;

2. Let AI work feed back into chain security—PoSg converts paid Signals into validator voting rights, with the security budget growing in sync with AI activity;

3. Enable adaptive development and governance—With Application Sharding and AI intelligent governance frameworks, the network can scale on demand and automatically adjust parameters while maintaining continuous evolution without sacrificing verifiability.

### Core Roles

| Role | Responsibilities | Key Incentives |
| :---- | :---- | :---- |
| Validator | Stake BTC/B2, run CometBFT, package multiple Shard blocks | Block fees + signal rewards; malicious behavior is slashed |
| AI Agent | Send/receive Signals, execute on-chain/off-chain tasks, manage A-AA wallets | Earn BTC by completing tasks; their Signals enhance delegated validator weight |
| Miner / Mining Squared | Automatically route PoW earnings to staking or DeFAI strategies | Base mining rewards + PoSg/DeFi compound earnings |
| Rollup Sequencer / dApp Developer | Execute contracts at high frequency within Shard or Rollup, generate batches | High TPS, low latency environment; fees settled directly in BTC |
| Light Node / End User | Only sync Hub headers and NMT Root, can verify transactions of interest in Shards | Mobile second-level confirmations; no need for full chain storage, lowering barriers |

Positioning

* Layer 1.5: Positioned above Bitcoin L1 and various Rollups, balancing PoW finality with high performance.

* Secure Consensus: Merging Stake and Signal with PoSg; the more useful AI work, the stronger the underlying security.

* Modular Execution: Supporting coexistence of multiple VMs and data forms through Application Sharding; Rollups, Oracles, and AI Services can run in parallel.

* Self-Driving Governance: Reinforcement learning automatically provides fee and parameter tuning, XAI outputs interpretable reports, and on-chain guardrails and voting ensure transparency and prudence.

With this design, B² Hub is not only a "bridge" in technology but also a "bridge" in economics and incentives: weaving Bitcoin's absolute scarcity with AI's infinite creativity into a single value cycle, providing a solid yet flexible foundation for the next generation of machine economy.

## System Layering and Data Flow Overview

### Layered Architecture

1. P2P Network Layer

    Uses libp2p/gossip-sub for node discovery, block headers, transaction, and signal event propagation, with underlying channels reused for all Shards and Rollups.

2. Consensus Layer (CometBFT + PoSg)

    CometBFT provides a Propose-Prevote-Precommit three-step BFT process, with block intervals of 2 seconds or 12 seconds; the PoSg weight engine snapshots Stake and SignalScore at each Epoch to calculate Voting Power for validators and drive the next election.

3. Execution Layer (Application Sharding)

    Namespace Router routes transactions to the corresponding Shard's ABCI application based on namespace_id:

    * Execution Shard: EVM / Move / WASM dApp

    * Data Shard: AI training data, file storage

    * Service Shard: Oracle, VRF, Signal dedicated Shard



4. Data Availability Layer (Chunk + NMT)

    All Shard data slices are written into the Namespace Merkle Tree after erasure coding. Every ≈ 10 minutes, the NMT root is aggregated with threshold signatures to generate a DA Commit, which is anchored to Bitcoin L1 through Taproot transactions.

5. AI Governance Layer

    Off-chain RL-Tuner, GNN Detector, and XAI-Auditor periodically submit parameter tuning and risk suggestions to the on-chain ParameterOracle; all changes must be written into the consensus state after a delay window and PoSg voting.

6. Interface Layer

    Provides WebSocket events, gRPC/RPC queries, and IBC-lite cross-chain messages; light nodes only need to synchronize block headers and the Namespace proofs of interest to verify the state.

### Three Core Data Flows

1. BTC Value Flow

    TODO Value Flow Diagram

    Mining rewards -> Mining Squared tokenization -> Router automatic allocation

    -> (a) Staked to StakingModule to enhance validator VP

    -> (b) Invested in DeFAI strategies to earn external returns

    -> (c) Directly returned to miners/Agents as Gas

    Block rewards and strategy earnings flow back again, forming a compound interest cycle.

2. Signal Flow

    Agents submit submitSignal() through Signal Shard -> CheckTx immediately soft confirms and broadcasts signal.softCommit;

    Proposers package the current round Signal into BatchSignalTx during block production -> Validators delegated by sender and receiver synchronously increase SignalScore -> Affects the next Epoch Voting Power.

3. Proof/Data Flow

    Rollup or Shard transactions -> NMT slices -> Enter Hub header with the block to achieve second-level BFT finality;

    Hub generates DA Root + threshold signature every 10 minutes -> Written into Bitcoin Taproot -> All states achieve PoW economic finality at the minute level.

Through the above layers and three data flows, B² Hub weaves the finality and security collateral (Stake) of Bitcoin with the real-time production factors (Signal) of AI into the same economic and technical stack:

BTC is continuously injected from the bottom, Signal is consumed at the millisecond level and instantaneously fed back to consensus security, while all data and states are ultimately sealed into Bitcoin, making them immutable. This structure makes the Hub inherently adaptable to high-frequency AI scheduling while maintaining the same level of finality reliability as Bitcoin.

## PoSg Consensus Layer

PoSg (Proof of Signal + Stake) is B² Hub's original proprietary consensus mechanism, driven by a dual engine of Stake and Signal. It introduces payable and verifiable AI Signal as a second-dimensional weight on the basis of traditional staking security (PoS), merging capital collateral with real work into a secure crankshaft:

[![][image]]

Where Stake comes from staked BTC/B2 and can be slashed; SignalScore is the weighted sum of all signals sent/received by agents delegated to validator v within the last M epochs. α and β are dynamically adjusted by on-chain governance (default 0.7/0.3). Therefore—staking increases the cost of malicious behavior, while signals directly convert on-chain activity into a security budget.

Key Components

| Module | Responsibility | Highlights |
| :---- | :---- | :---- |
| StakeMap | Records BTC/B2 staking and delegation relationships | Multiple delegation, liquid shares, delayed unlocking |
| SignalPool | Caches all validated Signals within the current Epoch | Soft confirmation enters Pool, archived after hard block |
| ScoreAccounter | Settles SignalScore -> Writes to Validator metadata | Dual scoring for sender & receiver, window rolling |
| PoSg Engine | Calculates VotingPower, selects the next round validator set | α/β and window length can be governed and modified |
| SlashGuard | Monitors double signing, offline, forged signals, etc. | Penalizes Stake + resets SignalScore |

Workflow (Epoch Level)

TODO Flowchart

1. Snapshot

    Freeze the current Stake and SignalPool, write to the Epoch Header.

2. Validator Set Selection

    Select the top N based on VP; if the difference between this set and the last one is greater than Δ, trigger DKG to generate a new threshold public key.

3. CometBFT Block Production

    Adopt weighted round-robin proposal; block interval can be configured to 2 s or 12 s; Signal Tx is soft-executed in CheckTx and batch settled in DeliverTx.

4. Settlement & Slash

    Block fees + Signal rewards are distributed according to VP; double signing and malicious nodes on the graylist are immediately penalized.

5. Rolling

    At the end of the Epoch, the window slides; a new Snapshot starts the cycle again.

Security and Performance Features

* Economic security dual insurance. Stake can be slashed, and Signal requires payment; attackers must lock slashing collateral to gain points.

* Second-level soft confirmation. Signal transactions return softCommit events within 200–500 ms, meeting the real-time requirements of AI microservices; finality is protected by BFT in 2/12 s.

* Dynamic adaptation. RL-Tuner automatically adjusts α/β, minimum Signal fee rate, and Slash coefficient based on chain load and Slash events; all changes are implemented through delayed voting.

* Anti-centralization design. SignalScore ≤ k × Stake (k≈3) prevents zero-stake point farming; delegation can be distributed among multiple validators to reduce the risk of monopolization by large holders.

* Light client friendly. Block headers embed aggregated threshold signatures; light nodes only need to verify signatures and NMT proofs to confirm any Shard state.

In summary: PoSg merges "slashed funds" and "paid funds" into the same voting power, maintaining the economic resistance to malicious behavior of the staking system while making the real work of AI a direct fuel for enhancing chain security and validator rewards, establishing the shortest path between second-level experiences and minute-level PoW finality. The following subsections will elaborate on the state machine structure, signal batch settlement algorithm, reward/slashing rules, and how AI intelligent governance seamlessly adjusts these parameters.

### CometBFT Overview and Adaptation

Why Choose CometBFT

CometBFT (formerly Tendermint Core) is one of the most mature BFT consensus engines in the industry, featuring instant finality, ABCI application layering, and cross-language easy embedding. It allows us to encapsulate the staking logic of PoSg, Signal batch settlement, and Application Sharding within the ABCI application layer without modifying the underlying network and voting protocol, thus reusing its stable network stack and multi-language ecosystem.

Consensus Process Overview

* Block interval: 2 s block production timeout; governance can switch on-chain.

* Instant finality: Finalize after ≥ 2/3 VotingPower completes Precommit, with no probability of reorganization.

PoSg Custom Adaptation

| CometBFT Integration | Our Extension | Description |
| :---- | :---- | :---- |
| CheckTx | 1. Verify Signal Tx signature, fees, Proof 2. applySoft(softState, tx) writes to soft state cache 3. EmitEvent("signal.softCommit") | Signal receives soft confirmation immediately in the mempool stage, pushed to Agent within 200–500 ms. |
| PrepareProposal | 1. Extract pending Signal from softState within Δt interval 2. Sort by (timestamp, id) -> encapsulate BatchSignalTx 3. Write to proposal block; empty blocks can still contain batches | Ensures deterministic ordering across the network, preventing proposer malfeasance or partial ordering. |
| ProcessProposal | Full nodes replay BatchSignalTx, calling applyHard(appState, list); if inconsistent with soft state, reject the proposal. | Maintains soft/hard state consistency, preventing double spending. |
| FinalizeBlock | 1. Aggregate validator BLS / Schnorr signatures (threshold Schnorr via FROST) 2. BlockHeader adds taprootCommit field for DA layer use | Light clients only need to verify a single threshold signature. |

Priority mempool

```
Priority(tx) =    2  if tx.isSignal
               1.01  if tx.isGasBidHigh
               1.00  default
```

Signal Tx highest priority, ensuring soft confirmation can still occur promptly during network congestion. Batches are uniformly collected during the block finalization phase to avoid header bloat.

Threshold Signatures & Light Nodes

* Each round Epoch validators generate Schnorr public key PK_epoch through FROST-DKG;

* BlockHeader saves aggSig; light clients only verify Verify(PK_epoch, aggSig, blockHash), without needing to traverse individual signatures;

* Epoch handover blocks contain re-aggregated signatures of the previous Epoch root, ensuring verifiable key rotation.

Data Availability Anchoring Pipeline

![][image]

CometBFT's event system broadcasts DA root, threshold signatures, and block height to DA Workers, which periodically aggregate and write to Bitcoin Taproot.

Security and Failover

* Greylist validators: After the GNN detector marks suspicious nodes, the PoSg Engine temporarily removes their voting rights; CometBFT can still finalize with automatic downscaling.

* Long fork detection: If a Hub light client finds a Header inconsistent with Bitcoin submissions, it triggers a network-wide Slash; CometBFT nodes automatically reject malicious branches by comparing taprootCommit.

Through minimally invasive customization, we treat CometBFT as a "high-speed voting machine," injecting PoSg's Stake/Signal weight, Signal soft confirmation and Batch finalization, threshold signatures, and DA Root commitments at the ABCI hook layer; maintaining second-level finality and a mature network stack while laying a solid foundation for subsequent Bitcoin anchoring, Application Sharding, and AI intelligent governance.

### Core State and Data Structures

The state machine of PoSg is based on KV-Store + prefix tree, with each prefix corresponding to a type of object; during snapshots, a simple (key, value, version) list is exported, which can be used by light nodes to reconstruct the Merkle root. The table below lists the most important key spaces and structures (Go-pseudo).

| Prefix | Structure / Description | Read/Write Path |
| :---- | :---- | :---- |
| B2S/ | StakeEntry: Single stake share | StakingModule |
| B2D/ | DelegationEntry: Agent -> Validator mapping | AgentRegistry.delegate() |
| B2A/ | AgentMeta: A-AA public key, delegation, version | registerAgent / upgrade / recover |
| B2G/ | SignalObj: Full signal after block finalization | DeliverTx(BatchSignalTx) |
| B2P/ | SoftSig cache (TTL) | CheckTx() |
| B2V/ | ValidatorMeta: Stake, SignalScore, accumulated rewards, greylist flag | EpochTransition |
| B2E/ | EpochInfo: Window pointer, α/β, threshold public key | Updated at the end of each Epoch |
| B2C/ | ChainParam: Hard thresholds, window M, k value, and other constants | Governance modification only |

1. Stake and Delegation

    ```go
      type StakeEntry struct {
          Amount      uint64    // sat/b2
          UnlockEpoch uint32    // 0 = still locked
      }

      type DelegationEntry struct {
          Validator   addr
          Percent     uint16    // 千分比，支持多委托
      }
    ```

    * Pledged shares are split by the pledger's address + nonce for easier partial unlocking.

    * Multiple delegations are expressed through multiple D/<agent> records, with the total percentage = 1000.

2. Agent and Signal

    Here’s a polished version of the provided text:

    ```go
    type AgentMeta struct {
        PubkeyRoot [32]byte // Multi-signature root
        DelegateSet []addr   // Current set of delegated validators
        Version     uint32
    }
    ```

    ```go
    type SignalObj struct {
        Sender    addr
        Receivers []addr
        Weight    uint64
        BlockTime int64
        Id        [32]byte
    }
    ```

    - After a SignalObj is finalized, only the essential fields are retained; the payload is handled internally within the shard.
    - SoftSig caches only the Id and Sender, with a TTL of one block; it is cleared upon block finalization.

3. Validator State

    ```go
    type ValidatorMeta struct {
        Pubkey        []byte // CometBFT ed25519 or BLS12 public key
        StakeSum      uint64
        SignalScore   uint64
        VotingPower   uint64 // α·Stake + β·SignalScore (scaled)
        RewardAccrued uint64
        GrayFlag      bool
        LastSlashEpoch uint32
    }
    ```

    - VotingPower is updated and synchronized with the CometBFT UpdateValidator API.
    - The GrayFlag is marked by the AI Detector; nodes on the graylist do not incur penalties on their stake, but their Voting Power is set to zero.

4. Epoch & Global Parameters

    ```go
    type EpochInfo struct {
        EpochNum    uint32
        WindowPtr   uint16 // Points to the circular SignalRing
        AlphaBeta   [2]uint16 // Scaled α/β values (multiplied by 10000)
        ThresholdPK []byte // FROST Schnorr aggregate key
        DA_RootPrev [32]byte
    }

    type ChainParam struct {
        WindowSize         uint16 // M
        MinSignalFee      uint64
        MaxWeight         uint64
        StakeToScoreRatio uint8  // k
        HardSlashRatio    uint16 // ‱
    }
    ```

    The WindowPtr maintains the SignalScore in a circular queue: `SignalRing[WindowPtr]` stores the scores of validators for the current epoch. During epoch rotation, the oldest slot is overwritten, allowing for O(1) window movement through addition and subtraction.


5. Merkle Combination Root Layout

    ```
    StateRoot = MH(

    MH("B2S/"+*), // Stake Trie

    MH("B2A/"+*), // Agents

    MH("B2V/"+*), // Validators

    MH("B2D/"+*), // Delegations

    MH("B2G/"+epochPtr), // Current Window Signal Sub Trie

    MH(other shards ...)

    )
    ```

    * Each namespace is separately hashed with Merkle, then concatenated for easier synchronization of specific object types.

    * Light nodes that only care about balances can download the "B2S/" sub Trie and verify the parent root.

6. Memory Cache and Asynchronous Disk Writes

    * SoftSigCache: LRU+TTL map, written during CheckTx; read during PrepareProposal to generate Batch.

    * SignalRing: a circular array of map[ValidatorID]uint64; at the end of the Epoch, the current slot is written to the DB, then the pointer ++ mod M.

    * RocksDB / LevelDB backend enables column families to reduce write amplification.

This state layout follows three principles:

* Parallelizable and partitionable—Stake, Signal, and Shard are independent and can be synchronized as needed;

* Window O(1) rotation—SignalScore moving window does not require full chain scanning;

* Soft/hard state separation—soft confirmations are only in memory, and any data not included in blocks is automatically cleared after 1-2 blocks.

With these structures, the PoSg engine only needs to incrementally update VotingPower and write an EpochInfo to complete snapshots each Epoch, significantly reducing I/O and storage costs, while providing clear verifiable synchronization boundaries for light clients and archival nodes.

### Signal Soft Confirmation & Batch Settlement Mechanism

Goal: Balance millisecond-level user experience with global consistency

* Soft Confirmation (Soft-Commit): Signal Tx is executed locally and events are broadcast immediately after entering CheckTx, providing AI Agents with second-level feedback.

* Hard Settlement (Hard-Commit): Each block generation cycle, the proposer packages soft confirmation signals within the same time window into 1 – N BatchSignalTx written to the block, guaranteed irreversible by PoSg + BFT.

A. Temporal Overview (Δ = blockTime = 2 s / 12 s)

B. Core Process

| Step | Processing Point | Logic |
| :---- | :---- | :---- |
| 1 | CheckTx | 1. Parse Tx -> Verify signature / fees / Proof 2. Deduplication: If id is already in SoftCache or has been committed, reject 3. applySoft(SoftCache, tx) —— Update temporary score 4. EmitEvent("signal.softCommit", id, sender, weight) |
| 2 | PrepareProposal (proposer) | 1. Retrieve Signals from cache with timestamp ∈ [lastCommit, now] 2. Stably sort by (timestamp, id) 3. Assemble BatchSignalTx{signals[]} in shards; support multiple batches 4. Append other ordinary Tx afterwards |
| 3 | ProcessProposal / DeliverTx | 1. Full nodes unpack Batch 2. Verify nonce and weight limits for each signal 3. applyHard(StateDB, signal): a. Write to G/ Sub Trie; b. Delegate validators for sender/receiver each +weight 4. Mark corresponding SoftCache entry as “final” |
| 4 | FinalizeBlock | Generate threshold Schnorr aggregate signature, block achieves BFT finality; upper layer applications can treat signal.hard=true as a business termination condition |
| 5 | Cleanup | Clear already committed items in SoftCache after Commit; expired (TTL = 1 block) uncommitted signals re-enter the next round of candidates |

C. BatchSignalTx Data Format (RLP / Protobuf)

| Field | Type | Description |
| :---- | :---- | :---- |
| count | uint16 | Number of Signals in this batch |
| signals | []SignalLite | Simplified structure (no payload) |
| merkleRoot | bytes32 | Merkle root of all id‖weight leaves, for proof |

```go
SignalLite {
  id bytes32
  sender address
  receivers []address
  weight uint64
  ts uint32 // seconds
}
```

Merkle root ensures batch replay consistency; if proposer forges order, block will be rejected if root differs during Precommit phase.

D. Fees and Garbage Control

* minSignalFee: AI governance can dynamically increase; soft confirmation must also deduct fees first.

* weight ≤ MAX_WEIGHT: Prevent large single score inflation; exceeding must be split into multiple transactions.

* Graylisted nodes incur additional grayMultiplier × minSignalFee.

Fees are locked during soft confirmation; if not ultimately committed (TTL timeout), 90% is automatically refunded, and 10% is destroyed.

E. Conflict and Rollback Handling

| Scenario | Result | Event |
| :---- | :---- | :---- |
| Multiple submissions with the same id | First soft confirmation successful, others Duplicate | signal.duplicate |
| Soft state passes but hard state fails (nonce, balance, etc.) | signal.revert, Agent can resend after perception | Soft state score deducted from cache |
| Proposer ignores signals | Automatically enters next round proposer queue after TTL; ignoring 3 times consecutively will result in Slash | |

F. Security Summary

* Soft confirmation is not final: If Agent's business requires economic assurance -> wait for hard block; large settlements -> wait for Bitcoin Anchoring.

* Economic resistance to malicious behavior: Sender pays + weight limits + k×Stake cap, score inflation cost increases linearly.

* Slash conditions: Tampering with Batch, repeated omissions, and fraudulent replays can all submit BatchFraudProof to trigger penalties.

The soft confirmation / batch accounting mechanism allows B² Hub to provide sub-second feedback for AI Agents without sacrificing BFT-level consistency and Bitcoin-level economic finality—harmonizing real-time performance, throughput, and security within the same protocol stack.

### Voting Power Calculation and Validator Update

PoSg reassesses validator weights for each Epoch and synchronizes the results to CometBFT. This process consists of three steps: Collection -> Normalization -> Output.

1. Weight Collection

| Symbol | Meaning | Measurement Source |
| :---- | :---- | :---- |
| S_v | Staked Amount (StakeSum) | StakeMap: Total BTC/B2 delegated to validator v |
| Q_v | Signal Score (SignalScore) | SignalRing[WindowPtr]: Cumulative weight within window M |
| F_v | Graylist Flag | ValidatorMeta.GrayFlag, written by AI detector |

2. Normalization and Mixing Formula

    1. Scaling

    * Staking: $\hat S_v = \frac{S_v}{\sum S}$

    * Signal: $\hat Q_v = \frac{Q_v}{\sum Q}$

    2. Upper Limit Constraint

    $$\hat Q_v \le k \cdot \hat S_v \quad\text{(k = StakeToScoreRatio 3)}$$

    3. Graylist Penalty

    $$\hat S_v = 0,\;\hat Q_v = 0 \quad F_v = \text{true}$$

    4. Mixed Weight

    $$VP_v = \alpha \cdot \hat S_v + \beta \cdot \hat Q_v \qquad (\alpha + \beta = 1,\; \alpha,\beta \in [0,1])$$

    5. Minimum Weight Filtering

    If $VP_v < VP_\text{min}$ (governance parameter, default 0.001), the validator is considered a backup and does not participate in block production for this Epoch.

3. Validator Set Selection Algorithm

    ```
    input: VP map, TargetSize N

    list = sort_desc(VP) // Weight in descending order

    set = list.take(N) // Take top N

    if Σ VP(set) < 0.67 // Ensure ≥2/3 weight is online

    expand set until Σ VP ≥ 0.67

    return set
    ```

    * N defaults to 64, adjustable by governance;

    * If weight concentration occurs (whale validators), expansion ensures ≥2/3 VP is online;

    * Automatically triggers governance proposal reminders after exceeding 100.

4. Write to CometBFT

    1. UpdateValidator

    * Hub ABCI calls CometBFT's ValidatorUpdates, submitting <pubkey, VP_scaled>;

    * VP_scaled = uint64(VP * 1e12) to retain 12 decimal precision.

    2. Threshold Public Key Rotation

    * Trigger FROST-DKG when the difference between the new and old sets is ≥ ⅓;

    * Generate new ThresholdPK and write to EpochInfo; light nodes can verify the new aggregated signature by syncing.

5. Epoch Rotation Timeline (Example 12 s block, 1 h Epoch)

    ![][image]

6. Parameter Governance and AI Tuning

    | Parameter | Default Value | Adjustment Method | AI Self-Tuning Range |
    | :---- | :---- | :---- | :---- |
    | α / β | 0.7 / 0.3 | DAO Voting | RL-Tuner fine-tunes within ±0.1 |
    | $VP_\text{min}$ | 0.1 % | Governance | Automatically scales linearly with the number of validators |
    | k (StakeToScore) | 3 | Governance | Can be temporarily reduced to 2 after GNN detects abnormal scoring |
    | Window M | 24 h | Governance | Can slide between 6–48 h based on chain load |

    Delay Barrier: All parameter changes take effect after ≥ 100 Hub blocks (≈20 min); if XAI gives a "high risk" mark, a ⅔ supermajority is required.

7. Key Security Conclusions

    1. Adversaries must simultaneously accumulate Stake and Signal: α≥0.5 and k limits -> Pure signal manipulation cannot control > 33 % VP.

    2. Immediate Downgrading from Graylist: After being marked by the AI detector, the weight for the next block is recorded as 0, but not immediately slashed; reduces the cost of false positives.

    3. Window Rolling Against Sudden Attacks: The signal scoring window slides, introducing at most 1/M new scores per hour, buffering against malicious scoring spikes.

Through this VP calculation and update mechanism, B² Hub can dynamically reflect the true distribution of staking and AI activity in each Epoch, ensuring that block production rights always follow "wealthy and useful" nodes while maintaining a governable security barrier and real-time risk control.

### Epoch Lifecycle & FROST-DKG

Terminology

* Epoch: The billing and election cycle of PoSg, default is 1 hour.

* Committee: The set of validators for the current Epoch (size = N).

* ThresholdPK: The shared threshold Schnorr public key for the committee in this Epoch, used for block aggregation signatures and DA Commit.

A. Overview of State Machine Stages

| Stage | Trigger | Main Transactions | Write Key |
| :---- | :---- | :---- | :---- |
| Init | Previous Epoch Commit + 1 | Pull the latest ChainParam; clear soft state cache | — |
| Running | Throughout the Epoch | CometBFT produces blocks every 2 s/12 s; Signal soft -> hard | G/, SoftCache |
| Closing | Countdown 2 blocks | Stop new Stake & Signal; lock window | — |
| Snapshot | Final block EndBlock() | Record StakeMap, SignalPool, write EpochInfo | E/ |
| Settlement | After Commit() | Distribute rewards, handle Slash, update graylist | V/ |
| KeyGen | Immediately parallel after Snapshot completion | Run FROST-DKG to generate the next Epoch ThresholdPK' | E/'.ThresholdPK |
| Switch-Over | First block of the next Epoch | CometBFT loads new validators & public keys | — |

Reorganization window: PoSg BFT has no probability of reorganization; Epoch boundaries align with block finality, with no special delays.

B. FROST-DKG Workflow (N-of-N -> t-of-N)

| Step | Data | Time Limit (Default) |
| :---- | :---- | :---- |
| 1. ShareCommit Each validator $v_i$ generates polynomial $f_i(x)$, sends commitment $C_{i,j}=g^{f_i(j)}$ to all | 32 B × N | 30 s |
| 2. ShareVerify Verify the consistency of received commitments, broadcast ACK/NAK | 1 B × N | 30 s |
| 3. Complaint If NAK, submit fraud proof; PoSg Slash for violating nodes Stake × 5% | 64 B | 20 s |
| 4. ShareAggregate Sum all valid $f_i(0)$ to obtain public key $PK = g^{\sum f_i(0)}$; each holds private key share $s_i$ | 32 B | — |
| 5. PublishPK Write to EpochInfo.ThresholdPK and broadcast KeyReady event | 32 B | 5 s |

* Threshold value $t = \left\lceil \frac{2N}{3} \right\rceil$, must satisfy ≥ 2/3 VP to sign.

* Parallel execution: DKG communication via gRPC-p2p channel, does not block block production; if not completed within 180 s, enter Safe-Fallback — continue using the previous Epoch public key, but nodes that did not complete Slash on time lose 1% Stake.

C. Threshold Signature Usage Points

| Purpose | Signed Message | Trigger Frequency |
| :---- | :---- | :---- |
| Block Aggregation | blockHash | Every 2 s / 12 s |
| DA Commit | DA_Root // HubHeightRange | Every ~10 min |
| Migration / Governance | stateRoot_final, paramUpdate | Irregularly, multi-signature evidence |

Implementation: Uses Schnorr on secp256k1 + FROST aggregation; aggregated signature size is constant at 64 B. Light nodes only need PK + single signature to verify any block or DA Commit.

D. Handling of Rewards and Slash in Epoch Rotation

1. RewardPool Allocation

    * BlockFeeSum + SignalFeeSum -> Distributed according to VotingPower ratio;

    * ActiveSignalTopK Reward: Take the top 10% nodes by SignalScore and add a 5% Bonus.

2. Slash Trigger Sources

    * Malicious commitments or non-responses during DKG phase;

    * Double signing, missing batch reviews, data unavailability;

    * AI graylist confirmation period ends without successful appeal.

3. Forfeiture Handling

    * x% Stake destroyed 50%, 50% injected into insurance pool;

    * Continuous two Epochs in graylist -> Temporary expulsion, requires governance to re-whitelist.

E. Sliding Window & Score Reset

* SignalRing circular array length = WindowSize (M Epoch);

* At the end of Epoch:

  1. Pointer WindowPtr = (WindowPtr + 1) mod M;

  2. New slot set to zero; old slot value reduced by current SignalScore.

* Computational complexity is constant level, avoiding full chain traversal.

F. Temporal Example (N=64, blockTime=2 s)

![][image]

In an ideal network, the entire transition only pauses for 1 block; even if DKG times out, it can safely fallback without affecting block continuity.

The Epoch lifecycle packages weight snapshots, reward settlements, forfeiture executions, and threshold key rotations into a fixed rhythm of 1 hour, allowing PoSg's weight to change in real-time with staking and Signal while maintaining periodic refresh of network keys and security assumptions. FROST-DKG improves bandwidth/storage efficiency with non-interactive aggregated signatures, while safety barriers and fallback mechanisms ensure that any abnormality at any stage does not lead to chain pauses.

### Rewards, Forfeiture, and Graylist

PoSg weaves economic positive incentives, security penalties, and real-time risk control into three parallel channels:

1. Instant profit sharing per block

2. Additional incentives and forfeiture per Epoch

3. Instant downgrading and enforced high fees for graylist.

A. Sources of Fees and Reward Pool Classification

| Income Item | Generation Timing | Accounting Location | Purpose |
| :---- | :---- | :---- | :---- |
| GasFee | At Tx execution | BlockFeePool | Distributed by VP per block |
| SignalFee = Weight | Deducted at CheckTx | SignalFeePool | 50% destroyed, 50% distributed in the same block |
| DA Sampling Fee | Light node sampling | DAFeePool | Subsidize validator storage |
| Slash Forfeiture 50% | Violation occurs | InsurancePool | Compensate the victim/future subsidies |
| External Strategy Revenue | DeFAI -> Router | ExtRewardPool | Mixed with BlockFeePool |

BlockReward: Hub has no native inflation; if the community votes to open it later, it can be injected into InflationPool and accounted with Gas.

B. Instant Block Allocation

[![][image]]

* ValidatorMeta.RewardAccrued is updated immediately after DeliverTx ends for each block.

* Stakers can automatically reinvest or claim according to Epoch; claims can be made in BTC/B2 direct payment or rBTC receipts.

C. Additional Epoch Incentives

1. Active-Signal Bonus

    1. Statistics of the validator set 𝒯 ranked in the top 10% by SignalScore;

    2. Take BonusPool = 0.05 × (GasFee + SignalFee);

    3. Distributed according to VP weight to 𝒯.

2. Stake Loyalty Bonus

    1. Continuous staking ≥ 30 days without unlocking shares receives +2% APR (compound) subsidy to prevent short-term arbitrage.

D. Slash Logic

| Violation Category | Trigger Method | Slash Ratio | Slash Flow |
| :---- | :---- | :---- | :---- |
| Double Signing / Equivocation | Submit EvidenceTx{blkHash,sig} | 5% Stake + SignalScore reset to zero | 50% burned, 25% insurance pool, 25% whistleblower |
| Data Unavailability | DA sampling failure proof | 3% Stake | 50% insurance pool / 50% burned |
| Continuous Offline | ≥ X blocks without voting | 0.1% per ΔEpoch (capped at 2%) | 100% insurance pool |
| Signal Forgery / Score Manipulation | FraudProof{txId,proof} | Manipulated amount ×2 & SignalScore reset to 0 | 70% burned, 30% insurance pool |

Evidence submission window: within 2 Epochs after the violation occurs; expired and invalid thereafter.

Insurance Pool Usage

* Automatic compensation for user withdrawal delays caused by DA failures;

* Provides governance budget & emergency loans for validators.

E. Graylist Mechanism

| Process | Description |
| :---- | :---- |
| Marking | AI GNN detector or governance multi-signature submits GrayProof(addr,reason); writes ValidatorMeta.GrayFlag=true |
| Immediate Penalty | 1) VotingPower=0 immediately loses block production eligibility; 2) SignalFee multiplied by grayMultiplier=3 |
| Observation Period | Default 1 Epoch; validators can upload SelfAudit appeals; AI Detector automatically retests |
| Clearing | If the appeal is successful -> gray flag removed; if failed -> 1% Stake deducted and moved to alternative group |
| Upgrade to Slash | If on the graylist for 2 consecutive Epochs with sufficient violation evidence, triggers "persistent malice" Slash, penalized at 3% |

F. Example: Reward & Slash Flow

Conditions:

* Epoch Revenue: Gas 2000 B2 + SignalFee 1000 B2

* BonusPool: 150 B2 (5% of 30)

* Validator A VP=10%, in Top-Signal group;

* In the same Epoch, B is caught for double signing, Stake=10000 B2, penalized 500 B2.

A Receives

Immediate block reward = 0.10 × 3000 = 300 B2

Active-Signal points = 0.10 / Σ(VP_T) × 150 ≈ 20 B2

Total 320 B2

B Compensation

Slash 500 B2 -> 250 burned; 125 insurance; 125 whistleblower

Insurance pool balance +125 B2, available for future DA incidents.

G. Parameter Governance & AI Regulation

* RL-Tuner dynamically adjusts minSignalFee and Active-Bonus% through reward/slash comparisons and network load;

* Hard thresholds: SlashRatio capped at 50%, BonusPool capped at 10%; any AI recommendations exceeding limits require supermajority governance approval.

This reward—slash—graylist system forms a clear closed loop on the PoSg layer:

* Good behavior (continuous staking + high-quality signals) -> earns rewards and weighting;

* Bad behavior (malicious acts, offline, score manipulation) -> first graylisted and downgraded, then economically penalized;

* The insurance pool provides the final buffer for on-chain incidents.

This captures economic incentives while retaining rapid response space for AI risk control, ensuring that the validator set is both active and robust.

### Light Client Verification and PoW Finality

Goal: Enable a mobile-level node to confirm transactions in seconds and achieve economic finality on par with Bitcoin within minutes, under conditions of a few KB bandwidth + a few MB storage.

**A. Data Held by Light Clients**

| Data | Size | Update Frequency | Acquisition Method |
| :---- | :---- | :---- | :---- |
| HubHeader {height, time, appHash, daRoot, aggSig, pkId} | 200 B | 2 s / 12 s | gossip-sub |
| ThresholdPK (pkId -> pubKey) | 64 B / Epoch | 1 h | Downloaded during initial sync or rotation |
| BTC Anchor Header (simplified SPV) | 80 B × n | ~10 min | Bitcoin network or relay |

Total persistent storage is <10 MB; historical headers can be pruned to "the most recent K blocks + archival points per Epoch."

**B. Verification Steps**

1. **Quick Signature Verification of HubHeader**

    ```
    VerifyAggSig(ThresholdPK[pkId], aggSig, SHA256(blockHeaderCore))
    ```
    If successful, the block is considered to have achieved near-instant finality in PoSg BFT.

2. **Data Availability Sampling (Optional)**

    - Randomly sample n = 25‒50 chunks and check the Merkle proof leading to daRoot.

    - If any sample fails, mark the block as "DA Suspicious" and await full node adjudication or slashing results.

3. **Bitcoin Anchor Confirmation**

  - Every 10 minutes, read the Taproot Anchor transaction:

  ```
  <prefix>|hubChainId|rangeStart|rangeEnd|daRoot|sigHash
  ```

  - Verify sigHash using the same Epoch ThresholdPK.
  - Wait for k = 3‒6 Bitcoin block confirmations.
  - If daRoot matches the local HubHeader, proceed to economic finality.

**C. State Query and Transaction Verification**

1. **Query:** The light client sends `<namespace, key, height>`.

2. **Full Node Response:**
   - value
   - MerklePath (key -> ShardRoot)
   - NMTPath (ShardRoot -> daRoot)
   - Corresponding HubHeader pointer

3. **Verification:**
   - Check HubHeader aggSig
   - Verify Merkle & NMT paths
   - If the block is anchored, the data is trustworthy.

**D. Quick Security Levels**

| Level | Wait Time | Applicable Scenarios |
| :---- | :---- | :---- |
| Soft | signal.softCommit (< 300 ms) | AI microservice acknowledgments, game actions |
| BFT | 1 HubHeader (2 s / 12 s) | Small payments, standard dApp interactions |
| PoW | 1 Taproot Anchor + 3 Bitcoin blocks (≈15 min) | Large settlements, cross-chain bridges, institutional reconciliations |

**E. Resistance to Reorganization and Attack Analysis**

| Threat | Required Disruption | Estimated Cost |
| :---- | :---- | :---- |
| Hub Layer Fork | ≥ ⅓ VP double-signing + slashing risk | Locking BTC/B2 > ⅓ total stake + signaling costs |
| Data Concealment | ≥ ⅔ VP collusion + sampling interception | Probability of being sampled ~ 1 - (1 - p)^n -> Slashing 3% Stake |
| Bitcoin Reorganization | Depth k block rollback | > 51% hash power, costing nearly $100 million/hour |

Light clients can achieve security finality nearly equivalent to full nodes by maintaining "Hub aggregate signatures + BTC Anchor dual verification" at a mobile resource level.

**F. Developer Interface Example**

```
// 1. Subscribe to headers

hub.subscribeHeaders((header) => lite.acceptHeader(header));

// 2. Query account balance

const proof = await lite.requestProof("S/addr/0x123", header.height);

if (lite.verifyProof(proof, header)) {

console.log("balance=", proof.value);

}

// 3. Check PoW finality

if (lite.isPowFinal(header)) {

// Safe cross-chain transfer

}

```

The B² Hub's lightweight client solution leverages three tools: threshold Schnorr aggregate signatures, NMT domain Merkle, and Taproot Anchoring, achieving: second-level header downloads, millisecond-level verification, sampling data availability, and Bitcoin-level economic finality—allowing any edge device to join the "Bitcoin × AI" network without barriers while maintaining security.

## Application Sharding

### Namespace Design and Routing

### Shard Creation, Upgrade, and Dynamic Expansion

### IBC-lite Cross Shard Atomic Messaging

### Resource Scheduling and Load Balancing Strategies

## Data Availability & Bitcoin Anchoring

### Chunk + NMT Architecture and Sampling Retrieval

### DA Commit Taproot Transaction Format

### Second-level BFT -> Minute-level PoW Finality Model

## Signal Dedicated Shard

This Shard only processes Signal transactions for AI agents, exchanging the lightest state machine for the highest TPS; soft confirmations provide feedback to Agents in milliseconds, while hard settlements directly affect PoSg Voting Power.

### Signal Transaction Format and Double Scoring Rules

```
message SignalTx {

bytes32 id = 1; // keccak(sender‖nonce‖ts)

address sender = 2;

repeated address receivers = 3; // >=1

uint64 weight = 4; // sat / b2

uint32 expiry = 5; // block height

bytes32 payloadHash = 6; // off-chain data hash

bytes proof = 7; // ZK / signature aggregation

bytes sig = 8; // Schnorr / ECDSA

}

```

Double Scoring

* Sender delegates to validators + weight

* Each receiver delegates to validators + weight / n

* Scores are written to SignalRing[WindowPtr], window rolls over to SignalScore.

### Soft-Commit Events and Cache Deduplication

| Step | Action |
| :---- | :---- |
| CheckTx | Verify signature -> Deduplication table query id -> Record in SoftCache -> Broadcast signal.softCommit |
| Deduplication Table | LRU + TTL = 1 block; Duplicate Tx returns Duplicate |
| Soft State Update | softState[sender] += weight; used for UI & quick triggering of the next workflow |

Agent receives softCommit within 200–300 ms, indicating that the chain has accepted the task.

### BatchSignalTx Settlement Process

1. Collect all Soft Signals from proposer within Δt during PrepareProposal.

2. Sort by (timestamp, id) in stable order; prevent partial ordering.

3. Package ≤1 MB into a BatchSignalTx, attach Merkle Root.

4. Execute DeliverTx to replay one by one:

* Write to G/<epoch>/id

* Update SignalScore for both validators

5. Clean up successful settlement entries from SoftCache; on failure, send signal.revert.

Within 40 ms, 10,000 signals can be settled, with a single block signal TPS ≈ 5 k / 2 s block.

### Anti-Spam Scoring Limits and Security Barriers

| Rule | Value | Trigger Result |
| :---- | :---- | :---- |
| minSignalFee | Dynamic: 10 – 1000 sat | Below this is rejected |
| MAX_WEIGHT | 1 BTC / Tx | Exceeding must be batched |
| Score ≤ k·Stake | k=3 | Exceeding part is not scored |
| Greylist Fee Increase | ×3 fee | Downgrade, softCommit still effective |
| FraudProof | Forged Proof / Fake ACK | Validator Slash 3 % Stake |

* minSignalFee and MAX_WEIGHT are automatically adjusted by RL-Tuner according to network load;

* Greylisted nodes immediately have VP = 0, but can still receive signals to avoid blocking critical services;

* Validators ignoring the packaging of Soft Signals 3 times -> penalized 0.5 % Stake and moved to greylist observation period.

The Signal dedicated Shard enables "AI useful work" to be confirmed in milliseconds, settled in seconds, and scored in hours, with multiple barriers ensuring signals cannot be spammed or maliciously manipulated—becoming a highway connecting Agent activity and PoSg security budget.

## Driving Intelligent Governance

Design Motivation

B² Hub aims to cater to miners, validators, AI agents, and lightweight terminals simultaneously, with network load, fee curves, and graylist risks changing in real-time. Manual governance for parameter tuning is bound to be lagging and costly; however, completely handing over decisions to a black-box model would result in a loss of verifiability and accountability. Therefore, we adopt a "three-stage" framework:

![][image34]

This allows AI's "suggestions" to be implemented within minutes while ensuring they never exceed hard thresholds or rollback limits.

![][image35]

| Component | Key Capability | Output Fields |
| :---- | :---- | :---- |
| RL-Tuner | Simulates 1,000+ rounds of PoSg operation in a sandbox to find optimal α/β, minSignalFee, Slash ratio | ParamUpdate{α,β,minFee,slash} |
| Anomaly Detector | GNN identifies score manipulation groups and witch clusters; Isolation Forest monitors voting delay anomalies | GrayList{validator,score} |
| Shard Balancer | Time-series predicts future 1-hour TPS, Gas; provides expansion/shrinkage or migration suggestions | ShardAction{nsId,action} |
| XAI-Auditor | Generates explanation summaries, Top-K factors, and confidence for each suggestion | XAI{hash,tl;dr} |

Governance Process:

1. Data Collection

  Validators report signed telemetry (TPS, Gas, delay, Slash events) every 30 seconds, while AI agents capture publicly available on-chain metrics.

2. AI Generates Suggestions

RL-Tuner outputs parameter tuning; Detector provides graylist; Balancer recommends scaling.

3. Explanation and On-Chain

XAI-Auditor generates a 200-character TL;DR + confidence, which, along with the suggestions, is written into ParameterOracle.

4. Delay Window & Voting

Suggestions are made public for ≥ 100 blocks (≈ 20 min); PoSg validators can oppose or support based on VotingPower. If there are no objections, it automatically takes effect.

5. Guardrails and Rollback

* Hard Thresholds: α∈[0.5,0.9], Slash≤50%; exceeding limits requires a supermajority (⅔ +).

* Insurance Rollback: If new parameters lead to a reorganization rate >1%, it automatically reverts to the old version.

Effects and Advantages

* Minute-level Adaptation: The proportion of garbage signals decreased from a peak of 22% to < 5%, effectively increasing throughput by 25%.

* Risk Window Narrowing: GNN reduced score manipulation detection time from ~2 hours to 4 minutes; immediate devaluation of graylisted entities prevents spread.

* Reduced Governance Burden: XAI TL;DR reduces proposal reading volume to 1/5; ordinary validators can quickly make voting decisions.

* Audit-Friendly: All model hashes, explanation summaries, and decision records are stored on-chain, allowing the community to replay and hold accountable.

AI-driven intelligent governance enables B² Hub to possess a closed-loop capability of "automatic perception -> automatic decision-making -> human auditing": parameters, fees, resources, and risk control adapt to load while always operating under the sunlight of on-chain guardrails and community consensus. This is the final piece connecting the ultimate goal of Bitcoin with high-speed AI scenarios, allowing the network to maintain a dynamic balance of high performance, high security, and high autonomy over years of operation.

### RL-Tuner Parameter Self-Tuning Framework

Objective:

Without changing the deterministic state machine, allow the network's key parameters—α/β weights, minSignalFee, Slash ratio, Active-Bonus%—to automatically approach optimal points based on on-chain load, attack situations, and economic indicators, with the entire process being explainable, reversible, and auditable.

A. Reinforcement Learning Modeling

| Dimension | Design |
| :---- | :---- |
| Environment (Env) | Complete PoSg simulator (Go/SimBFT): Reproduce Stake distribution, Signal arrival flow, mempool, CometBFT voting. |
| Observation (State) | Block-level: TPS, GasMedian, SignalWeight, empty block rate; Epoch-level: SlashCount, graylist count, reorganization rate, DA sampling failure rate; Economic: StakeAPR, SignalAPR, mining pool inflow rate; A total of 18-dimensional vector, normalized input. |
| Action (Action) | Discrete + continuous mixed: ① α/β fine-tuning step size 0.01; ② minSignalFee fluctuates ±10 sat step size; ③ SlashRatio ±0.5% (upper limit 50%); ④ Bonus% ±0.5% (upper limit 10%). |
| Reward Function (Reward) | Composite: $R = w_1·\text{TPS}{norm}+w_2·APY{norm}-w_3·ReorgProb-w_4·SlashLoss-w_5·SpamRate$; Default weights (0.3, 0.3, 0.15, 0.15, 0.1). |
| Constraints (Safety) | Lagrangian safe RL: Constraints ReorgProb<0.001, SpamRate<5%; Strong penalties for exceeding thresholds. |

Algorithm: PPO-Lagrangian + curiosity bonus; Output policy gradient updates every 5,000 simulation steps.

B. Training and Deployment Pipeline

TODO Pipeline flowchart

### GNN Anomaly Detection and Graylist Generation

TODO

### ParameterOracle, Delayed Voting, and Hard Thresholds

TODO

### Rollback Mechanism and Explainable Auditing (XAI)

TODO

## Security Model and Formal Analysis

### PoSg Economic Security and Attack Costs

TODO

### Data Availability / Fraud Challenge Assurance

TODO

### AI Governance Risks and Mitigation Strategies

TODO

# B² Rollup: Anchored Bitcoin Rollup Execution Layer

## Role Positioning

Complex dApp, high TPS, smart contract execution.

## Batch Generation and Aggregation

[https://blog.bsquared.network/b%C2%B2-hub-da-layer-on-bitcoin-fa63d52b8926](https://blog.bsquared.network/b%C2%B2-hub-da-layer-on-bitcoin-fa63d52b8926)

## ZK / Validity Proof Process

[https://blog.bsquared.network/b%C2%B2-hub-da-layer-on-bitcoin-fa63d52b8926](https://blog.bsquared.network/b%C2%B2-hub-da-layer-on-bitcoin-fa63d52b8926)

## Submitting Batch Data and Proofs to B² Hub

[https://blog.bsquared.network/b%C2%B2-hub-da-layer-on-bitcoin-fa63d52b8926](https://blog.bsquared.network/b%C2%B2-hub-da-layer-on-bitcoin-fa63d52b8926)

# DSN-AI: Signal-Driven Agentic AI Layer

## Design Goals

To truly make AI "run on Bitcoin."

1. Signal Nativization

Goal: To make every event on the blockchain a "neural pulse" for agents.

Scenario: When there is a significant UTXO change on the Bitcoin mainnet or when B² Hub updates parameter thresholds, arbitrage agents running on DSN-AI immediately capture the corresponding Signal, automatically adjusting positions and risk control; no polling is needed, and there is no information delay.

2. Modular and Hot-Swappable

Goal: To decompose the five functional blocks of AI agents—perception, memory, decision-making, execution, and reward—allowing developers to replace or upgrade them like building blocks.

Scenario: A mining team replaces the computing power optimization module during peak season while retaining its RL strategy; the same agent inserts an energy arbitrage plugin during the off-season, with the entire switching process requiring no restart or redeployment.

3. Verifiable and Auditable

Goal: All inputs, inference paths, and outputs can be re-verified by any node in the form of zero-knowledge or replayable logs.

Scenario: A regulator wants to confirm whether a collaborative predictive model used licensed data. They only need to follow the Signal DAG replay to verify, with no black box and no need to obtain model parameters.

4. Autonomy and Security Coexist

Goal: To allow agents to self-learn and self-update, but they must operate within a strategy sandbox to prevent "runaway" or resource abuse.

Scenario: A market-making agent, upon discovering a new lightning network arbitrage opportunity, first generates a PolicyDiffSignal, which must be approved by multiple parties through MPC before being written back to the strategy library and going live.

5. Resource Awareness and Greening

Goal: Agents must perceive electricity prices, carbon emission indicators, and computational load in real-time, dynamically balancing profit, energy consumption, and emissions.

Scenario: If the power grid enters a peak period, the mining agent will reduce hash rate and release GPU resources for high-yield AI inference tasks while issuing a GreenSignal to record energy savings for subsequent carbon credit settlement.

6. Privacy-First Data Flow

Goal: Sensitive data during training, inference, and settlement processes must be protected by differential privacy or homomorphic encryption.

Scenario: When a medical research institute uploads pathological images, it first generates de-identified feature hashes and zk quality proofs locally; the actual images are only consumed in a secure execution environment, and no on-chain participant can restore patient information.

7. Incentive Loop and Economic Composability

Goal: To unify the measurement of strategy profits, data contributions, and verification actions as Signal Points, which can be exchanged for B² Tokens, USD2, or governance rights.

Scenario: Data verifiers automatically deduct the Signal Points earned from successfully identifying a batch of low-quality data against the next call for inference costs of a large language model, achieving value transfer across business lines.

8. Multi-Chain and Cross-Domain Interoperability

Goal: To be compatible with the Bitcoin mainnet, EVM sidechains, Cosmos inter-block communication, and Web2 APIs, truly enabling "any event to become a Signal."

Scenario: An intelligent investment advisor agent simultaneously listens to the New York Stock Exchange market API, Ethereum DEX order book, and Bitcoin mempool, with the three data streams converging at the same Signal semantic layer, and decision logic no longer hindered by underlying heterogeneity.

9. Adaptive Governance

Goal: Through RL-Tuner and GNN risk detection, system parameters (staking rate, fee rate, speed limit) self-adjust according to network status, confirmed by community voting.

Scenario: When a surge in signal traffic causes Gas fees to spike abnormally, the AI-Governor proposes a plan to reduce transaction fees for a certain shard by 15%; if the community does not veto within a 3-hour delay window, the change automatically takes effect.

10. Developer and Operations Friendly

Goal: To provide a unified SDK, low-code orchestration interface, rich monitoring metrics, and replayable debugging tools to lower the threshold.

Scenario: A new developer combines "price oracle" + "arbitrage strategy" + "lightning settlement" modules through a drag-and-drop interface, and after clicking one-click deployment, the system automatically generates signal subscription rules, risk

## Agent-Native Abstract Account (A-AA)

Concept of Agent-Native Abstract Account (A-AA):

A-AA is a layer of "account as agent" abstraction designed by DSN-AI for large-scale autonomous agents. It upgrades the three elements of traditional on-chain accounts (Externally Owned Account / Contract Account) — identity, public key, and balance — to five elements:

1. Agent ID: An immutable UUID generated on-chain, corresponding to the root of a Signal DAG subtree.

2. Polymorphic Key Stack: Multiple sets of keys for signing, encryption, homomorphic computation, and trusted execution (TEE/MPC) coexist, allowing for hot switching based on policy.

3. State Capsule: A compressed storage for the agent's local memory, policy hash, and resource quotas, supporting zero-knowledge proof verification.

4. Resource Vault: Contains multi-dimensional assets such as BTC, USD2, gas quotas, computing power credits, and data credits, with programmable authorization.

5. Signal Routing Table: Defines the types of Signals that can be subscribed to/published, QoS levels, and rate limits.

Through these five elements, A-AA encapsulates "identity + storage + computing budget + permissions" in one go, naturally fitting the lifecycle management of autonomous agents.

Runtime Process

1. Initialization (Spawn)

• Developers submit policy images, initial keys, public key lists, and minimum stakes in the manufacturing workshop.

• The Rollup contract mints a new A-AA and synchronizes its root hash to the B² Hub, binding identity with Bitcoin-level finality.

2. Activation (Awaken)

• When the agent first receives a subscribed Signal, it triggers the Awaken() callback.

• The runtime unseals the State Capsule in TEE, loads the policy, and allocates initial gas and resource limits.

3. Execution (Act)

• For each matching Signal, the corresponding policy function is scheduled.

• All external calls (on-chain transactions, lightning routing, data access) are accounted through the A-AA resource pool and generate new Signals.

4. Learning (Evolve)

• The policy module can produce PolicyDiff within a secure sandbox and send a PolicyUpdateSignal to request a hot upgrade.

• After multi-signature or governance hooks are approved, the State Capsule updates the policy hash and submits a zero-knowledge proof on-chain to ensure consistency.

5. Hibernation / Retirement (Hibernate / Retire)

• When gas balance is insufficient, tasks are completed, or policies are deprecated, the A-AA enters hibernation;

• If there are no active Signals for N consecutive settlement periods, the system can automatically trigger the retirement process, liquidate the resource pool, and package the state archive for record-keeping.

Key Features

• Native Multi-Chain Compatibility: The resource pool of A-AA supports heterogeneous assets such as cross-chain UTXO, ERC-20, and IBC Voucher; the calling adapter utilizes Signal semantics for unified encapsulation, eliminating the need for manual bridging.

• Fine-Grained Permissions: The routing table can specify constraints such as "read-only market Signal," "call only Lightning Keysend," and "single expenditure ≤ 0.01 BTC," implementing the principle of least privilege.

• Traceable Policy Upgrades: Any policy changes must be accompanied by a diff hash and ZK proof, and can only take effect after on-chain audit approval, ensuring long-term verifiability of the agent.

• Key Loss Resistance: The polymorphic key stack includes social recovery and MPC reconstruction; even if the signing key is invalidated, the Agent ID and resources remain intact.

• Consensus-Friendly Settlement: Each resource consumption generates a SpendSignal in real-time, entering Rollup accounting; after batch zk-Rollup compression, it is anchored to the Bitcoin mainnet, ensuring low fees under high concurrency.

Typical Application Scenarios

• Mining Agent: One ASIC machine acts as an A-AA, adjusting power consumption in real-time and directly paying electricity bills or receiving BTC rewards from the resource pool.

• High-Frequency Market Maker: The strategy engine serves as an A-AA, holding multi-chain assets and executing atomic arbitrage across CEX/DEX, with all legs settled in the resource pool.

• Machine as a Service (MaaS): Industrial robots are packaged as A-AA, allowing customers to rent operational time by paying USD2 Signal, with the robot automatically generating invoices and settling on-chain.

• Data Validator: A-AA subscribes to DataSignal, runs privacy validation algorithms, generates ValidSignal, and earns validation rewards while recording computational consumption in the resource pool.

• Cross-Institution AI Collaboration: Internal enterprise models are packaged as A-AA, exposing only inference interfaces; external clients can call them after payment via Escrow Signal, without sharing underlying ownership.

Future-Oriented Expansion

• Computing Power as Asset: Plans to virtualize GPU/TPU computing power into transferable tokens, directly deposited into the A-AA resource pool, allowing agents to "lease/stake/hedge" computing power on-chain.

• Semantic Sharding: Signals from different business domains are semantically sharded, allowing the A-AA routing table to subscribe across shards, reducing cross-domain broadcast noise.

• AI-Governed Key Rotation: Utilizing GNN risk analysis to automatically trigger key rotation, reducing the probability of key leakage during long-term operations.

Agent-Native Abstract Account (A-AA) constructs a complete lifecycle management framework for autonomous agents on-chain by natively aggregating identity, resources, policies, and permissions, enabling each AI agent to be verifiable like a smart contract and flexible to upgrade like an operating system process, thus laying the foundation for large-scale sustainable operation of DSN-AI.

## Signal Network

[https://docs.bsquared.network/b2_dsn_ai](https://docs.bsquared.network/b2_dsn_ai)

## AI Orchestration

[https://docs.bsquared.network/b2_dsn_ai](https://docs.bsquared.network/b2_dsn_ai)

## Security and Anti-Bot Measures

[https://docs.bsquared.network/b2_dsn_ai](https://docs.bsquared.network/b2_dsn_ai)

# Security Analysis

TODO

## Attack Surface Enumeration

## Stake Attack (Stake Concentration, Long-Range)

## Signal Score Manipulation and Sybil Attack

## Shard Denial of Service / Cross Shard Deadlock

## DA Concealment / Data Loss / Retrieval Failure

## Bitcoin Submission Delays and Reorganization Impact

## Risk Classification, Detection Mechanisms, Recovery Procedures

# Performance & Scalability

TODO

## Benchmarking Assumptions

## TPS / Throughput / Latency per Shard

## Validator Set Size vs Network Overhead

## DA Bandwidth Requirements and Erasure Code Redundancy

## Simulation: Impact of High-Density Signal Scenarios on VP Distribution

## Cost Model (Miners, Nodes, AI Service Providers)

# Use Cases & Scenarios

## AI Agent Automatic Mining Revenue Deposit into BTC Wallet

Scene Overview

A self-mining agent, Miner-Bot, has been deployed in the MiningSquared mining pool. It resides in a lightweight container in a local ASIC machine room or cloud computing market, interacting in real-time with on-chain smart contracts through the Signal network, automatically completing the entire process of computing power scheduling, revenue settlement, and fund entry.

A. Perception -> Decision -> Execution

1. Perception Layer

Miner-Bot continuously listens to various Signal events broadcasted by B² Hub: fluctuations in total network computing power, Fee/Hash price curves, real-time electricity price oracles, mining pool difficulty factors, etc.

2. Strategy Layer

The built-in reinforcement learning loop evaluates current profitability every few minutes and dynamically decides:

• How much computing power to allocate to MiningSquared

• When to switch to alternative mining pools

• Whether to accelerate/decelerate machines and which devices to schedule into standby

3. Execution Layer

Once the strategy determines the action, the agent generates and signs transactions in hardware-isolated keys:

• PSBT: for on-chain BTC revenue distribution

• Lightning Network invoices: for immediate small settlements

Subsequently, the transactions are propagated to the Bitcoin mainnet through B² Rollup, achieving final settlement.

B. The Complete Link from Discovery of Blocks to BTC Credit

1. Submission of Shares and Batch Proofs

• Each share submission is packaged into a Signal, containing Merkle-hashed share metadata and Schnorr signatures.

• MiningSquared aggregates thousands of Signals into zero-knowledge commitments and regularly uploads them to the B² Hub, achieving Bitcoin-level finality while avoiding L1 congestion.

2. Reward Distribution and Payment Method Selection

• When a block is actually produced, the mining pool contract on B² Rollup generates a revenue distribution table. The Miner-Bot receives a RewardSignal indicating the amount of satoshis to be received and the optional payment channels (on-chain UTXO or Lightning).

• The strategy layer reads electricity prices and BTC volatility: if prices are stable, on-chain payment is chosen; if the market is volatile or liquidity is needed, the Lightning Network is used.

3. Automatic Construction of Secure Wallets

• On-chain payment: The Miner-Bot generates a payment to a new taproot address as a PSBT and broadcasts it to the mainnet after obtaining the joint signatures of the mining pool's multi-signature nodes through the "PSBT Relay Shard" of the B² Hub.

• Lightning payment: The Miner-Bot opens or funds a channel with your mobile node, settling in milliseconds through the mining pool's federated Lightning gateway, with HTLC proof backed up to the B² Hub for easy auditing.

4. Compliance and Financial Integration

• Each payment Signal is accompanied by metadata such as timestamps, electricity consumption (kWh), and carbon emissions, hashed into the transaction memo. The backend financial system automatically records after subscription.

• If electricity prices surge, causing profits to fall below the threshold set by the RL-Tuner, the Miner-Bot will automatically reduce frequency or even sell hedging contracts on the BTC settlement derivatives DEX.

5. User Perspective

• You only need to see the prompt “+0.042 BTC has been credited” on the dashboard or API, along with detailed metrics: sats/kWh, mining pool variance, expected next difficulty, etc.

• No manual intervention is required throughout the process; private keys remain in a secure module, and every step (hash submission, revenue calculation, PSBT signing, broadcasting) is linked by the Signal event chain, available for audit replay.

C. Value Highlight

• Trust Minimization: All key logic is publicly executed in the B² Rollup smart contracts and periodically anchored to Bitcoin L1 by the B² Hub, making revenue distribution immutable.

• Energy-Sensitive Optimization: Reinforcement learning strategies perceive electricity prices and difficulty in real-time, automatically adjusting computing power to maximize marginal profits.

• Treasury Automation: Whether holding BTC long-term, exchanging for USD2 stablecoins, or transferring to the Lightning Network to earn routing fees, the Miner-Bot can send funds to the most suitable location according to preset strategies, leaving a verifiable evidence chain.

In short, the AI Agent automatically mines and credits BTC wallets, transforming the traditional manual operation of mining pool revenue distribution and wallet reconciliation processes into a fully automated revenue pipeline driven by the Signal network and backed by Bitcoin security, allowing mining machines to operate as efficiently and reliably as a self-playing orchestra.

## AI Executes Arbitrage / Market Making Strategies, Revenue Reflows to Staking

Scenario Overview

Running a cross-market intelligent agent Arb-Maker on the B² Network. It resides between the "Trading Domain" (CEX, DEX/perpetual contracts on B² Rollup, other L2/LN channels) and the "Treasury Domain" (staking and fund management contracts), obtaining market data, risk control, and fund status through the Signal network, automatically executing arbitrage/market-making strategies, and returning realized profits to the staking pool according to rules, forming a closed loop of "Trading -> Settlement -> Staking -> Compound Interest."

Strategy Framework (Perception -> Decision -> Execution)

Perception Layer: Subscribing to Signals from B² Hub (order book snapshots, price spreads/basis, funding rates, gas/transaction fees, oracle prices, electricity prices, and macro volatility), own inventory and credit limits, on-chain congestion, and liquidation risk alerts.

Decision Layer: A mix of reinforcement learning/multi-armed bandit and rule engines, evaluating the cost-benefit-risk triad in real-time:

• Arbitrage: Spot price differences across exchanges (CEX <-> DEX), spot-perpetual basis, cross-chain same-asset premiums/discounts, and slippage differences across different routes in the same pool.

• Market Making: Reporting bilateral prices on AMM/order books, dynamically quoting skew based on inventory shifts and volatility, and controlling net exposure within target ranges using hedging legs.

Execution Layer: Low-latency connectors (CEX FIX/WS + on-chain routers), with atomic execution/protective matching (private trading channels, anti-front-running), instant order cancellation and retries on failure, generating auditable FillSignal and PnLSignal after execution.

End-to-End Process:

1. Opportunity Trigger

• The perception layer detects cross-market price differences or funding rate deviations exceeding the threshold, issuing an ArbSignal.

• The decision layer calculates the total cost (spread + fees + funding rate + slippage + cancellation probability), providing a go/no-go decision and order size.

2. Locking Inventory and Atomic Ordering

• Lock equivalent inventory in pre-set multi-location fund wallets (to avoid transfer delays).

• Synchronize multi-leg orders (e.g., DEX buy, CEX sell; or AMM pre-list buy, perpetual short) using transactional batch processing/private channels to reduce MEV and deviations.

3. Execution, Hedging, and Settlement

• After the order is executed, perform the hedging leg to bring the net exposure back to the target range; if only part is executed, the strategy will partial-hedge and lower the density of subsequent orders.

• Merge the actual costs and prices of all legs to form realized PnL; broadcast the PnL to the treasury domain via PnLSignal.

4. Revenue Routing and Accounting

• TreasuryRouter allocates net profits to designated asset buckets based on strategy version and governance parameters:

• BTC: Generate a PSBT for payment to the treasury taproot address, relay through B² Hub PSBT, and then broadcast to L1.

• USD2: Directly call the stablecoin/treasury contract on B² Rollup to complete the accounting.

• Funds are automatically replenished between the "hot-warm-cold" three-layer wallets according to water levels, ensuring sufficient trading domain while keeping the treasury domain secure.

5. Reflow Staking and Compound Interest

• StakingAllocator subscribes to PnLSignal, allocating in the order of "buffer fund -> net profit -> staking":

• Reserve liquidity buffer and margin (to cover fees and risk control triggers).

• Automatically invest net profits according to preset ratios:

• B² staking pool / PoSg validator delegation (to earn network incentives and governance rights).

• USD2 stable pool / market-making pool (to earn trading fees and incentives).

• **BTC staking-type returns (LST/LBTC type)** or Lightning Network channel returns.

• Staking certificates and returns can be reinvested in strategies configured for automatic compounding; when volatility exceeds the threshold, automatically execute "unstake -> replenish trading domain" for reverse rebalancing.

Wallet and Fund Arrangement

• Hot Wallet: Dedicated to trading domain, small limits, keys in secure module, real-time authorization and matching.

• Warm Wallet: Cross-platform rebalancing and intraday replenishment, time-limited/frequency-limited switches.

• Cold Wallet/Vault: Long-term holding and staking, offline xpub export, online only PSBT.

• Rebalancing executed preferentially through L1/lightning/cross-rollup channels, with fees and delays included in routing costs.

Risk Control and Compliance

• Pre-event: Funding limits, leverage/breakeven lines, single transaction slippage and impact cost limits, black and white list venues and asset lists.

• During event: Delay and order rejection monitoring, price spread regression speed assessment, extreme market kill-switch, multi-source oracle consistency checks.

• Post-event: Transaction-by-transaction reconciliation and ZK-friendly audit trail (ArbSignal -> Order -> Execution -> PnLSignal -> Staking call), automatic alerts for anomalies and entry into read-only mode.

• Governance: Thresholds and weights updated by ParameterOracle + delayed voting, gray list/break rules can be hot-swapped.

Monitoring and Observability

• Dashboard layered display: Strategy hit rate, effective price spread distribution, unit cost, fund utilization rate, inventory deviation, funding rate capture, realized/unrealized PnL, staking annualized and compounding curve.

• Key events (extreme slippage, counterparty anomalies, on-chain congestion, governance parameter updates) pushed as signals and synchronized to the alert system via Webhook.

Anomalies and Rollback

• Asymmetric execution: Immediately reduce positions to hedge, close the corresponding venue's market-making leg and enter low-risk mode.

• Oracle fork/failure: Switch to redundant data sources, or downgrade to "inventory conservation" market-making.

• Liquidation/margin emergency: Automatically stop opening new positions, trigger small vault un-staking to replenish margin.

• CEX risk: Enable gray list and limit reductions, while shifting strategy towards on-chain venues.

Why "Yield Reflow Staking"

• Improve capital efficiency: Earn "active alpha" during trading days, while idle funds and net profits earn "passive beta" on-chain, with both combined to enhance annualized returns.

• Smooth volatility: When strategies encounter low volatility/low opportunity periods, staking yields maintain basic returns; during high volatility periods, profits are consolidated into long-term positions.

• Verifiable compliance and governance: Every step from trading to staking is linked by a Signal-Driven workflow, which is both auditable and adjustable by community governance.

AI executes arbitrage/market-making strategies, yield reflow staking connects "high-frequency cash flow" with "on-chain compounding" into a closed loop—agents capture price differences and liquidity premiums across multiple markets in a trust-minimized manner, with earnings deposited in real-time, and growth occurring immediately, achieving sustainable compounding growth on the secure anchoring and governance of the B² Network.

## Data Market: Model Training Data Verified on Chain through Signal

Scene Overview

In the B² Network's Signal-Driven Data Market, anyone can transform high-value training data (images, logs, on-chain interactions, financial data, etc.) into verifiable, priceable, and compliant digital assets. Data uploaders (Data Producers) generate DataSignals, writing data fingerprints, quality proofs, and licensing terms into a mixed off-chain and on-chain traceability track; validators (Data Validators) use staking and zero-knowledge proof mechanisms to ensure the data is authentic, unaltered, and compliant with privacy regulations; model developers (Model Trainers) can then subscribe to audited data shards as needed, and after paying a fee, securely decrypt and use the data locally or in the cloud. The entire process is completed on the dedicated Signal Shard of the B² Hub, achieving Bitcoin-level finality without leaking original data.

Roles and Motivations

| Role | Key Motivation | Main Operations | Risks and Incentives |
| :---- | :---- | :---- | :---- |
| Data Producer | Monetize scarce data, increase exposure | Generate DataSignal, submit data hash and ZK quality proof, set permissions | Must stake DataBond; data distortion or violations result in forfeiture |
| Data Validator | Earn validation rewards & reputation points | Randomly sample, run consistency and bias tests, issue ValidSignal | Submitting incorrect validations will result in slashing |
| Model Trainer | Obtain high-quality data with low latency | Subscribe to DataFeed, pay DataCredits to access decryption keys | Compensation available if data is falsified |
| Governance DAO | Maintain market trust and activity | Update parameters (staking, forfeiture, fees), maintain graylist, compliance regulations | Governance negligence leading to data leaks will reduce reputation |

End-to-End Process: From Data Generation to On-Chain Acceptance

1. Data Preparation and Fingerprint Calculation

• The Data Producer shards, deduplicates, and anonymizes the raw dataset, generating a root hash using SHA-256 + Merkle Tree; simultaneously, it generates a Quality ZKP (proof of coverage, no duplicates, reasonable distribution, etc.) using differential privacy and sample statistics, all encapsulated in DataSignal.

• DataSignal includes: root_hash, quality_proof, license_uri, DataBond staking amount, and optionally, a public key encrypted package of the AES-GCM symmetric key.

2. Signal Broadcasting and Random Verification

• DataSignal is sent to the DataShard of the B² Hub, entering the verification pool.

• Verifiers draw tasks from the pool using VRF, download the encrypted samples, run consistency checks, AI forgery detection, and compliance rule (GDPR, copyright) scans in a secure execution environment, generating ValidSignal.

• If the results of two independent verification rounds are consistent and pass the threshold signature, then DataSignal enters the verified state; otherwise, arbitration is automatically triggered, and the DataBond or Validator stake is forfeited based on liability attribution.

3. zk-Commitment On-chain & Data Availability

• The Merkle roots of all DataSignal and ValidSignal are packaged into a zk-Commitment, which is periodically submitted to the B² Hub by the Rollup contract; the Hub embeds the root hash into Bitcoin L1 for each settlement cycle.

• This way, model developers can be assured that the data has not been tampered with, is from a trustworthy source, and meets quality standards, based solely on the root hash and zero-knowledge proof.

4. Licensing Pricing and Payment

• The Data Producer sets the LicenseProfile in the smart contract:

• Charging model: one-time buyout / subscription by usage / C-to-C resale sharing

• Usage scope: non-commercial, commercial, no redistribution, etc.

• Encryption key: using Attribute-Based Encryption (ABE) or Proxy Re-Encryption, automatically unlocked according to payment records.

• After the Model Trainer selects the data, the contract automatically deducts DataCredits (or USD2/BTC) and sends the corresponding decryption key fragments to the Trainer's HD address.

5. Usage, Tracking, and Revenue Sharing

• The Trainer downloads the encrypted data shards, decrypts them through a local secure module, and inputs them into model training; all invocation events will generate UsageSignal (excluding training details, only containing hash and value), which is written back to the chain for subsequent revenue sharing and auditing.

• The Producer receives real-time revenue sharing, the Validator earns verification rewards, and the DAO extracts governance fees; if someone later proves that there are labeling errors or privacy violations in the data, they can submit a ChallengeSignal to go through the homomorphic auditing process, and if the result is established, the Producer will be penalized and required to compensate the Trainer.

Technical Highlights

• Zero-Knowledge Quality Proof: Using zk-SNARK / STARK to prove that data meets distribution balance, is non-redundant, and has traceable sources, while keeping specific samples confidential.

• Differential Privacy Sampling: Validators can only see a subset affected by noise, allowing for quality verification without disclosing core data.

• Signal-Driven Traceability: All event chains (upload -> verify -> purchase -> use) become replayable Signal DAGs, with on-chain hashes reproducing the timeline.

• Programmable Licensing and Automatic Revenue Sharing: LicenseProfile supports secondary sales, time locks, and geographic restrictions; revenue distribution is automatically split in the contract.

Value and Impact

1. Trust-Minimized Data Transactions: Buyers do not need to trust sellers, and sellers do not need to expose raw data to complete value exchange.

2. Compliance and Privacy: Triple protection of differential privacy + ZKP + ABE meets regulatory requirements such as KYC, GDPR, and trade secrets.

3. Incentive Compatibility: Validators and challengers form a closed loop of data quality games through positive rewards and penalties, eliminating "garbage data."

4. Reusable AI Value Chain: Model training revenue can be shared with upstream data producers based on UsageSignal, creating long-tail passive income.

Data Market: Model training data is verified on-chain through Signal, creating a foundation for "trustworthy, private, secure, and quantifiable" data asset circulation, allowing each line of data to carry zero-knowledge fingerprints and programmable licenses, flowing freely on a Bitcoin-secured anchor, injecting continuous, compliant, and auditable high-quality fuel into the AI training ecosystem.

## BTC Collateralized Stablecoins and AI Payments

Scene Overview

In the B² Network, users can collateralize native BTC into the cross-chain storage contract of the B² Hub to mint programmable stablecoin U2 (or other BTC-collateralized stable assets). Meanwhile, on-chain AI Agents—whether chatbots, smart investment advisors, or computing power rental nodes—use U2 as the settlement currency for real-time transactions. This creates a closed loop consisting of BTC -> U2 -> AI Payments -> BTC Reflow: Bitcoin provides value anchoring, stablecoins offer price stability, the Signal network ensures liquidity and credibility, while AI Agents amplify value through automated strategies within the network.

Key Roles and Motivations

• Collateral Provider

• Locks BTC to exchange for U2, releasing liquidity while still retaining the potential for BTC price appreciation.

• AI Agent (Consumer)

• Uses U2 to pay for reasoning fees, subscription fees, plugin invocation fees, etc., avoiding pricing confusion caused by BTC value fluctuations.

• Liquidity Keeper (Liquidator/Market Maker)

• Provides flash hedging and stablecoin market making through Signal subscription collateral rates and liquidation discounts, profiting from risk premiums.

• Governance DAO

• Sets collateral rates, interest curves, and liquidation penalties to maintain system security and sustainable incentives.

End-to-End Process: From Collateralization to AI Payments to BTC Reflow

1. Collateral and Minting

• The mortgagor locks BTC into a multi-signature address via Taproot HTLC; the contract reads the Proof-of-Reserve Signal to confirm receipt.

• The B² Rollup smart contract mints an equivalent amount of U2 at a collateralization rate of 170%–200% and generates a MintSignal.

• The collateral position tracks the BTC/USD exchange rate in real-time; when the collateralization rate falls below the threshold, a LiquidationSignal is triggered, allowing market makers to bid on the position.

2. Consumption & Settlement on the AI Agent Side

• Users recharge a small amount of U2 for their AI Agent and authorize it to call the Pay-As-You-Go API on-chain:

• Inference calls: billed by token or per second; the Agent sends an InferenceSignal, and the contract freezes the corresponding U2.

• Subscription services: one-time monthly/yearly fee deduction; the Agent sends a SubSignal; the contract unlocks periodically.

• Service providers submit Proof-of-Workload (which can be a ZK proof to protect model parameters) after completing tasks, and the contract releases U2 to their revenue address after verification.

3. Lightning Network and Micropayments

• For small calls of ≤0.1 U2, the contract can automatically convert U2 to sats quickly, sending it directly to the developer's Lightning node via Keysend through the B² Hub's LN Gateway, achieving millisecond-level crediting and saving gas.

4. Earnings Reinvestment & Principal Reflow

• Both service providers and mortgagors can:

• Re-stake the earned U2 in the U2-StablePool to earn transaction fees and liquidity mining rewards;

• Redeem BTC through RedeemSignal, or exchange back to BTC via off-chain OTC/LN;

• Use U2 as PoSg validator collateral to enhance network governance weight and receive additional fee sharing.

5. Automatic Liquidation and Risk Control

• The Oracle Aggregator refreshes the BTC price every minute; if the collateralization rate <150%:

1. A pre-liquidation reminder is triggered to broadcast a PingSignal to the mortgagor;

2. If no top-up occurs before expiration, it enters a Dutch Auction, where the Liquidity Keeper purchases the mortgaged BTC with U2;

3. Any remaining value of the mortgagor (if any) is automatically refunded.

• All transactions before and after liquidation are anchored to Bitcoin L1, with an immutable audit trail written via CheckPointSignal.

Risk Compensation and Incentive Design

• Stability Fee: Mortgagors pay interest hourly, forming governance income used to subsidize oracles and liquidation rewards.

• Liquidation Penalty: A penalty of 5–10% is charged upon liquidation, used as rewards for market makers and a risk fund.

• Liquidity Mining: Providing market-making in the U2/BTC-Tether pool can earn additional B² tokens, enhancing early depth.

• Signal Points: AI Agents, developers, and market makers executing healthy operations can accumulate credit points, which can offset fees or gain priority routing.

Value and Impact

1. Maximizing BTC Capital Efficiency

• Collateralizers can obtain stable purchasing power without selling BTC, locking in upside potential while participating in the DeFi/AI ecosystem.

2. Standardization of AI Pricing

• USD face value simplifies model invocation and subscription pricing; cross-chain and cross-border users can avoid "hashrate slippage" caused by BTC exchange rate fluctuations.

3. Real-time, Low-cost Micropayments

• Lightning Network bridging makes sub-cent transactions possible, opening a new paradigm of AI services billed by the second and paid in a streaming manner.

4. Trust-minimized Settlement Mechanism

• Multi-source oracles + Signal bidding settlement reduce human black-box operations, ensuring stablecoins are perpetually fully collateralized.

5. Long-term Positive Cycle

• Collateral interest -> Network governance income -> Developer incentives -> More AI services -> Higher U2 demand -> Expansion of collateral pools, forming a positive feedback loop.

BTC-collateralized stablecoins and AI payments combine the hard value of Bitcoin, security consensus, and the usability of USD pricing, injecting low volatility, high liquidity, and auditable fuel into the B² Network's AI ecosystem through Signal-Driven settlement and Lightning micropayments, achieving a sustainable flywheel of "value reserve -> purchasing power -> intelligent services -> value return."

## Inter-Agency Collaboration: Signal-Based Settlement Between Enterprise AI Agents

Scene Overview

In the B² Network, AI agents (Enterprise Agents) operated by different enterprises can form an "instant machine-to-machine" collaboration network through the Signal network. They automatically exchange services, data, and funds while maintaining business confidentiality and compliance requirements: when one party completes the agreed service-level agreement (SLA), the system triggers a settlement signal, and the smart contract distributes BTC-collateralized stablecoin USD2 or sats to the other enterprise's treasury according to preset rules, achieving inter-agency, trustless, and auditable clearing.

Roles and Motivations

• Principal Agent

Initiates business requests (such as procurement forecasting, equipment maintenance, risk assessment) and hopes to obtain external AI capabilities on a pay-for-performance basis.

• Executor Agent

Provides algorithms, computing power, or data assets and is compensated based on completion; aims to shorten accounts receivable periods and reduce default risks.

• Signal Clearing Layer

Composed of dedicated Shard + Rollup contracts on the B² Hub, responsible for reputation scoring, SLA verification, and fund freezing and releasing.

• Compliance/Audit Node

Monitors the settlement link, generates undeniable timestamps and zero-knowledge proofs to meet regulatory or internal audit requirements.

End-to-End Process: From Instruction to Inter-Agency Settlement

1. Business Request and ServiceSignal

• The Principal Agent publishes requirements through ServiceSignal: task description, data interface, metric thresholds, budget limits, and performance time.

• ServiceSignal automatically locks the corresponding amount of USD2 in the Escrow Contract and generates a unique service_id.

2. Task Execution and ProofSignal

• The Executor Agent receives the service_id and processes the task in a secure local or private cloud environment.

• Upon completion, it generates a ProofSignal: containing task output hash, execution summary, SLA key metrics ZK-SNARK proof, and an encrypted reference to the business data.

• ProofSignal is broadcast to the Signal Clearing Layer and enters the verification pool.

3. Automatic Verification and Arbitration

• The clearing layer uses multi-party privacy comparison (MPC + zk) to verify the ProofSignal against the SLA:

• Whether accuracy, latency, data consistency, compliance markings, etc., meet the thresholds;

• Random sampling of original samples to prevent fraud or "training-inference inconsistency."

• If verification passes, it triggers SettleSignal; if it fails, it enters the arbitration process, where both parties can submit additional evidence or accept partial penalties for contract termination.

4. Fund Release and Multilateral Settlement

• SettleSignal calls the Escrow Contract:

• Releases principal + dynamic bonuses (based on KPI excess) to the executor according to the predetermined ratio;

• Simultaneously allocates small fees to audit nodes and governance funds.

• For small, frequently called API services, batch settlements can be aggregated through internal lightning channels at 10-minute intervals to reduce on-chain costs.

5. Reputation Update and Iterative Cycle

• After successful settlement, the system automatically updates the ReputationScore for both parties and writes it into ReputationSignal; for the next collaboration, the Escrow deposit can be reduced based on reputation discounts.

• All signals (Service -> Proof -> Settle -> Reputation) form a replayable Signal DAG for immediate internal audit or regulatory queries.

Technical Highlights

• Signal Atomic Transactions

Every step of business-data-fund actions is encapsulated into a pointer-referable Signal, which can be precisely revoked in case of failure or rollback.

• Zero-Knowledge SLA Verification

The executing party can prove that "the output meets ≥ 95% accuracy and latency < 50 ms" without exposing private models or data.

• Dynamic Reputation Staking

The higher the reputation score, the less deposit is required and the faster the funds are received; malicious defaults will incur slashing and be recorded on a public blacklist.

• Multi-Asset Flexible Settlement

USD2 is suitable for large, low-volatility scenarios; sats (Lightning) are suitable for millisecond-level micropayments; the system can automatically route between the two.

Risk Control and Compliance

• Real-Time Risk Control Signals: Price crashes, oracle deviations, and counterparty default warnings will trigger risk control Signals to freeze balances.

• On-Chain Regulatory Interface: Compliance nodes can verify the legality of fund flows and service content without disclosing commercial privacy.

• Cross-Border Payment Transparency: The Signal DAG inherently carries geographical, temporal, and payee information, providing data basis for multinational taxation and anti-money laundering.

Value and Impact

1. Cash Flow Acceleration: Enterprise AI services upgrade from "monthly reconciliation, quarterly payment" to "settlement upon delivery," significantly reducing working capital pressure.

2. Default Cost Minimization: Both parties use locked funds + SLA proof mechanisms to avoid defaults, greatly reducing cooperation thresholds and legal disputes.

3. Interoperable Ecosystem: AI agents from different industries, blockchains, or Web2 systems can interconnect through standardized Signal interfaces.

4. Audit-Friendly: All key steps leave verifiable fingerprints under Bitcoin's finality, meeting compliance requirements such as SOX, GDPR, ISO, etc.

Cross-Institution Collaboration: Signal-based settlements between enterprise AI agents transform traditional "paper contracts + offline reconciliation" into "smart signals + instant clearing," allowing cross-company and cross-border AI services to interconnect securely like microservices, automatically price against each other, and quickly cash out.

# Conclusion

## Technical Summary

In the overall architecture of the B² Network, Signal serves as the "nerve fiber" that connects everything. It integrates previously fragmented processes such as on-chain transactions, off-chain computations, data verification, and incentive distribution into a traceable, composable, and governable event stream. By generating the smallest granularity of Signal for each important action, the platform achieves an atomic transaction model of "state—signature—proof—settlement," inherently possessing capabilities for retroactive tracing, auditing, and automated governance.

The core technology stack can be summarized into three layers:

1. Trusted Execution Layer

• B² Rollup + B² Hub provide a scalable execution environment anchored to the Bitcoin L1 chain, ensuring that transactions and computations have PoW finality;

• The zk-Commitment mechanism uses zero-knowledge batch proofs to compress massive Signals, reducing L1 load while retaining a complete security proof chain.

2. Data and Value Flow Layer (Signal & Settlement Layer)

• Signal Shard adopts an event DAG storage model, with each Signal carrying a hash pointer, timestamp, and verifiable metadata;

• The multi-asset settlement gateway supports USD2, BTC, sats (Lightning), and future on-chain derivative assets, dynamically routing to the optimal settlement path;

• ParameterOracle + delayed voting ensure that system parameters (staking rate, fee rate, risk control thresholds) can be transparently adjusted on-chain while preventing flash governance attacks.

3. Intelligent Autonomy Layer (AI & Governance Layer)

• The AI Agent SDK encapsulates Signal primitives as strategy hooks, allowing scenarios such as mining, arbitrage, data verification, and enterprise collaboration to be orchestrated by a unified API;

• The RL-Tuner framework enables each Agent to self-learn and adapt while ensuring returns and risk constraints;

• GNN anomaly detection + graylist promptly identify malicious behaviors and feed back into consensus security through "signal points—staking—forfeiture."

Connecting the three layers is a closed loop of "trusted data -> programmable incentives -> automated governance":

The original events are written into the Signal DAG at a low cost, and after being batched by zk, they are settled on Bitcoin; AI Agents and smart contracts read these highly credible events, make timely decisions, and generate new incentives and governance signals in reverse. This continuous iteration endows the B² Network with three characteristics: high security, strong scalability, and flexible governance.

In summary, B² Network uses the finality of Bitcoin as its foundation, expands throughput through zero-knowledge and event-driven mechanisms, and unleashes automation potential through AI-native signal orchestration, delivering a set of infrastructure for the Web3 ecosystem that balances security, performance, and composability:

• For developers: a one-time integration that provides on-chain certainty while enabling off-chain high-performance computing;

• For users: funds, data, and computing power flow freely under the same signal semantics, offering an experience similar to Web2 but with on-chain security;

• For governors: every system parameter and every profit distribution is verifiable on-chain, allowing the community to make upgrade decisions based on facts rather than guesses.

This embodies the technical vision of "signals as the lifeblood, Bitcoin as the heart"—ensuring that every heartbeat of decentralized applications is precise, measurable, and self-consistent.

## Economic and Ecological Outlook

As the Signal-Driven architecture is fully rolled out, the economy and ecology of B² Network will present several clear growth curves that are coupled and mutually accelerating—continuing the long-term appreciation logic of Bitcoin's "hard assets" while releasing the high-turnover cash flow brought by AI automation.

1. Capital Efficiency Curve: BTC -> Stablecoin -> High-Frequency Returns -> Staking Compound Interest

• BTC collateralized stablecoins solve the dilemma of "holding + liquidity." Holders can release purchasing power without reducing their positions, and the circulation of stablecoins expands in tandem with BTC's market value.

• AI Agent high-frequency strategies (mining, arbitrage, market making, computing power leasing) convert stablecoins into intraday or minute-level income streams.

• The staking and re-staking mechanism deposits returns back to the base layer, forming a compound interest "snowball." The collateral pool thickens over time, further raising the system's security threshold.

2. Behavior-Driven Curve: Signal Generation -> Data Network Effects -> Platform Externalities

• Every transaction, call, and verification will mint new Signals, becoming combinable "atomic" events.

• The larger the signal DAG, the richer the AI Agent's trainable behavior space, leading to diverse strategies and a surge in long-tail scenarios.

• With external developers and enterprises connecting, the network exhibits typical bilateral platform externalities:

• More Agents -> More Signals -> Higher Data Entropy -> More Precise Strategies -> Higher Returns -> Attracting More Agents.

• More enterprise collaboration -> Richer services -> Stronger settlement depth -> More robust liquidity -> Attracting More Enterprises.

3. Fees and Value Capture: Multidimensional, Programmable, Progressive

• Base Gas Fee: Rollup packaging, Hub Checkpoint, providing sustainable "L1 data rent" for Bitcoin.

• Signal Toll: Fine-grained rates can be inserted into stages such as uploading, verifying, challenging, and calling, supporting dynamic adjustments.

• Composable Incentives: Governance can return part of the fees to key ecosystem roles (oracles, validators, developers), creating a "negative friction" experience— the more active users are, the lower the actual net cost.

• Value-Added Services: Custodial nodes, MPC wallets, privacy computing, dedicated bandwidth, and other advanced services can be layered on demand, forming a secondary income curve.

4. Governance Evolution: Gradual Parameters, Reputation Weighting, AI Assistance

• Initially, key parameters (collateral rate, penalties, fee rate curve) are set by the core governance DAO;

• As ReputationScore and Signal points accumulate, voting rights for parameters will gradually shift to high-reputation entities;

• AI-Governor will use GNN and RL-Tuner to simulate governance data scenarios, propose automated parameter adjustment suggestions, and then quickly execute them through community voting, achieving self-optimization.

5. Industry Linkage: From On-Chain Finance to Real-World Assets

• The data market will attract traditional data vendors and research institutions to tokenize RWA data such as health, climate, and logistics;

• Enterprise collaboration settlements will connect SaaS, industrial IoT, and energy trading, giving rise to a signal-based Machine-as-a-Service model;

• BTC collateral and liquidity pools provide a low-threshold dollar alternative for global offshore funds, becoming the underlying channel for cross-border payments and supply chain finance.

6. Long-Term Vision: Signals Become a "Liquid Value" Metric

When signal density is sufficiently high and covers a wide range of economic activities, the B² Network is expected to evolve into an "economic operating system":

• Every value exchange automatically carries proof and incentives;

• Every Agent behavior is instantly mapped to the ledger and governance;

• Every protocol upgrade is data-driven, risk-controlled, and completed through community consensus.

In this system, BTC is no longer just a static reserve asset but continuously "flows" and generates compound returns through collateral, the Lightning Network, and signal clearing; AI Agents become autonomous nodes that capture and amplify these returns, collectively driving a safe, transparent, and rapidly growing diverse economy.

In short, the economic and ecological landscape of the B² Network is an upward curve jointly drawn by Bitcoin's security endorsement, signal-driven liquidity, AI automatic value addition, and community self-consistent governance—it inherits the scarcity and censorship resistance of BTC while injecting the era's momentum of fully programmable Web3 and high-efficiency AI, ultimately pointing towards a more open, trustworthy, and resilient digital civilization foundation.

## Community Action Call: Building the "AI Holds BTC" Future

Imagine a not-so-distant tomorrow:

• Mining farms are no longer just power factories, but operate self-learning mining agents that schedule power by the second and convert earnings into programmable stablecoins in real-time;

• Traders and market makers capture cross-chain price differences through one-click deployed strategy agents, automatically funneling net profits back into the staking pool;

• Data creators write every sensor reading and every frame of imagery into verifiable Signals, protecting privacy while providing fuel for the AI training market;

• Enterprise applications call external AI agents like invoking microservices, delivering instant settlement and seamless global collaboration 24/7;

• Ordinary holders only need to hold BTC to continuously generate USD2 in the background, participate in PoSg governance, and share in the network's growth dividends.

Whether this vision can be realized depends on you—the developers, miners, investors, researchers, or curious individuals reading this text. Here are the immediate action paths you can take:

1. Run a node and become a guardian of Signals

• Deploy a B² Hub light client or full node to provide additional validation and relay bandwidth for the Signal DAG.

• Participate in ParameterOracle and delayed voting to help the network iterate quickly on a decentralized basis.

2. Build and share AI agents

• Use the AI Agent SDK to create custom strategies: mining scheduling, arbitrage market making, enterprise SaaS, IoT predictions...

• Publish agents to the Signal Marketplace, providing plug-and-play AI capabilities for other users and earning revenue shares based on usage.

3. Contribute data to ignite the training flywheel

• Package your high-quality images, on-chain interactions, financial data, etc., into DataSignals on-chain to earn DataCredits.

• Stake and validate others' data as a Data Validator, earning validation rewards while enhancing market credibility.

4. Provide liquidity and act as the "central bank" of the network

• Collateralize BTC to generate USD2, or provide liquidity to the USD2/BTC pool, earning stability fees and mining incentives.

• Delegate staking to PoSg validators, earning network rewards while gaining governance influence.

5. Participate in governance and shape the rules

• Regularly review governance proposals and vote using your B² Tokens, Signal points, or ReputationScore.

• Utilize the AI-Governor simulator to propose parameter improvements based on real data through Pull Requests, making governance decisions more forward-looking.

6. Spread the idea and build consensus

• Write articles, podcasts, or short videos about the value proposition of "AI Holds BTC";

• Share your usage experiences and best practices in developer communities, hackathons, and industry summits;

• Invite traditional enterprises and academic institutions to explore new paradigms like Machine-as-a-Service and RWA data on-chain, broadening the boundaries together.

Conclusion: Why take action now?

Sixteen years after Bitcoin's birth, its role as a "store of value" is deeply ingrained, but the liquidity and productivity of value still seem insufficient. The mission of the B² Network is to use Signal-Driven AI to upgrade BTC from a static "digital gold" to a dynamic "economic energy unit":

Gold provides anchoring, signals provide speed, and AI provides intelligence.

As more people, more computing power, and more data are integrated into this closed loop, the network will self-expand, self-repair, and self-appreciate like breathing, ultimately nurturing a new frontier of AI × Bitcoin where everyone can participate and benefit.

So, let’s take action together—run the first node, deploy the first agent, upload the first batch of data, cast the first governance vote.

Let today’s small step accumulate into a future of decentralized intelligent civilization.

# References

Academic Papers & Research

[1] Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. https://bitcoin.org/bitcoin.pdf

[2] Wood, G. (2014). Ethereum: A secure decentralised generalised transaction ledger. https://ethereum.github.io/yellowpaper/paper.pdf

[3] Buterin, V. (2021). An Incomplete Guide to Rollups. https://vitalik.ca/general/2021/01/05/rollup.html

[4] Komlo, C., & Goldberg, I. (2020). FROST: Flexible round-optimized Schnorr threshold signatures. https://eprint.iacr.org/2020/852.pdf
Bitcoin Layer 2 & Scaling

[5] Poon, J., & Dryja, T. (2016). The bitcoin lightning network: Scalable off-chain instant payments. https://lightning.network/lightning-network-paper.pdf

[6] Somsen, R. (2021). BitVM: Compute anything on Bitcoin. https://bitvm.org/bitvm.pdf

[7] Celestia Labs. (2023). Celestia: A modular consensus and data availability layer. https://celestia.org/

AI & Blockchain Integration

[8] Fetch.ai. (2022). Autonomous Economic Agents: Combining AI and blockchain for decentralized systems. https://fetch.ai/whitepaper

[9] Bittensor. (2023). A Peer-to-Peer Intelligence Market. https://bittensor.com/whitepaper

Consensus Mechanisms

[10] Buchman, E. (2016). Tendermint: Byzantine fault tolerance in the age of blockchains. https://tendermint.com/static/docs/tendermint.pdf

[11] Boneh, D., Drijvers, M., & Neven, G. (2018). Compact multi-signatures for smaller blockchains. https://crypto.stanford.edu/~dabo/pubs/papers/BLSmultisig.html

Zero-Knowledge Proofs

[12] Ben-Sasson, E., Bentov, I., Horesh, Y., & Riabzev, M. (2018). Scalable, transparent, and post-quantum secure computational integrity. https://eprint.iacr.org/2018/046.pdf

[13] Groth, J. (2016). On the size of pairing-based non-interactive arguments. https://eprint.iacr.org/2016/260.pdf

[14] Gabizon, A., Williamson, Z. J., & Ciobotaru, O. (2019). PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge. https://eprint.iacr.org/2019/953.pdf

Stablecoins & DeFi

[15] Maker Foundation. (2020). The Maker Protocol: MakerDAO's Multi-Collateral Dai (MCD) System. https://makerdao.com/whitepaper

[16] Curve Finance. (2020). StableSwap - efficient mechanism for Stablecoin liquidity. https://curve.fi/files/stableswap-paper.pdf

[17] Frax Finance. (2023). Frax Protocol Documentation. https://docs.frax.finance/

Machine Learning & Reinforcement Learning

[18] Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. http://incompleteideas.net/book/the-book-2nd.html

[19] Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal policy optimization algorithms. https://arxiv.org/abs/1707.06347

Privacy & Security

[20] Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf

[21] Kosba, A., Miller, A., Shi, E., Wen, Z., & Papamanthou, C. (2016). Hawk: The blockchain model of cryptography and privacy-preserving smart contracts. https://eprint.iacr.org/2015/675.pdf

Data Availability & Storage

[22] Srinivasan, S., Chitra, U., & Bhat, S. (2023). Data availability sampling and sub-sampling for light clients. https://arxiv.org/abs/2301.10785

Industry Reports & Standards

[23] Bank for International Settlements. (2023). The future monetary system. BIS Annual Economic Report. https://www.bis.org/publ/arpdf/ar2023e.htm

[24] World Economic Forum. (2024). Navigating the AI Revolution: Insights and Strategies. https://www.weforum.org/reports/

B² Network Documentation

[25] B² Network Team. (2024). B² Network Technical Documentation. https://docs.bsquared.network/

[26] B² Network Team. (2024). B² Hub: DA Layer on Bitcoin. https://blog.bsquared.network/b²-hub-da-layer-on-bitcoin-fa63d52b8926

[27] B² Network Team. (2024). B² DSN-AI: Decentralized AI Infrastructure. https://docs.bsquared.network/b2_dsn_ai

[28] B² Network GitHub Repository. (2024). https://github.com/b2network/

Related Projects

[29] Lightning Network Specification. https://github.com/lightning/bolts

[30] Cosmos SDK Documentation. https://docs.cosmos.network/

[31] Polygon zkEVM Documentation. https://wiki.polygon.technology/docs/zkevm/

[32] Arbitrum One Portal. https://developer.arbitrum.io/

[33] Optimism Documentation. https://docs.optimism.io/