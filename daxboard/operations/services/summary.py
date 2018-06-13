from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class SummaryBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher
        self._extra_filters = {}

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)  

    def extra_filters(self, **kwargs):
        self._extra_filters = kwargs

class SalesOrdersSummary(SummaryBase):
    def get_url(self):
        extra_filters = ''
        for key, value in self._extra_filters.items():
            extra_filters += 'and {0} eq \'{1}\''.format(key, value)
        
        return '/data/SalesOrderHeaders?$select=SalesOrderNumber&$filter=SalesOrderStatus eq Microsoft.Dynamics.DataEntities.SalesStatus\'Backorder\' {0}'.format(extra_filters)

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])

class PurchOrdersSummary(SummaryBase):
    def get_url(self):
        extra_filters = ''        
        for key, value in self._extra_filters.items():
            extra_filters += 'and {0} eq \'{1}\''.format(key, value)

        return '/data/PurchaseOrderHeaders?&$select=PurchaseOrderNumber&$filter=PurchaseOrderStatus eq Microsoft.Dynamics.DataEntities.PurchStatus\'Backorder\' {0}'.format(extra_filters)

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])

class FreeTextInvoiceSummary(SummaryBase):
    def get_url(self):
        extra_filters = ''        
        for key, value in self._extra_filters.items():
            extra_filters += 'and {0} eq \'{1}\''.format(key, value)

        return '/data/FreeTextInvoiceHeaders?$filter=IsPosted eq Microsoft.Dynamics.DataEntities.NoYes\'No\' {0}'.format(extra_filters)

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