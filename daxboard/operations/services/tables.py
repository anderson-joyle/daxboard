from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class LatestBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)   

class LatestSalesInvoices(LatestBase):
    def get_url(self):
        return '/data/SalesInvoiceHeaders?$top=10&$orderby=InvoiceDate desc&$select=InvoiceNumber, TotalInvoiceAmount, InvoiceCustomerAccountNumber, dataAreaId'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data['value']

class LatestSalesOrders(LatestBase):
    def get_url(self):
        return '/data/SalesOrderHeaders?$top=10&$orderby=SalesOrderNumber desc&$select=SalesOrderNumber, InvoiceCustomerAccountNumber, OrderTotalAmount, dataAreaId'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data['value']

class LegalEntities(LatestBase):
    def get_url(self):
        return '/data/LegalEntities'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data['value']

class UserInfoService(LatestBase):
    def get_url(self):
        return '/api/services/UserSessionService/AifUserSessionService/GetUserSessionInfo'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data