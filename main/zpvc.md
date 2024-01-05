# Zero-Knowledge Proof Verification Commitment for ZK-Rollup on Bitcoin

B² Network is a Layer 2 solution on Bitcoin, primarily utilizing zero-knowledge proof verification commitments submitted to Bitcoin. It allows challengers to initiate fraud proofs for disputes, aiming to leverage the powerful consensus of Bitcoin to ensure the security of the B² Network.

This article mainly introduces the operating mechanisms of ZK-Rollup and OP-Rollup on Ethereum, explores the marvelous NAND gate circuit, and discusses the role of commitments. Utilizing these mechanisms and concepts, we design the zero-knowledge proof verification commitments for the B² Network. Furthermore, we explain how these commitments are executed on Bitcoin and how they ensure the security of the B² Network.

## ZK-Rollup on Ethereum

ZK-Rollup is a Layer 2 scaling solution for blockchains that aggregates multiple transactions and utilizes zero-knowledge proofs to ensure the correctness and completeness of these transaction batches. It verifies zero-knowledge proofs on the Layer 1 blockchain network, thus leveraging the Layer 1 network to ensure the security of the Layer 2 network. It aims to increase the throughput of blockchain systems, reduce transaction costs, and maintain a high level of security and data integrity.

The operation process of ZK-Rollup is roughly as follows:
- Transaction Aggregation and Ordering: Users submit transactions to ZK-Rollup, which are then added to a mempool. The ZK-Rollup Sequencer retrieves transactions from the mempool and performs aggregation and ordering. The Sequencer is responsible for processing transactions, updating account states, and ultimately generating a batch representing these updates.
- State Transition and Computation: All transactions and state updates are performed off-chain. ZK-Rollup's Virtual Machine (including various zero-knowledge proof smart contract execution engines like zkEVM, zkVM, etc.) computes new account states and handles operations such as transfers and smart contract interactions. It also generates necessary data and evidence to prove that these transactions and state updates are valid, including new account states and zero-knowledge proofs.
- Zero-Knowledge Proof Generation: ZK-Rollup's Prover uses zero-knowledge proof technology (such as zk-SNARKs or zk-STARKs) to create a proof that all aggregated transactions are valid and do not violate network rules. This proof protects user privacy and ensures data integrity and security without revealing any information about the transaction contents.
- Zero-Knowledge Proof Verification: The Aggregator submits the batch's data and zero-knowledge proof to the Layer 1 blockchain network. This is usually done in a compressed form to reduce the required on-chain space. Smart contracts on the Layer 1 blockchain network receive this data and proof and verify its validity. If the proof is valid, the contract will update the state recorded by the ZK-Rollup layer.

The core of ZK-Rollup lies in the generation and verification of zero-knowledge proofs. Transactions in ZK-Rollup are executed off-chain, and states are generated off-chain. The Prover generates a zero-knowledge proof as a commitment to ZK-Rollup. This commitment represents the correct and valid execution of transactions on ZK-Rollup, leading to the correct state. The Layer 1 blockchain network does not need to verify all transactions and states of ZK-Rollup, only the commitment. The verification of the commitment is done through the Layer 1 network's smart contracts by verifying the zero-knowledge proof, thus confirming the validity of ZK-Rollup.

Therefore, in Ethereum's ZK-Rollup, the zero-knowledge proof data is the commitment submitted by the Layer 2 network to the Layer 1 network.

## OP-Rollup on Ethereum

Optimistic Rollup (OP-Rollup) is a technology designed to scale blockchain performance by maintaining minimal data on-chain and performing as many computations off-chain as possible. OP-Rollup utilizes an 'optimistic' assumption that most transactions are honest, instead of immediately verifying the validity of each transaction. This allows for validation to occur after a certain period, greatly increasing throughput and efficiency.

