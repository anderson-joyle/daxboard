class Fetcher(object):
    def __init__(self, token):
        self._token = token

    def fetch(self, fetchable):
        print('==========================> ',fetchable.get_url())

class Fetchable(object):
    def fetch_data(self, fetcher):
        raise NotImplementedError

    def get_url(self):
        raise NotImplementedError