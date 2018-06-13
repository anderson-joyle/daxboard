import requests
import time

from datetime import datetime
from requests import HTTPError

from django.core.exceptions import ValidationError

from session.models import Session

class TokenManager(object):
    def __init__(self, resource='', client_id='', tenant='', client_secret=''):
        try:
            self._resource = resource
            self._client_id = client_id
            self._tenant = tenant            
            self._client_secret = client_secret
            self._grant_type = 'client_credentials'

            self._got_it = False

        except (KeyError, ValueError) as err:
            raise ValidationError(err)

    def pack(self):
        pack = {
            'resource':self._resource,
            'tenant':self._tenant,
            'client_id':self._client_id,
            'client_secret':self._client_secret,
            'response_json':self._response_json,
        }
        
        return pack

    def unpack(self, pack):
        self._resource = pack['resource']
        self._tenant = pack['tenant']
        self._client_id = pack['client_id']
        self._client_secret = pack['client_secret']
        self._response_json = pack['response_json']

        self._got_it = True
        
    def _generate_token(self):
        try:
            body = {}
            body['resource'] = self._resource
            body['client_id'] = self._client_id
            body['tenant'] = self._tenant    
            body['grant_type'] = self._grant_type
            body['client_secret'] = self._client_secret

            token_url = 'https://login.microsoftonline.com/{0}/oauth2/token'.format(self._tenant)
            
            if not self._is_valid() or not self._got_it:
                response = requests.post(token_url, data=body)
                response.raise_for_status()

                self._got_it = True
                self._response_json = response.json()
            
        except HTTPError as err:
            response_error_json = response.json()
            raise ValidationError('Error {0}: {1}'.format(response_error_json['error_codes'], response_error_json['error_description']))

    def get_expires_on(self):
        self._generate_token()
        return datetime.fromtimestamp(self._response_json['expires_on'])

    def get_access_token(self):
        self._generate_token()
        return self._response_json['access_token']

    def get_token_type(self):
        self._generate_token()
        return self._response_json['token_type']

    def get_resource(self):
        self._generate_token()
        return self._response_json['resource']

    def _is_valid(self):
        ret = True
        if self._got_it:
            expires_on = self._response_json['expires_on']
            if datetime.now() > datetime.fromtimestamp(int(expires_on)):
                ret = False
        else:
            ret = False

        return ret

        