from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class LatestBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher
        self._extra_filters = {}

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)   

    def extra_filters(self, **kwargs):
        self._extra_filters = kwargs

class LatestSalesInvoices(LatestBase):
    def get_url(self):
        extra_filters = ''
        for key, value in self._extra_filters.items():
            extra_filters += '{0} eq \'{1}\''.format(key, value)
        
        if extra_filters:
            return '/data/SalesInvoiceHeaders?$top=5&$orderby=InvoiceDate desc&$select=InvoiceNumber, TotalInvoiceAmount, InvoiceCustomerAccountNumber, dataAreaId&$filter={0}'.format(extra_filters)
        else:
            return '/data/SalesInvoiceHeaders?$top=5&$orderby=InvoiceDate desc&$select=InvoiceNumber, TotalInvoiceAmount, InvoiceCustomerAccountNumber, dataAreaId'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data['value']

class LatestSalesOrders(LatestBase):
    def get_url(self):
        extra_filters = ''
        for key, value in self._extra_filters.items():
            extra_filters += '{0} eq \'{1}\''.format(key, value)
        
        if extra_filters:
            return '/data/SalesOrderHeaders?$top=5&$orderby=SalesOrderNumber desc&$select=SalesOrderNumber, InvoiceCustomerAccountNumber, OrderTotalAmount, dataAreaId&$filter={0}'.format(extra_filters)
        else:
            return '/data/SalesOrderHeaders?$top=5&$orderby=SalesOrderNumber desc&$select=SalesOrderNumber, InvoiceCustomerAccountNumber, OrderTotalAmount, dataAreaId'

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