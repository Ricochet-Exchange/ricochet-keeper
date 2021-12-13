
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import ERC20_ABI_BALANCE

class ERC20BalanceOfOperator(ContractInteractionOperator):
    template_fields = ["account"]
    ui_color = "#BC9EC1"

    @apply_defaults
    def __init__(self,
                 account,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.account = account
        self.function_args = {"account": self.account}
        self.function = self.contract.functions.balanceOf