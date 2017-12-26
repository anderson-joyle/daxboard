class RequestManager(object):
    def __init__(self, request):
        self._request = request

    def _is_valid(self):
        is_valid = False
        if (self._request.session.get('resource') and 
            self._request.session.get('client_id') and 
            self._request.session.get('tenant') and
            (self._request.session.get('client_secret') !=
            (self._request.session.get('username') and self._request.GET.get('password')))):   
            is_valid = True             
        else:
            if (self._request.GET.get('resource') and 
            self._request.GET.get('client_id') and 
            self._request.GET.get('tenant') and
            (self._request.GET.get('client_secret') !=
            (self._request.GET.get('username') and self._request.GET.get('password')))):
                is_valid = True

        return is_valid

    def is_login_attempt(self):
        is_login_attempt = False

        if (self._request.session.get('resource') or 
            self._request.session.get('client_id') or 
            self._request.session.get('tenant') or 
            self._request.session.get('client_secret') or 
            self._request.session.get('username') or 
            self._request.session.get('password') or 
            self._request.GET.get('resource') or 
            self._request.GET.get('client_id') or 
            self._request.GET.get('tenant') or 
            self._request.GET.get('client_secret') or 
            self._request.GET.get('username') or 
            self._request.GET.get('password')):

            is_login_attempt = True

        return is_login_attempt

    def raise_for_missing_argument(self):
        if self.is_login_attempt():
            if not self._is_valid():
                if not self._request.session.get('resource') or not self._request.GET.get('resource'):
                    raise ValueError('Argument RESOURCE has not been found on request.')
                elif not self._request.session.get('client_id') or not self._request.GET.get('client_id'):
                    raise ValueError('Argument CLIENT_ID has not been found on request.')
                elif not self._request.session.get('tenant') or not self._request.GET.get('tenant'):
                    raise ValueError('Argument TENANT has not been found on request.')
                elif not self._request.session.get('tenant') or not self._request.GET.get('tenant'):
                    raise ValueError('Argument TENANT has not been found on request.')
                else:
                    if not (self._request.session.get('client_secret') or self._request.GET.get('client_secret')) and not (self._request.session.get('username') or self._request.GET.get('username')) and not (self._request.session.get('password') or self._request.GET.get('password')):
                        raise ValueError('Please provide either CLIENT_SECRET or combination of USERNAME and PASSWORD arguments.')
                    elif not (self._request.session.get('client_secret') or self._request.GET.get('client_secret')) and (self._request.session.get('username') or self._request.GET.get('username')) != (self._request.session.get('password') or self._request.GET.get('password')):
                        raise ValueError('Please provide both USERNAME and PASSWORD arguments.')
                    else:
                        raise ValueError('An unknown error has been raisen.')

    def get_tenant(self):
        tenant = ''
        if self._request.session.get('tenant'):
            tenant = self._request.session.get('tenant')
        else:
            tenant = self._request.GET.get('tenant')

        return tenant

    def get_resource(self):
        resource = ''
        if self._request.session.get('resource'):
            resource = self._request.session.get('resource')
        else:
            resource = self._request.GET.get('resource')

        return resource

    def get_client_id(self):
        client_id = ''
        if self._request.session.get('client_id'):
            client_id = self._request.session.get('client_id')
        else:
            client_id = self._request.GET.get('client_id')

        return client_id

    def get_client_secret(self):
        client_secret = ''
        if self._request.session.get('client_secret'):
            client_secret = self._request.session.get('client_secret')
        else:
            client_secret = self._request.GET.get('client_secret')

        return client_secret

    def get_username(self):
        username = ''
        if self._request.session.get('username'):
            username = self._request.session.get('username')
        else:
            username = self._request.GET.get('username')

        return username

    def get_password(self):
        password = ''
        if self._request.session.get('password'):
            password = self._request.session.get('password')
        else:
            password = self._request.GET.get('password')

        return password