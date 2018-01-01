from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class SummaryBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)  

class BatchJobSummaryBase(SummaryBase):
    def status(self):
        raise NotImplementedError('Method BatchJobSummaryBase.status is not implemented.')

    def get_url(self):
        return '/data/BatchJobs?$filter=Status eq Microsoft.Dynamics.DataEntities.BatchStatus\'{0}\''.format(self.status())

    def get_context_value(self):
        return len(self.json_data['value'])

class BatchJobErrorSummary(BatchJobSummaryBase):
    def status(self):
        return 'Error'

    def get_context_key(self):
        return __class__.__name__

class BatchJobExecutingSummary(BatchJobSummaryBase):
    def status(self):
        return 'Executing'

    def get_context_key(self):
        return __class__.__name__

class BatchJobWaitingSummary(BatchJobSummaryBase):
    def status(self):
        return 'Waiting'

    def get_context_key(self):
        return __class__.__name__

class BatchJobWithholdSummary(BatchJobSummaryBase):
    def status(self):
        return 'Hold'

    def get_context_key(self):
        return __class__.__name__