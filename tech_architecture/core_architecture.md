# Core Architecture

B² Network is designed as a **modular Bitcoin + AI settlement infrastructure**, enabling the vision of
**“Put Bitcoin in Every AI’s Wallet.”**

The architecture is built around **five tightly connected modules**, each solving a key challenge in unifying Bitcoin, AI Agents, and Stablecoin economies:

1. **Mining² (DeFAI-Mining Router)**
   Connects Bitcoin miners to the network by routing hashrate and BTC revenues into staking pools, agent wallets, and validator incentives.
   It bridges Proof-of-Work security with Proof-of-Signal governance.

2. **B² Hub (Layer 1.5 PoSg Consensus)**
   A sovereign “Layer 1.5” chain powered by Proof-of-Signal + Stake (PoSg).
   - Signals from AI agents and delegators determine validator voting power.
   - Application sharding separates Signal, Agent, and Stablecoin execution environments.
   - Anchors finality to Bitcoin via Taproot inscriptions for global security.

3. **B² Rollup (BTC-Anchored L2 Execution Layer)**
   An EVM-compatible rollup environment with high throughput and native BTC-denominated gas.
   - Aggregates transactions, zk/fraud proofs, and data commitments.
   - Posts merkle roots and proofs to Bitcoin for trustless anchoring.
   - Enables developers to deploy dApps and smart contracts with BTC settlement.

4. **DSN-AI (Signal-Driven Agentic AI Layer)**
   The protocol layer that integrates autonomous AI agents directly into blockchain consensus.
   - Agents emit verifiable “signals” representing perception, planning, and actions.
   - Validators use signals to adjust voting power via SignalScore.
   - Provides Agent-Native Abstraction Accounts (A-AA), enabling agents to hold and transact in BTC or U2 natively.

5. **U2 Stablecoin (BTC-Collateralized Settlement Layer)**
   A Bitcoin-backed stablecoin designed for micro-payments and predictable pricing.
   - Over-collateralized by BTC with hedging strategies for peg stability.
   - Used by agents for task payments, settlements, and long-term contracts.
   - Serves as the stable economic medium for the AI-driven ecosystem.

![B² Network Architecture](https://github.com/user-attachments/assets/43babba0-f08c-4621-a16e-e1efb30218d7)

---

## Architectural Flow

- **From Mining to AI**: BTC mined by Mining² flows into validators and agents, securing the Hub.
- **From Agents to Consensus**: AI signals are aggregated into the Hub’s PoSg consensus, shaping governance and execution.
- **From Rollup to Bitcoin**: Transactions and proofs are rolled up and anchored to Bitcoin for ultimate settlement finality.
- **From BTC to Stability**: U2 stablecoin ensures agents and users transact with predictable value.

Together, these modules form a **closed economic and technical loop**:
BTC → Signals → Consensus → Rollup Execution → U2 Stablecoin → AI Economy → back to BTC.

This architecture transforms Bitcoin from a passive store of value into the **active settlement currency of the AI era**.
