from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import RICOCHET_ABI


class RicochetStreamerCloseOperator(ContractInteractionOperator):
    """
    Closes a streamers stream using `closeStream`
    """
    template_fields = ['streamer_address', 'exchange_address']

    @apply_defaults
    def __init__(self,
                 streamer_address,
                 exhange_address,
                 *args,
                 **kwargs):
        super().__init__(*args,
                        **kwargs)
        self.streamer_address = streamer_address
        self.exchange_address = exhange_address
        self.abi_json = RICOCHET_ABI
        self.argsForFunction = {"streamer_address": self.streamer_address}
        self.function = self.contract.functions.closeStream