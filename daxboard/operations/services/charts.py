from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class ChartBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self._data_fetcher.fetch(self)

    def funcname(self, parameter_list):
        raise NotImplementedError

class OperationChartSimple(ChartBase):
    def get_url(self):
        return 'URL_SIMPLE'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return 'chart_simple_value'

class OperationChartDetailed(ChartBase):
    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return 'chart_detailed_value'