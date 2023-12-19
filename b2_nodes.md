# B² Nodes

B² Nodes act as off-chain validators and are executors of multiple distinctive features in B² Network. B² Nodes consist of six main modules: ZK Proof Verifier of Rollup Module, ZK Proof Verifier of Storage Module, Sequencer Selector Module, Bitcoin Indexer Module, Bitcoin Committer Module, and Validator Set Module.

## ZK Proof Verifier of Rollup Module

B² Nodes obtain rollup transactions data from Decentralized Storage and rollup transaction merkle tree root hash and zk proof data from the Aggregator of the Rollup Layer. First, within the ZK Proof Verifier of Rollup Module, the merkle tree root hash is used to check if the rollup transactions stored in Decentralized Storage have been tampered with. Then, the zk proof data is used to verify whether the rollup transactions have been executed correctly and effectively.

## ZK Proof Verifier of Storage Module

In the ZK Proof Verifier of Storage Module, B² Nodes validate the zk proof of storage submitted by the Storage Nodes of Decentralized Storage. Once the verification is passed, B² Nodes distribute rewards to the Storage Nodes, incentivizing them to store copies of rollup data over the long term.

## Sequencer Selector Module

In the Sequencer Selector Module, B² Network implements a mechanism similar to Delegated Proof of Stake (DPoS), selecting a group of sequencers. These sequencers sequentially provide transaction ordering and packaging services for a specified period. Individuals or organizations wishing to compete as a sequencer must stake a certain amount of $BSQ and prepare the necessary hardware resources to run the sequencer service. Users can also delegate their $BSQ to candidates competing for a sequencer position. Ultimately, the top N candidates with the highest total staked and delegated $BSQ become the sequencer set for a period. Operating a sequencer service earns a certain percentage of transaction fees and additional $BSQ rewards. 

## Bitcoin Indexer Module

The Bitcoin Indexer monitors blocks and transactions on the Bitcoin network. Upon obtaining the latest blocks and transactions, it generates zero-knowledge proofs for these blocks and transactions to ensure the accuracy of transaction information. The Bitcoin Indexer then sends the transactions and corresponding zk proofs to the Rollup Layer. When the zkEVM receives the Bitcoin transactions and zk proofs, it verifies them and generates the Bitcoin State. (See in Figure [B² Network Bitcoin Indexer](https://ipfs.io/ipfs/QmcfJr9KrqiN19iPFgeaabSgHV9oQgQdxCDTAcL3BgrLbc))

![B² Network Bitcoin Indexer](https://ipfs.io/ipfs/QmcfJr9KrqiN19iPFgeaabSgHV9oQgQdxCDTAcL3BgrLbc)

## Bitcoin Committer Module

The Bitcoin Committer sends two types of transactions to Bitcoin: one that writes rollup data into Bitcoin, and another that writes the zk proof verification commitment into Bitcoin.

- The Bitcoin Committer constructs a data structure to record B² rollup data and generates a Tapscript, known as a "B² Inscription." Then, the Bitcoin Committer sends a UTXO of one satoshi unit to a Taproot address containing the $B^{2}$ inscription. The rollup data is permanently written into Bitcoin. (See in Figure [Data availablity in B² Network](https://ipfs.io/ipfs/Qma2tcFRFA78cDNLDTZJzpa4fDWHR4TKGptc5Q6qpsS4yT))

![Data availablity in B² Network](https://ipfs.io/ipfs/Qma2tcFRFA78cDNLDTZJzpa4fDWHR4TKGptc5Q6qpsS4yT)

- The Bitcoin Committer breaks down large computational units from the ZK Proof Verifier of Rollup Module into smaller computational units. Each small computational unit is then turned into a bit value commitment and placed in a tapleaf script. The zk proof of rollup serves as the input for the first bit value commitment, with the output being the input for the next commitment, eventually forming a taproot. The Bitcoin Committer sends a UTXO of one satoshi unit to a Taproot address containing the commitment. The commitment based on zk proof verification is permanently written into Bitcoin. Additionally, the Bitcoin Committer sets a time-locked challenge, allowing challengers to contest the zk proof verification commitment. If there are no challengers or the challenge fails within the time lock, the rollup is finally confirmed on Bitcoin; if the challenge succeeds, the rollup is rolled back. (See in Figure [Commitment in B² Network](https://ipfs.io/ipfs/QmUSxP47LiQ1PaddAiCHw1SuKHwNVXe9KPi3Ta7JLXurEc))

![Commitment in B² Network](https://ipfs.io/ipfs/QmUSxP47LiQ1PaddAiCHw1SuKHwNVXe9KPi3Ta7JLXurEc)

## Validator Set Module

The Validator Set Module maintains members of the Schnorr signature on Bitcoin Layer1.