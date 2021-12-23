from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import UNISWAP_ROUTER_ABI, ERC20
from time import time

class UniswapSwapExactTokensForETHOperator(ContractInteractionOperator):
    """
    Calls `swapExactTokensForETH` on a Uniswap Router contract
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
        if int(self.amount_in) < 0:
            # Max swap
            input_token = self.web3.eth.contract(self.path[0], abi=ERC20_ABI)
            self.amount_in = input_token.functions.balanceOf(self.wallet.public_address).call()

        self.function = self.contract.functions.swapExactTokensForETH
        self.function_args = {
            "amountIn": int(self.amount_in),
            "amountOutMin": int(self.amount_out_min),
            "path": self.path,
            "to": self.to,
            "deadline": int(self.deadline)
        }
        return super().execute(context)
