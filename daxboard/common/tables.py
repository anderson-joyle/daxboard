from .fetching import Fetchable, Fetcher
from .contexting import Contextable

class TablesBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)   

class LegalEntities(TablesBase):
    def get_url(self):
        return '/data/LegalEntities'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data['value']