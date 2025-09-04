# B² Hub (Layer 1.5 PoSg Consensus)

## Overview
B² Hub serves as the **Layer 1.5 consensus backbone** of the B² Network, bridging Bitcoin’s Proof-of-Work finality with AI-driven Proof-of-Signal + Stake (PoSg).
It is designed to combine the **security of Bitcoin anchoring**, the **scalability of application sharding**, and the **intelligence of AI signals** into a unified infrastructure.

---

## Core Principles
- **Proof-of-Signal + Stake (PoSg):**
  Validators secure the Hub by staking BTC and receiving delegated **signals** from AI Agents and users.
  Voting power = Staked BTC × SignalScore, ensuring that **economic capital and intelligent activity jointly drive consensus**.

- **Application Sharding:**
  The Hub introduces multiple shards, such as:
  - **Signal Shard**: Collects and verifies signals from DSN-AI.
  - **Agent Shard**: Executes agent-native contracts and interactions.
  - **Stablecoin Shard**: Handles U2 minting, redemption, and settlements.
  This separation ensures high throughput and modular scalability.

- **Bitcoin Anchoring:**
  Finalized states and validator commitments are periodically written to Bitcoin’s Taproot via inscription transactions.
  This creates an **immutable audit trail** and inherits Bitcoin’s Proof-of-Work finality.

---

## Technical Design

### 1. Validator Lifecycle
- **Staking:** Validators bond BTC into the Hub to participate in consensus.
- **Signal Delegation:** AI Agents and users delegate signals to validators, weighted by trust and performance.
- **Epoch Rotation:** At each epoch, validator sets are updated via **FROST-DKG key resharing**, ensuring cryptographic robustness.
- **Reward Distribution:** Rewards are paid in BTC and U2, sourced from Mining² revenue routing and network fees.

### 2. Consensus Mechanics
- **CometBFT PBFT Engine:**
  The Hub runs a modified CometBFT engine, where PoSg determines voting power.
- **Byzantine Detection:**
  Graph Neural Networks (GNN) monitor validator behavior and detect anomalies (double-signing, equivocation, censorship).
- **Finality:**
  Hub blocks achieve instant BFT finality, while anchoring to Bitcoin provides long-term economic immutability.

### 3. Signal Integration
- **SignalScore:**
  A composite metric representing the volume, diversity, and reliability of signals delegated to a validator.
- **Weighting Formula:**
  $$
    \text{SignalScore}_v = \sum_{\text{agent} \in \mathcal{D}_v} \sum_{\text{sig} \in \mathcal{W}} \text{weight}
  $$
- **Impact:**
  Signals allow AI Agents to actively influence consensus, aligning network governance with intelligent activity.

---

## Applications of B² Hub
- **AI-Driven Governance:** Agents collectively steer validator voting power through their delegated signals.
- **BTC Settlement Backbone:** Provides high-throughput consensus while anchoring to Bitcoin for security.
- **Ecosystem Aggregator:** Serves as the coordination layer for Rollup execution, stablecoin issuance, and signal propagation.
- **Agent Economy Enablement:** Establishes a trustless environment where AI Agents transact and settle in BTC and U2 natively.

---

## Key Benefits
- **Hybrid Security:** Combines PoW anchoring with PoSg consensus for maximum resilience.
- **AI-Native Consensus:** Signals transform AI activity into measurable economic weight.
- **Modular Scalability:** Application sharding allows specialization and parallel execution.
- **Economic Finality:** Anchoring to Bitcoin guarantees irreversible settlement.

---

**B² Hub is the heart of the network — a consensus engine where Bitcoin, AI signals, and stablecoin economics converge.**