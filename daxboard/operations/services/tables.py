from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class LatestBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)   

class LatestSalesInvoices(LatestBase):
    def get_url(self):
        return '/data/SalesInvoiceHeaders?$top=10&$orderby=InvoiceDate desc'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data 

class LatestSalesOrders(LatestBase):
    def get_url(self):
        return '/data/SalesOrderHeaders?$top=10&$orderby=SalesOrderNumber desc'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data 

class LegalEntities(LatestBase):
    def get_url(self):
        return '/data/LegalEntities'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data 