The operation process of OP-Rollup is roughly as follows:
- Transaction Aggregation and Ordering: Users submit transactions to OP-Rollup, which are then added to a mempool. The OP-Rollup Sequencer retrieves transactions from the mempool and performs aggregation and ordering. The Sequencer is responsible for processing transactions, updating account states, and ultimately generating a batch representing these updates.
- Transaction Execution: Transactions within OP-Rollup are executed off-chain. The execution of each batch of transactions leads to a transition from an old state to a new state. Each batch calculates a new state root (an encrypted 'snapshot' representing the entire system state) and submits it to the Layer 1 blockchain network.
- State Verification: OP-Rollup does not immediately perform complex verification when submitting transaction batches. Instead, it 'optimistically' assumes these transactions are valid and then submits them to the Layer 1 blockchain network. If any observer believes a batch is invalid, they can submit a fraud proof to challenge the batch. In the Optimistic Rollup solution, fraud proofs are mechanisms that allow any observer to challenge incorrect or maliciously submitted states or transactions on the chain. Optimistic Rollup uses fraud proofs to ensure that even 'optimistically' accepted transactions can be proven wrong afterward and accordingly revoked.
- Challenge Mechanism: There is a challenge window period after OP-Rollup submits the state confirmation. During this period, anyone can check the submitted batch and submit a fraud proof if they find errors. This is usually achieved by submitting a transaction to the Layer 1 blockchain network, declaring their perceived error and providing corresponding evidence. Arbitrum Rollup (a type of Optimistic Rollup solution) uses a process known as the 'interactive verification game' to resolve challenges. In this process, challengers and submitters engage in a series of rounds, gradually narrowing down their disagreement on where the error occurred (using a binary search method to quickly locate the transaction position of the error). Eventually, this process will determine the exact location of the error. Once an error is confirmed, the original batch will be revoked, and penalties will be imposed on the verifier who raised the error. If the challenge fails, the challenger might lose the funds they staked to initiate the challenge; if the challenge is successful, the challenger can receive the reward funds for successfully initiating the challenge.

The core of OP-Rollup lies in the fraud proof and challenge mechanism. OP-Rollup initially 'optimistically' assumes that all transactions are executed correctly, and then compiles the computations into bytecode for a virtual machine within the contract (such as AVM or OVM) on the Layer 1 network, publishing a commitment to this bytecode. The commitment verification of OP-Rollup requires performing transaction computations and obtaining the bytecode, followed by the verification of the commitment. Once an observer detects a batch with mismatching commitments, they will generate a fraud proof through the challenge mechanism and receive a reward.

Ethereum's OP-Rollup first 'optimistically' confirms and submits commitments, then utilizes the challenge mechanism, allowing anyone to challenge the submitted commitments. Ultimately, commitments and challenges ensure that OP-Rollup is verified and confirmed.

## Magical NAND Gate Circuit

The NAND gate is a fundamental logic gate in digital logic that implements a logical NOT operation following a logical AND operation. The characteristics of the NAND gate make it the foundation for constructing any other logic gate and complex logic circuits. Below is a detailed introduction to how NAND gates can be used to construct logic gates (such as AND, OR, XOR gates) as well as addition and subtraction gates.

### NAND Gate Basics
The NAND gate has two inputs and produces an output of 0 only when both inputs are 1; in all other cases, the output is 1. This can be represented by the logical expression A NAND B.

### Constructing Basic Logic Gates

#### AND Gate（AND）
To construct an AND gate using NAND gates:
1. Step 1: Connect the two inputs to a NAND gate.
2. Step 2: Connect the output of this NAND gate to both inputs of another NAND gate.
3. Result: The output of the second NAND gate is the result of the AND gate.

#### OR Gate（OR）
To construct an OR gate using NAND gates:
1. Step 1: Pass each input through a NAND gate (with itself), producing the effect of two NOT gates.
2. Step 2: Connect these two NAND gates' outputs as inputs to another NAND gate.
3. Result: The output of this NAND gate is the result of the OR gate.

#### XOR Gate（XOR）
To construct an XOR gate (more complex) using NAND gates:
1. Step 1: Construct two NAND gates, each input connected to one.
2. Step 2: Connect the outputs of the first step's NAND gates to the input of a third NAND gate.
3. Step 3: Connect the original input A and the output of the first NAND gate to a fourth NAND gate, and the original input B and the output of the second NAND gate to a fifth NAND gate.
4. Step 4: Finally, connect the outputs of the fourth and fifth NAND gates to a sixth NAND gate.
5. Result: The output of the sixth NAND gate is the result of the XOR gate.


### Constructing Addition Gates

#### Half Adder
A half adder is a simple adder that can handle the addition of two bits, producing a sum and a carry.
1. Sum: Use an XOR gate to generate the sum.
2. Carry: Use an AND gate to generate the carry.
3. Construct these basic gates using NAND gates, then combine them to form a half adder.

#### Full Adder
A full adder considers the carry input from a lower bit.
1. Step 1: Construct two half adders; the first deals with A and B, the second with the sum of the first half adder and carry input C.
2. Sum: The sum output of the second half adder.
3. Carry: The carry outputs of the two half adders are connected through an OR gate.
4. Construct half adders and an OR gate using NAND gates, then combine them to form a full adder.

### Constructing Subtraction Gates

#### Half Subtractor
A half subtractor deals with the subtraction of two bits.
1. Difference: Use an XOR gate to generate the difference.
2. Borrow: Use a NAND gate and a NOT gate to generate the borrow.
3. Construct an XOR gate and other required logic using NAND gates, then combine them to form a half subtractor.

