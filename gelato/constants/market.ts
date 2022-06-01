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
//             "MATIC_DAI": "0xcaB28480ab5c1E133e9B7FC67E030B8DCC2A1d24",
//             "MATIC_USDC": "0x87588653F2F840Bf0589d5715679Db77d8fC021d",
//             "WBTC_DAI": "0xE0073786618b886aA1aa44Df103850a227ADe9ae",
            "WBTC_USDC": "0x3c0AEA5B1A16352dEd8aBaB513477AFa3a70c484",
            "ETH_DAI": "0xB44B371A56cE0245ee961BB8b4a22568e3D32874",
            "ETH_USDC": "0xF1748222B08193273fd34FF10A28352A2C25Adb0",
            "RIC_USDC": "0x86c2B55bf5d3E9DAC2747389B38D41C6B1F34179"
        },
          ETH: "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", // MATIC
        };
      default: {
        throw new Error(`Launchpads: network: ${network} not supported`);
      }
    }
  };
  
