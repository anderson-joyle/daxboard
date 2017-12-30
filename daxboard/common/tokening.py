import requests
import time

class TokenManager(object):
    def __init__(self, **kargs):
        self.access_token = ''
        self.token_type = ''
        self.expires_on = ''
        self.resource = ''

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

            self.access_token = json_response['access_token']
            self.token_type = json_response['token_type']
            self.expires_on = json_response['expires_on']
            self.resource = json_response['resource']
        except:
            pass

    def _is_valid(self):
        is_valid = True
        current_timestamp = str(time.time() - 10).split('.')[0]
        if self.expires_on < current_timestamp:
            is_valid = False
        return is_valid

    def get_access_token(self):
        if not self.access_token:
            self.generate_token()

        if not self._is_valid():
            self.generate_token()

        return self.access_token

    def get_token_type(self):
        if not self.token_type:
            self.generate_token()

        if not self._is_valid():
            self.generate_token()

        return self.token_type

    def get_resource(self):
        if not self.resource:
            self.generate_token()

        if not self._is_valid():
            self.generate_token()

        if self.resource.endswith('/'):
            self.resource = self.resource[:len(self.resource) - 1]

        return self.resource
        