#### Full Subtractor
A full subtractor considers the borrow from a higher bit.
1. Step 1: Construct two half subtractors, the first dealing with A and B, the second with the difference of the first half subtractor and borrow input.
2. Difference: The difference output of the second half subtractor.
3. Borrow: The borrow outputs of the two half subtractors are connected through an OR gate.
4. Construct half subtractors and an OR gate using NAND gates, then combine them to form a full subtractor.

### Constructing Multiplication Gates

#### Binary Multiplication
Implement the multiplication of two binary numbers.
1. Step 1: Use AND gates for bit multiplication.
2. Step 2: Use a series of full adders for continuous addition.
3. Step 3: Implement shifting and accumulation.

### Constructing Registers

#### D Flip-Flop
Stores a single bit of binary information.
1. Step 1: Use NAND gates to create a latch.
2. Step 2: Expand the latch into a flip-flop.

#### Register
Stores multiple bits of binary information.
- Connect multiple D flip-flops in parallel, each storing one bit.

### Constructing Clocks

#### Oscillator
Provides periodic clock signals.
- Use NAND gates to create a feedback loop, producing continuous oscillation.

### Conclusion

The NAND gate is known as a 'universal logic gate' due to its ability to construct any other logic gate and complex circuits. Through the methods described above, the NAND gate can be utilized to build complex addition, subtraction, multiplication, as well as storage and clock circuits, which are the basis for arithmetic operations in computers and digital systems. In modern integrated circuit design, the NAND gate is widely used due to its simplicity and versatility.

In the practice of B² Network, any computational logic can be constructed using NAND gates.

## Commitment

Commitments have a wide range of applications in cryptography and blockchain, such as SHA256, Merkle Trees, and KZG in zero-knowledge proofs, all of which are forms of commitments. As introduced earlier, ZK-Rollup uses zero-knowledge proofs as the commitment for the Rollup, while OP-Rollup uses the bytecode within the virtual machine as the Rollup's commitment.

We can explain in detail how commitments are used through the example of a Merkle Tree:
- Commit: The Prover calculates the hash of all values, with the hashes serving as the leaves of a binary tree. The Prover then continually computes hashes upwards until the Merkle Tree is generated, and the tree root hash is published as the commitment.
- Reveal: The Prover reveals a value corresponding to a leaf node and its branch.
- Check: The Verifier calculates the hash using the revealed value and branch, and then compares it with the published commitment for verification.

For instance, in the following diagram:
- Commit: The Prover calculates the hash of transactions tx1, tx2...tx8, obtaining H(1), H(2)...H(8), and continually performs hash calculations pairwise to finally generate the binary tree structure shown in the diagram, which is the Merkle Tree. The Prover then publishes the root node value H(12345678) of the Merkle Tree as the commitment.
- Reveal: The Prover reveals a leaf node's corresponding value, such as tx3, along with its branch (H(4) -> H(12) -> H(5678)).
- Check: The Verifier calculates and verifies the commitment using the revealed tx3 and branch (H(4) -> H(12) -> H(5678)):
    1. Calculate the hash of tx3, H(3).
    2. Hash H(3) with H(4) from the branch to get H(34).
    3. Hash H(34) with H(12) from the branch to get H(1234).
    4. Hash H(1234) with H(5678) from the branch to get H(12345678).
    5. Compare H(12345678) with the published commitment for verification.

