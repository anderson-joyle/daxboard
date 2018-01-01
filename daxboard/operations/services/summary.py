from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class SummaryBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)  

class SalesOrdersSummary(SummaryBase):
    def get_url(self):
        return '/data/SalesOrderHeaders?$filter=SalesOrderStatus eq Microsoft.Dynamics.DataEntities.SalesStatus\'Backorder\'&$select=SalesOrderNumber'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])

class PurchOrdersSummary(SummaryBase):
    def get_url(self):
        return '/data/PurchaseOrderHeaders?$filter=PurchaseOrderStatus eq Microsoft.Dynamics.DataEntities.PurchStatus\'Backorder\'&$select=PurchaseOrderNumber'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])

class BalanceSummary(SummaryBase):
    def get_url(self):
        return 'Balance'

class BigAmountSummary(SummaryBase):
    def get_url(self):
        return 'BigAmountHeaders'