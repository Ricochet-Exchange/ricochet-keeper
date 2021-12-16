from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator


ERC20_ABI = '''[{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},
{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]
'''

class ERC20ApprovalOperator(ContractInteractionOperator):

    template_fields = ['spender', 'amount']
    ui_color = "#BC9EC1"

    @apply_defaults
    def __init__(self,
                 spender,
                 amount,
                 *args,
                 **kwargs):
        self.spender = spender
        self.amount = amount
        super().__init__(abi_json=ERC20_ABI, *args, **kwargs)

    def execute(self, context):
        # Check if the approve should use the max balance
        if int(self.amount) < 0:
            self.amount = self.contract.functions.balanceOf(self.wallet.public_address).call()
        # Setup args for ContractInteractionOperator's execute method
        self.function_args = {"spender": self.spender, "amount": int(self.amount)}
        self.function = self.contract.functions.approve
        super().execute(context)
