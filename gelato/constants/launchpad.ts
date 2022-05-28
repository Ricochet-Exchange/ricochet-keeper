/* eslint-disable @typescript-eslint/naming-convention */
// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export const getLaunchpadsByNetwork = (network: string) => {
    switch (network) {
      case "matic":
        return {
          GELATO: "0x7598e84B2E114AB62CAB288CE5f7d5f6bad35BbA",
          GELATO_RELAY: "0x837F0BB41d8cA7b051408aD312767e016622ed0b",
          GELATO_RELAY_TRANSIT: "0xE2Fc8F14B6cEb1AD8165623E02953eDB100288bE",
          LAUNCHPADS: {"RIC": "0x98d463A3F29F259E67176482eB15107F364c7E18"},
          ETH: "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", // MATIC
        };
      default: {
        throw new Error(`Launchpads: network: ${network} not supported`);
      }
    }
  };
  