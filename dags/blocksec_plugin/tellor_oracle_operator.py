from airflow.utils.decorators import apply_defaults
from blocksec_plugin.contract_interaction_operator import ContractInteractionOperator
from blocksec_plugin.abis import SUBMIT_VALUE_ABI
import requests
from time import sleep



class TellorOracleOperator(ContractInteractionOperator):
    """
    Calls `withdrawRewards` on TPS contracts
    """
    template_fields = ['request_id', 'price']

    @apply_defaults
    def __init__(self,
                 request_id,
                 price,
                 *args,
                 **kwargs):
        super().__init__(*args,
                        **kwargs)
        self.request_id = request_id
        self.price = price
        self.abi_json = SUBMIT_VALUE_ABI
        self.argsForFunction = {"request_id": self.request_id, "price": self.price}
        self.function = self.contract.functions.submitValue

    def get_gas_price(self):
        is_success = False
        while not is_success:
            try:
                url = "https://ethgasstation.info/json/ethgasAPI.json"
                r = requests.get(url=url)
                data = r.json()
                is_success = True
            except Exception as e:
                print("FAILED: ", e)
                print("Will retry...")
                sleep(10)

        return int(data[self.gas_key] / 10)
