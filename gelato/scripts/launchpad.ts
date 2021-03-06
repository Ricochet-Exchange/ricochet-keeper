
import hre from "hardhat";
import { getLaunchpadsByNetwork } from "../constants/launchpad";
import { GelatoOpsSDK, isGelatoOpsSupported, TaskReceipt } from "@gelatonetwork/ops-sdk";
import { Contract } from "ethers";
import launchPadABI from "../contracts/abis/rexLaunchpad.json";

// TODO: Use gelato ops to create a new task and send it to the relayer 

async function main() {
  const { LAUNCHPADS, ETH, GELATO_RELAY_TRANSIT } = getLaunchpadsByNetwork(hre.network.name);

  const chainId = hre.network.config.chainId ?? 0;
  if (!isGelatoOpsSupported(chainId)) {
    console.log(`Gelato Ops network not supported (${chainId})`);
    return;
  }

  // Init GelatoOpsSDK
  const [signer] = await hre.ethers.getSigners();
  const gelatoOps = new GelatoOpsSDK(chainId, signer);

  // loop over all launchpads key values
  for (const [launchpadName, launchpadAddress] of Object.entries(LAUNCHPADS)) {

    // Prepare Task data to automate
    const counter = new Contract(launchpadAddress, launchPadABI, signer);
    const selector = counter.interface.getSighash("distribute()");
    const execData = counter.interface.encodeFunctionData("distribute");

    // Create task
    console.log("Creating Task...");
    
    // Create try catch block to catch any errors
    try {
      const task: TaskReceipt = await gelatoOps.createTask({
        execAddress: launchpadAddress,
        execSelector: selector,
        execAbi: JSON.stringify(launchPadABI),
        execData: execData,
        name: `${launchpadName} distribute`,
        interval: 3600, // Seconds
      });
      console.log(`Task created, taskId: ${task.taskId})`);
      console.log(`> https://app.gelato.network/task/${task.taskId}?chainId=${chainId}`);
    } catch (error) {
      console.log(`Error: ${launchpadName} launchpad might already exist.`);
    }
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
