
import hre from "hardhat";
import { getMarketsByNetwork } from "../constants/market";
import { GelatoOpsSDK, isGelatoOpsSupported, TaskReceipt } from "@gelatonetwork/ops-sdk";
import { Contract } from "ethers";
import marketABI from "../contracts/abis/rexMarket.json";

// TODO: Use gelato ops to create a new task and send it to the relayer 

async function main() {
  const { MARKETS, ETH, GELATO_RELAY_TRANSIT } = getMarketsByNetwork(hre.network.name);

  const chainId = hre.network.config.chainId ?? 0;
  if (!isGelatoOpsSupported(chainId)) {
    console.log(`Gelato Ops network not supported (${chainId})`);
    return;
  }

  // Init GelatoOpsSDK
  const [signer] = await hre.ethers.getSigners();
  const gelatoOps = new GelatoOpsSDK(chainId, signer);

  // loop over all markets key values
  for (const [marketName, marketAddress] of Object.entries(MARKETS)) {

    // Prepare Task data to automate
    const market = new Contract(marketAddress, marketABI, signer);
    const priceSelector = market.interface.getSighash("updateTokenPrices()");
    const execPriceData = market.interface.encodeFunctionData("updateTokenPrices");

    // Create price update task
    console.log(`Creating ${marketName} price task...`);
    const updatePriceTask: TaskReceipt = await gelatoOps.createTask({
      execAddress: marketAddress,
      execSelector: priceSelector,
      execAbi: JSON.stringify(marketABI),
      execData: execPriceData,
      name: `${marketName} price update`,
      interval: 3600, // Seconds
    });
    console.log(`${marketName} price task created, taskId: ${updatePriceTask.taskId})`);
    console.log(`> https://app.gelato.network/task/${updatePriceTask.taskId}?chainId=${chainId}`);

    // Prepare distribute task data to automate
    const distributeSelector = market.interface.getSighash("distribute(bytes ctx)");
    const execDistributeData = market.interface.encodeFunctionData("distribute", ["0x"]);

    // Create distribute task
    console.log(`Creating ${marketName} distribute task...`);
    const distributeTask: TaskReceipt = await gelatoOps.createTask({
      execAddress: marketAddress,
      execSelector: distributeSelector,
      execAbi: JSON.stringify(marketABI),
      execData: execDistributeData,
      name: `${marketName} distribute`,
      interval: 3600, // Seconds
    });
    console.log(`${marketName} distribute task created, taskId: ${distributeTask.taskId})`);
    console.log(`> https://app.gelato.network/task/${distributeTask.taskId}?chainId=${chainId}`);
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
