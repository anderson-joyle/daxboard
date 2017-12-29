from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class SummaryBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self._data_fetcher.fetch(self)
        self.json_data = fetcher.fetch(self)    

class SalesOrdersSummary(SummaryBase)
    def get_url(self):
        return 'SalesHeaders'

class PurchOrdersSummary(SummaryBase)
    def get_url(self):
        return 'PurchHeaders'

class BalanceSummary(SummaryBase)
    def get_url(self):
        raise return 'Balance'

class BigAmountSummary(SummaryBase)
    def get_url(self):
        raise return 'BigAmountHeaders'