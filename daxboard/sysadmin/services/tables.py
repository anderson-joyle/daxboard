from common.fetching import Fetchable, Fetcher
from common.contexting import Contextable

class SqlDiagnosticServiceBase(Fetchable, Contextable):
    def __init__(self, fetcher):
        self._data_fetcher = fetcher

    def fetch_data(self):
        self.json_data = self._data_fetcher.fetch(self)

    def get_url(self):
        return '/api/services/SysSqlDiagnosticService/SysSqlDiagnosticServiceOperations'

class SqlBlocking(SqlDiagnosticServiceBase):
    def get_url(self):
        return super(SqlBlocking, self).get_url() + '/GetAxSqlBlocking'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data

class SqlLockInfo(SqlDiagnosticServiceBase):
    def get_url(self):
        return super(SqlLockInfo, self).get_url() + '/GetAxSqlLockInfo'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data

class SqlInfo(SqlDiagnosticServiceBase):
    def get_url(self):
        return super(SqlInfo, self).get_url() + '/GetAxSqlInfo'

    def get_context_key(self):
        return __class__.__name__

    def get_context_value(self):
        return self.json_data