import requests

class Fetcher(object):
    def __init__(self, token):
        self._token = token

    def fetch(self, fetchable):
        headers = {
            'Authorization': '{0} {1}'.format(self._token.get_token_type(), self._token.get_access_token()),
            'OData-MaxVersion': '4.0',
            'OData-Version': '4.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
        }
        
        url = '{0}{1}'.format(self._token.get_resource(), fetchable.get_url())
        
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()

        json_response = response.json()
        
        return json_response['value']
        

class Fetchable(object):
    def fetch_data(self, fetcher):
        raise NotImplementedError

    def get_url(self):
        raise NotImplementedError