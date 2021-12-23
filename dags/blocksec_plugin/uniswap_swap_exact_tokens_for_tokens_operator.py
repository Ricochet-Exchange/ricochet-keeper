from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import UNISWAP_ROUTER_ABI
from time import time
import requests

class UniswapSwapExactTokensForTokensOperator(ContractInteractionOperator):
    """
    Calls `swapExactTokensForTokens` on a Uniswap Router contract
    * Assumes amount of tokens has been approved already
    """
    template_fields = ['amount_in', 'amount_out_min', 'path', 'to']
    ui_color = "#EBBAB9"

    @apply_defaults
    def __init__(self,
                 amount_in=0,
                 amount_out_min=0,
                 path=[],
                 to=None,
                 deadline=None,
                 slippage=0.005,
                 *args,
                 **kwargs):
        super().__init__(abi_json=UNISWAP_ROUTER_ABI, *args, **kwargs)
        self.amount_in = amount_in
        self.amount_out_min = amount_out_min
        self.path = path
        self.to = to
        if not deadline:
            self.deadline = time() + 300
        else:
            self.deadline = deadline

    def execute(self, context):
        # Calulate min out:
        in_price = self.get_coingecko_price(self.path[0])
        out_price = self.get_coingecko_price(self.path[-1])

        self.amount * in_price / out_price * (1 - self.slippage)

        self.function = self.contract.functions.swapExactTokensForTokens
        self.function_args = {
            "amountIn": int(self.amount_in),
            "amountOutMin": int(self.amount_out_min),
            "path": self.path,
            "to": self.to,
            "deadline": int(self.deadline)
        }
        return super().execute(context)

    def get_coingecko_price(self, address):
        url = f"https://api.coingecko.com/api/v3/simple/token_price/polygon-pos?contract_addresses={address}&vs_currencies=usd"
        response = requests.get(url)
        result = response.json()
        return result[lower(address)]["usd"]
