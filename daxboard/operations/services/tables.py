from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class LatestBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self._data_fetcher.fetch(self)
        self.json_data = fetcher.fetch(self)   

class LatestInvoices(SummaryBase)
    def get_url(self):
        return 'LatestInvoicesURL'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return 'latest_invoices' 

class LatestSalesOrders(SummaryBase)
    def get_url(self):
        return 'LatestSalesOrdersURL'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return 'latest_sales_orders' 