![Merkle tree proof](https://ipfs.io/ipfs/QmWZunnonmhrSoSTDpEFjGBrUKywDo3GpoYgnPrKcp4BSs)


## ZK Proof Verification Commitment of B² Network

**B² Network is a ZK-Rollup Layer 2 solution built on Bitcoin.**

### Limit of Bitcoin ZK-Rollup

Due to the Turing incompleteness of Bitcoin, it's not possible to perform zero-knowledge proof verification on Bitcoin. Therefore, the traditional approach of ZK-Rollup solutions, where zero-knowledge proofs are verified on a Layer 1 blockchain network, cannot be implemented on Bitcoin.

ZK-Rollup only writes the zero-knowledge proofs and the aggregated data of the Rollup into Bitcoin through Taproot. This ensures that the data of ZK-Rollup is anchored in Bitcoin and cannot be tampered with. However, it does not guarantee the validity and correctness of the transactions within the ZK-Rollup, nor can it utilize the powerful consensus capabilities of Bitcoin to ensure the security of the Layer 2 ZK-Rollup.

Therefore, it is necessary to confirm ZK-Rollup on Bitcoin.

### ZK Proof and Arithmetic Circuit

#### ZK Proof

In zero-knowledge proofs, arithmetic circuits are used to construct a proof that the prover knows certain secret information without revealing the information itself.

Zero-knowledge proofs use arithmetic circuits to generate a proof:
- Generating the Proof:
    - Once the arithmetic circuit is established, the prover uses their secret inputs to compute the circuit's output. During this process, the prover also generates additional information (such as commitments and random numbers unique to zero-knowledge proofs), which are used to construct the proof.
- Verifying the Proof:
    - The prover sends their proof to the verifier. The verifier does not know the prover's secret inputs but has a description of the circuit and the prover's proof. The verifier validates the proof's authenticity by performing the same computations as the circuit and comparing its results with the proof provided by the prover.

#### Arithmetic Circuit

Arithmetic circuits are typically represented as a directed acyclic graph (DAG), where each node represents an arithmetic operation and the edges represent the flow of data between operations. Input nodes represent the inputs to the circuit, typically some numbers or variables, while internal nodes represent arithmetic operations. The output of the circuit is the final result of the computation.

Basic gates in arithmetic circuits include:
- Addition Gate (Addition Gate): Performs addition operations.
- Multiplication Gate (Multiplication Gate): Performs multiplication operations.

As introduced earlier with NAND gates, arithmetic circuits can be converted into logic gate circuits based on NAND gates by transforming addition gates into NAND gates and multiplication gates into NAND gates, ultimately translating the entire arithmetic circuit into a circuit based on NAND gate logic.

### ZK Proof Verification Commitment

The verification procedure for zero-knowledge proofs itself is an arithmetic circuit, which can be converted into a logic gate circuit based on NAND gates. This effectively translates the zero-knowledge proof verification procedure into a logic gate circuit based on NAND gates.

NAND gates are implemented via Bitcoin script, assembling Bit Value Commitment as inputs and outputs into logic gates to enforce logical constraints.

This can be succinctly represented as *==<hash_c0> <hash_c1> <hash_b0> <hash_b1> <hash_a0> <hash_a1> OP_GATECOMMITMENT==*, with the corresponding unlocking script being *==<preimage_a> <preimage_b> <preimage_c>==*.

In practice, NAND gates can be implemented through Bitcoin script, and from these NAND gates, addition and multiplication gates can be constructed. These addition and multiplication gates are then combined into an arithmetic circuit to ultimately build the zero-knowledge proof verification procedure. However, due to the vast number of gate circuits involved, the resulting Bitcoin script is also quite large and impractical to run on the Bitcoin network.

By assembling Bit Value Commitment as inputs and outputs into logic gates, each logic gate with different inputs and outputs acts as a leaf node, forming a circuit binary tree. The published Circuit Taproot is the root of this binary tree, reducing the size of the published data.

Circuit Taproot serves as the commitment for the B² Rollup submitted on the Layer 1 blockchain network, Bitcoin. Unlike traditional ZK-Rollups that can perform validation on the Layer 1 network, B² Rollup cannot directly execute validation on Bitcoin. However, an Optimistic Rollup-like approach can be adopted, providing a challenge mechanism for the commitment. The confirmation of the Circuit Taproot commitment is completed through this challenge mechanism.

## Challenges and Responses

Unlike BitVM, which requires pre-signing off-chain transactions between two parties, the B² Network adopts the publishing of UTXO transactions that lock a reward. The unlocking script is a Taproot script.

The specific unlocking Taproot script involves the Prover generating scripts for each branch of the Circuit Taproot Tree in advance, along with the given hash inputs. Challengers can execute the script using a preimage. If the output of the execution is inconsistent with the Prover's submission, they can unlock the entire Taproot using MAST (Merkelized Abstract Syntax Tree) to claim the locked reward.

Due to the small running cost and speed of the zero-knowledge verification procedure, all users on the Bitcoin network can act as observers for the Challenge mechanism, verifying the commitments submitted by B² Rollup. If an inconsistency in the commitment is discovered, they can immediately initiate a challenge.

The challenge mechanism is similar to Arbitrum Rollup's 'interactive verification game,' continuously searching for incorrectly executed logic gate computations. To find the erroneous gate among many, a binary search method is used to execute the gate circuit Bitcoin script. The challenger who finds the erroneous branch fastest can unlock the UTXO with the locked reward on the Bitcoin network and thus receive the reward.

Additionally, one branch of the Taproot locking script is a time-lock script. If no successful challenges occur, the Prover can unlock the UTXO and retrieve the reward after the challenge period ends, using the time-lock script.


## Summary

B² Network, through the Ordinals Protocol, aggregates the rollup's data and proof and writes them into Tapscript. It utilizes various decentralized storage protocols to save the detailed rollup data, effectively ensuring the data availability of the rollup.

B² Network records the zero-knowledge proof verification commitment on Bitcoin, allowing any observer to challenge the commitment. This mechanism enables the inheritance of Bitcoin's security, reaching consensus on the rollup's data on the Bitcoin network.
