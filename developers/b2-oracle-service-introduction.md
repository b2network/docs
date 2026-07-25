# B2 Oracle Service

B2 Oracle Service is a decentralized, multi-signature price oracle running on [B2 Network](https://www.bsquared.network/) (a Bitcoin Layer 2). It publishes BTC/USD price data on-chain and exposes it through **two industry-standard interfaces**, so existing integrations work without code changes:

- **Chainlink-compatible** — the standard `AggregatorV3Interface` (drop-in for any protocol built against Chainlink feeds)
- **Supra-compatible** — the `ISupraSValueFeed` push-model interface (drop-in for any protocol built against Supra)

## How It Works

```
  ┌──────────────────────────────────────────────────────────────┐
  │                        DeFi Protocols                        │
  └───────────────┬─────────────────────────────┬────────────────┘
                  │ AggregatorV3Interface       │ ISupraSValueFeed
                  ▼                             ▼
  ┌───────────────────────────┐   ┌───────────────────────────┐
  │      AggregatorProxy      │◀──│    SupraSValueAdapter     │
  │  stable integration addr  │   │  read-only Supra facade   │
  └───────────────┬───────────┘   └───────────────────────────┘
                  ▼
  ┌───────────────────────────┐
  │      OracleAggregator     │  ← verifies ≥3-of-4 signer ECDSA
  │  bounds, replay & fresh-  │    signatures before storing a
  │  ness protection          │    new price round
  └───────────────▲───────────┘
                  │ transmit(report, signatures)
  ┌───────────────┴───────────┐
  │        Coordinator        │  ← polls prices, triggers updates,
  └──┬───────┬───────┬───────┬┘    collects signatures, pays gas
     ▼       ▼       ▼       ▼
  Signer1 Signer2 Signer3 Signer4   ← 4 independent verifiers,
     └───────┴───┬───┴───────┘        each holds its own key
                 ▼
   Binance / OKX / Coinbase / Kraken (public market data)
```

### Data pipeline

1. **Aggregation.** An off-chain coordinator continuously polls multiple centralized exchanges (Binance, OKX, Coinbase, Kraken) and computes the **median** price, tolerant to any single source failing or misreporting.
2. **Update triggers.** A new price is pushed on-chain when either the price **deviates beyond a configured threshold** from the last on-chain value, or a **heartbeat interval** expires — so the feed tracks volatile markets closely while proving liveness in quiet ones.
3. **Independent multi-party verification.** Before anything goes on-chain, the coordinator must collect signatures from independent signer services. Each signer **fetches exchange prices itself**, recomputes the median, and only signs if the proposed price is within its own tolerance. The coordinator never holds signer keys; signers never see each other's keys.
4. **On-chain verification.** The `OracleAggregator` contract accepts a new round only if it carries valid ECDSA signatures from **at least 3 of the 4 authorized signers** (threshold and signer set are on-chain state, rotatable by the owner). Forging a price requires compromising 3 independent parties simultaneously.

### On-chain safeguards

- **Price bounds** — each aggregator is deployed with immutable `minAnswer`/`maxAnswer`; out-of-range prices are rejected even with valid signatures.
- **Replay protection** — every signature binds to a `feedId = keccak256(chainId, aggregator, description, configEpoch)`. Signatures cannot be replayed across chains, contracts, or signer-set rotations (each rotation bumps `configEpoch`, instantly invalidating all outstanding signatures).
- **Freshness & monotonicity** — round IDs and observation timestamps must be strictly increasing; timestamps more than 300 s in the future are rejected.
- **Safe upgrades** — consumers integrate against a proxy whose address never changes. The underlying aggregator can be replaced through a two-step propose/confirm process (with phase-encoded round IDs, mirroring Chainlink's `EACAggregatorProxy`), and all admin roles use two-step ownership transfer.

## Contract Addresses (B2 Mainnet, chainId 223)

| Feed | Interface | Address |
|---|---|---|
| BTC / USD | Chainlink `AggregatorV3Interface` | `0x3031EC46cb223dAF943FFDbCbDDE0374036E8a7f` |
| uBTC / USD | Chainlink `AggregatorV3Interface` | `0xae06f38b576A921C768Afb172dc6fC6B88495D65` |
| BTC / USD | Supra `ISupraSValueFeed` | `0x76bc00D4C3BfBfC6ABb2cb018df0125a2Ad26767` |
| uBTC / USD | Supra `ISupraSValueFeed` | `0xB9C787b2fAA8eECFC9E6a602d41D968f32fcc6F5` |

uBTC (1:1 BTC-pegged) is served through its own proxy backed by the same BTC/USD feed, so protocols can configure it like any independent feed.

## Developer Guide

### Option A: Chainlink-style integration

The proxy addresses above are drop-in replacements for a Chainlink price feed:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface AggregatorV3Interface {
    function decimals() external view returns (uint8);
    function latestRoundData()
        external view
        returns (uint80 roundId, int256 answer, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound);
}

contract Example {
    AggregatorV3Interface constant BTC_USD =
        AggregatorV3Interface(0x3031EC46cb223dAF943FFDbCbDDE0374036E8a7f);

    function btcPrice() external view returns (int256 price) {
        (, price,, uint256 updatedAt,) = BTC_USD.latestRoundData();
        require(block.timestamp - updatedAt < 3600, "stale price"); // always check freshness
    }
}
```

- `decimals()` is always **8** — e.g. $64,043.055 is returned as `6404305500000`
- `answer` is the USD price as a fixed-point integer
- `startedAt` = off-chain observation time, `updatedAt` = on-chain write time
- `roundId` is encoded as `(phaseId << 64) | aggregatorRoundId`, identical to Chainlink's proxy format

Quick check from the command line:

```bash
cast call 0x3031EC46cb223dAF943FFDbCbDDE0374036E8a7f \
  "latestRoundData()(uint80,int256,uint256,uint256,uint80)" \
  --rpc-url https://rpc.bsquared.network
```

### Option B: Supra-style integration

If your protocol already consumes Supra's push oracle, point it at the Supra-compatible address instead — pair indexes, return struct, and decimal conventions all follow Supra's catalog:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

interface ISupraSValueFeed {
    struct priceFeed { uint256 round; uint256 decimals; uint256 time; uint256 price; }
    function getSvalue(uint256 _pairIndex) external view returns (priceFeed memory);
    function getSvalues(uint256[] memory _pairIndexes) external view returns (priceFeed[] memory);
}

contract Example {
    ISupraSValueFeed constant FEED =
        ISupraSValueFeed(0x76bc00D4C3BfBfC6ABb2cb018df0125a2Ad26767);

    function btcPrice() external view returns (uint256 price, uint256 decimals) {
        ISupraSValueFeed.priceFeed memory f = FEED.getSvalue(18); // 18 = BTC_USD
        require(block.timestamp * 1000 - f.time < 3600 * 1000, "stale price");
        return (f.price, f.decimals); // read decimals dynamically — it varies per pair
    }
}
```

Registered pair indexes (Supra's official numbering):

| Pair index | Supra pair | Decimals | Available on |
|---|---|---|---|
| `0` | BTC_USDT | 18 | both Supra-compatible contracts |
| `18` | BTC_USD | 8 | both Supra-compatible contracts |

- `time` is a **millisecond** timestamp
- USDT-quoted pairs are served from the USD feed (USDT ≈ USD, deviation typically ~0.1%)

```bash
cast call 0x76bc00D4C3BfBfC6ABb2cb018df0125a2Ad26767 \
  "getSvalue(uint256)((uint256,uint256,uint256,uint256))" 18 \
  --rpc-url https://rpc.bsquared.network
# → (round, 8, 1784949600000, 6404305500000)   i.e. $64,043.055
```

Differences from Supra's official contracts (intentional):

1. **Unregistered pairs revert** with `"pair not registered"` instead of returning an all-zero struct — a zero price can silently poison liquidation logic.
2. `round` is the underlying proxy round ID (monotonically increasing `uint256`); Supra's is timestamp-shaped. Treat it as an opaque increasing value.
3. Updates are typically **fresher** than Supra's native push feed on B2 (which refreshes on a 10% deviation / 6-hour schedule).

### Integration checklist

- Always enforce a staleness check against `updatedAt` (Chainlink-style) or `time` (Supra-style); pick a window consistent with the feed's heartbeat.
- Integrate the **proxy / adapter addresses** listed above — never the underlying aggregator, whose address changes on upgrades.
- For Supra-style reads, take `decimals` from the returned struct rather than hardcoding it: it differs per pair (8 vs 18).
