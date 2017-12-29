from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

from .requesting import RequestManager
from .tokening import TokenManager

class SessionManager(object):
    def __init__(self, request):
        self._request = request

    def init_session(self):
        try:
            request_manager = RequestManager(self._request)
            request_manager.raise_for_missing_argument()
            
            if request_manager.is_login_attempt():
                if not self._request.user.is_authenticated:
                    self._request.session['resource'] = self._request.GET.get('resource')
                    self._request.session['tenant'] = self._request.GET.get('tenant')
                    self._request.session['client_id'] = self._request.GET.get('client_id')

                    if self._request.GET.get('client_secret'):
                        self._request.session['client_secret'] = self._request.GET.get('client_secret')

                        token_manager = TokenManager(
                            resource=request_manager.get_resource(),
                            tenant=request_manager.get_tenant(),
                            client_id=request_manager.get_client_id(),
                            client_secret=request_manager.get_client_secret()
                        )

                    if self._request.GET.get('username') and self._request.GET.get('password'):
                        self._request.session['username'] = self._request.GET.get('username')
                        self._request.session['password'] = self._request.GET.get('password')

                        token_manager = TokenManager(
                            resource=request_manager.get_resource(),
                            tenant=request_manager.get_tenant(),
                            client_id=request_manager.get_client_id(),
                            username=request_manager.get_username(),
                            password=request_manager.get_password()
                        )

                    self._request.session['token_json'] = token_manager.generate_token()
                    
                    user = User.objects.get(username=request_manager.get_tenant())
                    auth = authenticate(self._request, username=request_manager.get_tenant(), password=request_manager.get_tenant())
                    if auth is not None:
                        login(self._request, auth)
            else:
                pass
        except ObjectDoesNotExist as err:
            User.objects.create_user(username=request_manager.get_tenant(), password=request_manager.get_tenant())
            auth = authenticate(self._request, username=request_manager.get_tenant(), password=request_manager.get_tenant())
            if auth is not None:
                login(self._request, auth)
        except ValueError as err:
            print('Exception: ', err)
            
