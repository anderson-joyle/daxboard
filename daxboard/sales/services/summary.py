from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class SummaryBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)  

class OpenCasesSummary(SummaryBase):
    def get_url(self):
        return '/data/DXBCases?$filter=CaseStatus eq Microsoft.Dynamics.DataEntities.CaseStatus\'Planned\'&$select=CaseId'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])

class ActiveOpportunitiesSummary(SummaryBase):
    def get_url(self):
        return '/data/DXBOpportunities?$filter=Status eq Microsoft.Dynamics.DataEntities.smmOpportunityStatus\'Active\'&$select=OpportunityId'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])

class OpenLeadsSummary(SummaryBase):
    def get_url(self):
        return '/data/DXBLeads?$filter=LeadStatus eq Microsoft.Dynamics.DataEntities.smmLeadStatus\'Open\'&$select=LeadId'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])

class BackendSalesOrdersSummary(SummaryBase):
    def get_url(self):
        return '/data/SalesOrderHeaders?$filter=SalesOrderStatus eq Microsoft.Dynamics.DataEntities.SalesStatus\'Backorder\'&$select=SalesOrderNumber'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return len(self.json_data['value'])