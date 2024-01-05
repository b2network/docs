# B² account abstraction sdk

## Getting started

- Add following content to .npmrc:

```bash
@b2network:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=<REPLACE WITH YOUR PERSONAL ACCESS TOKEN WITH PACKAGE READ PERM>
```

- Then install the package with:

```bash
yarn add @b2network/aa-sdk
```

- Refer to [b2-account-infra](https://github.com/b2network/b2-account-infra) repo to collect deployed contract addresses 

### Basic Usage with viem

```ts
import { SimpleWeightedECDSAProvider, SmartAccountSigner } from '@b2network/aa-sdk';
import { type WalletClient, type Chain, type Hex, hexToBigInt, keccak256, concatHex } from "viem";

const convertWalletClientToAccountSigner = (
  client: WalletClient
): SmartAccountSigner => {
  return {
    async getAddress() {
      return Promise.resolve((await client.getAddresses())[0] as `0x${string}`)
    },
    async signMessage(message: Uint8Array | Hex | string) {
      const sig = await client.signMessage({
        account: client.account!,
        message:
          typeof message === 'string'
            ? message
            : {
                raw: message,
              },
      })
      return concatHex(['0x00', sig])
    },
    async signTypedData(params: SignTypedDataParams) {
      const sig = await client.signTypedData({
        ...params,
        account: client.account!,
      })
      return concatHex(['0x00', sig])
    },
  }
}

const selectedSigner = convertWalletClientToAccountSigner(signer)
const ownerHash = keccak256(
  Buffer.from((await selectedSigner.getAddress()).toLowerCase(), "utf-8")
);

const provider = SimpleWeightedECDSAProvider.init({
  projectId: "0",
  selectedSigner,
  guardians: ['0x7d25AF0015dB2625a5560b3914565FcD7AE49C78'],
  ids: ['0x0000000000000000000000000000000000000000000000000000000000000000'],
  weights: [1],
  threshold: 1,
  opts: {
    providerConfig: {
      chain,
      rpcUrl: BUNDLER_RPC_URL,
      entryPointAddress: ENTRYPOINT_ADDRESS,
      opts: {
        txRetryMulitplier: 1,
        txRetryIntervalMs: 3000,
      }
    },
    accountConfig: {
      entryPointAddress: ENTRYPOINT_ADDRESS,
      factoryAddress: KERNEL_FACTORY_ADDRESS,
      implAddress: KERNEL_IMPL_ADDRESS,
      index: hexToBigInt(ownerHash),
    },
    validatorConfig: {
      entryPointAddress: ENTRYPOINT_ADDRESS,
      validatorAddress: SW_VALIDATOR_ADDRESS,
    },
    paymasterConfig: {
      policy: "VERIFYING_PAYMASTER",
      baseURL: PM_BASE_URL,
    }
  },
})

const { hash } = await provider.sendUserOperation({
  target: "0xtarget",
  data: "0xcallData",
  value: 0n
});

await provider.waitForUserOperationTransaction(
  result.hash as Hex
);
```

### Batch Transactions

```ts
const { hash } = await provider.sendUserOperation([
  {
    target: "0xtarget1",
    data: "0xcallData1",
    value: 0n,
  },
  {
    target: "0xtarget2",
    data: "0xcallData2",
    value: 0n,
  },
]);
```

## Components

### Core Components

The primary interfaces are the `ZeroDevProvider`, `KernelSmartContractAccount` and `KernelBaseValidator`

The `ZeroDevProvider` is an ERC-1193 compliant Provider built on top of Alchemy's `SmartAccountProvider`

1. `sendUserOperation` -- this takes in `target`, `callData`, and an optional `value` which then constructs a UserOperation (UO), sends it, and returns the `hash` of the UO. It handles estimating gas, fetching fee data, (optionally) requesting paymasterAndData, and lastly signing. This is done via a middleware stack that runs in a specific order. The middleware order is `getDummyPaymasterData` => `estimateGas` => `getFeeData` => `getPaymasterAndData`. The paymaster fields are set to `0x` by default. They can be changed using `provider.withPaymasterMiddleware`.
2. `sendTransaction` -- this takes in a traditional Transaction Request object which then gets converted into a UO. Currently, the only data being used from the Transaction Request object is `from`, `to`, `data` and `value`. Support for other fields is coming soon.

`KernelSmartContractAccount` is Kernel's implementation of `BaseSmartContractAccount`. The following methods are implemented:

1. `getDummySignature` -- this method should return a signature that will not `revert` during validation. It does not have to pass validation, just not cause the contract to revert. This is required for gas estimation so that the gas estimate are accurate.
2. `encodeExecute` -- this method should return the abi encoded function data for a call to your contract's `execute` method
3. `encodeExecuteDelegate` -- this method should return the abi encoded function data for a `delegate` call to your contract's `execute` method
4. `signMessage` -- used to sign messages
5. `signTypedData` -- used to sign typed data
6. `signMessageWith6492` -- like `signMessage` but supports ERC-6492
7. `signTypedDataWith6492` -- like `signTypedData` but supports ERC-6492
8. `getAccountInitCode` -- this should return the init code that will be used to create an account if one does not exist. Usually this is the concatenation of the account's factory address and the abi encoded function data of the account factory's `createAccount` method.

The `KernelBaseValidator` is a plugin that modify how transactions are validated. It allows for extension and implementation of arbitrary validation logic. It implements 3 main methods:

1. `getAddress` -- this returns the address of the validator
2. `getOwner` -- this returns the eligible signer's address for the active smart wallet
3. `getSignature` -- this method signs the userop hash using signer object and then concats additional params based on validator mode.

### Adding new custom validator plugin

1. Create a new validator class that extends `KernelBaseValidator` similar to [`ECDSAValidator`](`packages/accounts/src/kernel-zerodev/validator/ecdsa-validator.ts`).

2. Make sure to pass the `validatorAddress` of your validator to the `KernelBaseValidator` base class.

3. Create a new validator provider that extends `ValidatorProvider` similar to [`ECDSAValidatorProvider`](`packages/accounts/src/kernel-zerodev/validator-provider/ecdsa-provider.ts`).

4. Use the newly created validator provider as per above examples.

#### `KernelBaseValidator` methods to be implemented in your validator class

- `signer()` -- this method should return the signer as per your validator's implementation. For example, for Multi-Signature validator, this method should return one of the owner signer which is connected to the multisig wallet contract and currently using the DAPP.
- `getOwner()` -- this method should return the address of the signer. For example, for Multi-Signature validator, this method should return the address of the signer which is connected to the multisig wallet contract and currently using the DAPP.
- `getEnableData()` -- this method should return the bytes data for the `enable` method of your validator contract. For example, in ECDSA validator, this method returns `owner` address as bytes data. This method is used to enable the validator for the first time while creating the account wallet.
- `encodeEnable(enableData: Hex)` -- this method should return the abi encoded function data for the `enable` method of your validator contract. For example, in ECDSA validator, this method returns the abi encoded function data for the `enable` method with owner address as bytes param.
- `encodeDisable(disableData: Hex)` -- this method should return the abi encoded function data for the `disable` method of your validator contract. For example, in ECDSA validator, this method returns the abi encoded function data for the `disable` method with empty bytes param since ECDSA Validator doesn't require any param.
- `signMessage(message: Uint8Array | string | Hex)` -- this method should return the signature of the message using the connected signer.
- `signUserOp(userOp: UserOperationRequest)` -- this method should return the signature of the userOp hash using the connected signer.