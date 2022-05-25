import { HardhatUserConfig } from "hardhat/config";

// PLUGINS
import "@nomiclabs/hardhat-waffle";
import "@nomiclabs/hardhat-ethers";

// Process Env Variables
import * as dotenv from "dotenv";
dotenv.config({ path: __dirname + "/.env" });

const ALCHEMY_ID = process.env.ALCHEMY_ID ?? "";

const config: HardhatUserConfig = {
  defaultNetwork: "ropsten",

  networks: {

    matic: {
      chainId: 137,
      url: `https://polygon-mainnet.g.alchemy.com/v2/${ALCHEMY_ID}`,
    },
    boba: {
      chainId: 288,
      url: `https://mainnet.boba.network`,
    },
  },

  solidity: {
    compilers: [
      {
        version: "0.8.7",
        settings: {
          optimizer: { enabled: true, runs: 200 },
        },
      },
    ],
  },
};

export default config;
