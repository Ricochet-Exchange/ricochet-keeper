
from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import ERC20_ABI

class ERC20BalanceOfOperator(ContractInteractionOperator):
    template_fields = ["account"]
    ui_color = "#BC9EC1"

    @apply_defaults
    def __init__(self,
                 account,
                 *args,
                 **kwargs):
        super().__init__(abi_json=ERC20_ABI, *args, **kwargs)
        self.account = account

    def execute(self, context):
        self.initContract()
        self.function = self.contract.functions.balanceOf
        return self.function(self.account).call()
