import requests

class Fetcher(object):
    def __init__(self, token):
        self._token = token

    def fetch(self, fetchable):
        url = '{0}{1}'.format(self._token.get_resource(), fetchable.get_url())

        headers = {
            'Authorization': '{0} {1}'.format(self._token.get_token_type(), self._token.get_access_token()),
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
        }

        if '/data/' in url:
            headers['OData-MaxVersion'] = '4.0'
            headers['OData-Version'] = '4.0'

            method = 'GET'
        elif '/api/services/' in url:
            method = 'POST'
        else:
            raise ValueError('Couldn\'t define if URL is ODAT or REST SERVICE.')
        
        response = requests.request(method, url, headers=headers, verify=False)
        response.raise_for_status()

        json_response = response.json()
        
        return json_response
        

class Fetchable(object):
    def fetch_data(self, fetcher):
        raise NotImplementedError

    def get_url(self):
        raise NotImplementedError