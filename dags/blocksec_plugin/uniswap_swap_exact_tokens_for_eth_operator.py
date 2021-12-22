from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import SWAP_ABI
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
                 router_address=None,
                 amount_in=0,
                 amount_out_min=0,
                 path=[],
                 to=None,
                 deadline=None,
                 *args,
                 **kwargs):
        super().__init__(*args,
                        **kwargs)
        self.router_address = router_address
        self.amount_in = amount_in
        self.amount_out_min = amount_out_min
        self.path = path
        self.to = to
        if not deadline:
            self.deadline = time() + 300
        else:
            self.deadline = deadline
        self.abi_json = SWAP_ABI
        self.function = self.contract.functions.swapExactTokensForEth

    def execute(self, context):
        self.function_args = {
            "amountIn": int(self.amount_in),
            "amountOutMin": int(self.amount_out_min),
            "path": self.path,
            "to": self.to,
            "deadline": self.deadline
        }
        return super().execute(context)
