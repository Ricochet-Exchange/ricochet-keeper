from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import ERC20_ABI_APPROVE


class ERC20ApprovalOperator(ContractInteractionOperator):
    """
    Calls `distribute` on Ricochet contracts
    """
    template_fields = ['spender', 'amount']
    ui_color = "#BC9EC1"

    @apply_defaults
    def __init__(self,
                 spender,
                 amount,
                 *args,
                 **kwargs):
        super().__init__(*args,
                        **kwargs)
        self.spender = spender
        self.amount = amount
        self.abi_json = ERC20_ABI_APPROVE
        # Verify if max balance is needed
        if int(self.amount) < 0:
            self.amount = self.contract.functions.balanceOf(self.wallet.public_address).call()
        self.argsForFunction = {"spender": self.spender, "amount": int(self.amount)}
        self.function = self.contract.funtions.approve
