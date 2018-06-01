import requests

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth import authenticate, login

from requests.exceptions import HTTPError

# Create your views here.
def index(request):
    try:
        if not request.user.is_authenticated:
            if not request.GET.get('resource'):
                raise ValidationError('Argument RESOURCE not declared.')

            if not request.GET.get('client_id'):
                raise ValidationError('Argument CLIENT_ID not declared.')

            if not request.GET.get('tenant'):
                raise ValidationError('Argument TENANT not declared.')

            if not request.GET.get('client_secret') and not (request.GET.get('username') and request.GET.get('password')):
                raise ValidationError('Argument CLIENT_SECRET or combination of USERNAME and PASSWORD not declared.')

            user = User.objects.get(username=request.GET.get('tenant'))

            # auth = authenticate(self._request, username=request_manager.get_tenant(), password=request_manager.get_tenant())
            if user is not None:
                login(request, user)
        else:
            return redirect('/operations')
    except ValidationError as err:
        html = '<html><body>Error: <b>{0}</b></body></html>'.format(err)
        return HttpResponse(html)
    except ObjectDoesNotExist as err:
        user = User.objects.create_user(username=request.GET.get('tenant'), password=request.GET.get('tenant'))
        
        if user is not None:
            login(request, user)
            return redirect('/operations')
        else:
            html = '<html><body>Error: <b>{0}</b></body></html>'.format('Could not create new user')
            return HttpResponse(html)

    if request.user.is_authenticated:
        request.session['resource'] = request.GET.get('resource')
        request.session['client_id'] = request.GET.get('client_id')
        request.session['tenant'] = request.GET.get('tenant')

        if request.GET.get('client_secret'):
            request.session['client_secret'] = request.GET.get('client_secret')
            request.session['grant_type'] = 'client_credentials'
        else:
            request.session['username'] = request.GET.get('username')
            request.session['password'] = request.GET.get('password')
            request.session['grant_type'] = 'password'
        
        try:
            body = {}
            body['resource'] = request.session['resource']
            body['client_id'] = request.session['client_id']
            body['tenant'] = request.session['tenant']
            body['grant_type'] = request.session['grant_type']

            if request.session['grant_type'] == 'client_credentials':
                body['client_secret'] = request.session['client_secret']
            else:
                body['username'] = request.session['username']
                body['password'] = request.session['password']

            token_url = 'https://login.microsoftonline.com/{0}/oauth2/token'.format(request.session['tenant'])
            
            response = requests.post(token_url, data=body)
            response.raise_for_status()

            json_response = response.json()

            request.session['token_json'] = json_response

            login(request, user)
            return redirect('/operations')
                
        except HTTPError as err:
            html = '<html><body>Error: <b>{0}</b></body></html>'.format(err)
            return HttpResponse(html)
    else:
        html = '<html><body>Error: <b>{0}</b></body></html>'.format('Could not login')
        return HttpResponse(html)

def logout(request):
    request.session.reset()
    redirect('index')    

def dashboard(request):
    pass