import hre from "hardhat";
import { Interface } from "ethers/lib/utils";
import { RelaySDK } from "@gelatonetwork/relay-sdk";
import launchPadABI from "../contracts/abis/rexLaunchpad.json";
import { getLaunchpadsByNetwork } from "../constants/launchpad";
import { BigNumber, Contract } from "ethers/lib/ethers";

async function main() {
  const { LAUNCHPADS, ETH, GELATO_RELAY_TRANSIT } = getLaunchpadsByNetwork(hre.network.name);

  // Verify that current network is supported by Gelato Multichain Relay
  const chainId = hre.network.config.chainId ?? 0;
  const isChainSupported = await RelaySDK.isChainSupported(chainId);
  if (!isChainSupported) {
    console.log("ChainId not supported");
    return;
  }

  // loop over all launchpads
  for (const launchpadAddress of LAUNCHPADS) {

    // Estimate gas limit for our helloWorld call
    const launchpad = new Contract(launchpadAddress, launchPadABI, hre.ethers.provider);
    const gasLimit: BigNumber = await launchpad
      .connect(GELATO_RELAY_TRANSIT) // Gelato relay transit will be our contract caller
      .estimateGas.distribute();

    // Estimate the fees to pay to the relayer for the given gas limit
    const estimatedFees: BigNumber = await RelaySDK.getEstimatedFee(
      chainId,
      ETH,
      gasLimit,
      false // Set to true for high priority fees
    );

    // Encode our function call
    const data = launchpad.interface.encodeFunctionData("distribute", [
      estimatedFees,
      ETH,
    ]);

    // Send our tx to Gelato Relay
    console.log(`Sending launchpad tx to Gelato Relay...`);
    const relayTx = await RelaySDK.sendRelayTransaction(
      chainId,
      launchpadAddress, // Smart contract address
      data,
      ETH, // Payment token address
      estimatedFees
    );
    console.log(`RelayTransaction Id: ${relayTx.taskId}`);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
