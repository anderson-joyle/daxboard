import requests

class TokenManager(object):
    def __init__(self, **kargs):
        self._resource = kargs['resource']
        self._client_id = kargs['client_id']
        self._tenant = kargs['tenant']

        if 'client_secret' in kargs:
            self._grant_type = 'client_credentials'
            self._client_secret = kargs['client_secret']
        elif 'username' in kargs and 'password' in kargs:
            self._grant_type = 'password'
            self._username = kargs['username']
            self._password = kargs['password']
        else:
            raise ValueError('Please provide either CLIENT_SECRET or combination of USERNAME and PASSWORD arguments.')
        

    def generate_token(self):
        try:
            body = {}
            body['resource'] = self._resource
            body['client_id'] = self._client_id
            body['tenant'] = self._tenant

            if self._grant_type == 'client_credentials':
                body['grant_type'] = 'client_credentials'
                body['client_secret'] = self._client_secret
            else:
                body['grant_type'] = 'password'
                body['username'] = self._username
                body['password'] = self._password

            token_url = 'https://login.microsoftonline.com/{0}/oauth2/token'.format(self._tenant)
            
            response = requests.post(token_url, data=body)
            response.raise_for_status()

            json_response = response.json()

            return json_response
        except:
            pass
        