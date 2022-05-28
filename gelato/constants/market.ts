/* eslint-disable @typescript-eslint/naming-convention */
// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export const getMarketsByNetwork = (network: string) => {
    switch (network) {
      case "matic":
        return {
          GELATO: "0x7598e84B2E114AB62CAB288CE5f7d5f6bad35BbA",
          GELATO_RELAY: "0x837F0BB41d8cA7b051408aD312767e016622ed0b",
          GELATO_RELAY_TRANSIT: "0xE2Fc8F14B6cEb1AD8165623E02953eDB100288bE",
          MARKETS: {
            "MATIC_DAI": "0xcaB28480ab5c1E133e9B7FC67E030B8DCC2A1d24",
            "MATIC_USDC": "0x87588653F2F840Bf0589d5715679Db77d8fC021d",
            "WBTC_DAI": "0xE0073786618b886aA1aa44Df103850a227ADe9ae",
            "WBTC_USDC": "0xef2C9e8777648d7Dea03b319c64EA53f38EC1398",
            "ETH_DAI": "0x5970Acd9e2Cb09089FE61f4D0fEc1ae0E959bbDe",
            "ETH_USDC": "0xD83321984CF13b47b84D2b2939EC286c8d08714d"
        },
          ETH: "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", // MATIC
        };
      default: {
        throw new Error(`Launchpads: network: ${network} not supported`);
      }
    }
  };
  