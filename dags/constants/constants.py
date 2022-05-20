from datetime import datetime, timedelta


class PriceConstants:
    # Gas
    MAX_GAS_PRICE_DEFAULT = 33
    KEEPER_FUNDS_THRESHOLD = 1
    GAS_DEFAULT = 3000000
    GAS_MULTIPLIER_DEFAULT = 1.1
    GAS_MULTIPLIER_SWAP = 1.2
    GAS_MULTIPLIER_STREAM_CLOSURE = 10

    # Swap
    RIC_DCA_SWAP_AMOUNT = 100000000
    SWAP_SLIPPAGE = 0.005


class ScheduleConstants:
    ETHEREUM_BLOCK_POLL = "*/15 * * * *"
    RICOCHET_DCA = "0 * * * *"
    RICOCHET_DISTRIBUTE_V2 = "0 * * * *"
    RICOCHET_DISTRIBUTE = "0 * * * *"
    RICOCHET_HARVEST = "0 * * * *"
    RICOCHET_REFILL = "0 * * * *"
    RICOCHET_STREAM_CLOSURE = None
    RICOCHET_STREAM_WATCH = "50 * * * *"
    RICOCHET_TELLOR_REPORTER = "*/5 * * * *"


class AddressConstants:
    SUSHI_V2_ROUTER_02 = "0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506"
    TELLOR_CONTRACT = "0xACC2d27400029904919ea54fFc0b18Bf07C57875"
    RIC_TOKEN = "0x263026E7e53DBFDce5ae55Ade22493f828922965"
    USDC_TOKEN = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
    WMATIC_TOKEN = "0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270"
    USDCx_TOKEN = "0xCAa7349CEA390F89641fe306D93591f87595dc1F"


class Utils:

    DAG_ARGS_DEFAULT = {
        "owner": "ricochet",
        "depends_on_past": False,
        "start_date": datetime(2020, 3, 29),
        "email": ["mike@mikeghen.com"],
        "email_on_failure": True,
        "email_on_retry": False,
        "retries": 0,
        "retry_delay": timedelta(minutes=1),
    }

    def get_DAG_args(**kwargs):
        args = Utils.DAG_ARGS_DEFAULT.copy()
        args.update(kwargs)
        return args
