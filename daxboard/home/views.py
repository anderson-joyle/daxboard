import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Access

# Create your views here.
def index(request):
    content = ''

    if request.session.get('access_token'):
        status = 'Logged in'
        content += 'Authorization: {0} {1}<br>'.format(request.session['token_type'], request.session['access_token'])
    else:
        if (request.GET.get('resource') and 
        request.GET.get('client_id') and 
        request.GET.get('tenant') and
        (request.GET.get('client_secret') !=
        (request.GET.get('username') and request.GET.get('password')))):
            status = 'Logged in'
            body = {}

            content += 'Resource: {0}<br>'.format(request.GET.get('resource'))
            content += 'Client id: {0}<br>'.format(request.GET.get('client_id'))
            content += 'Tenant: {0}<br>'.format(request.GET.get('tenant'))

            body['resource'] = request.GET.get('resource')
            body['client_id'] = request.GET.get('client_id')

            if request.GET.get('client_secret'):
                # It is possible that client secret string contains URL enconde. Deal with it.
                body['client_secret'] = request.GET.get('client_secret')
                body['grant_type'] = 'client_credentials'

                content += 'Client secret: {0}<br>'.format(request.GET.get('client_secret'))

            if request.GET.get('username') and request.GET.get('password'):
                body['username'] = request.GET.get('username')
                body['password'] = request.GET.get('password')
                body['grant_type'] = request.GET.get('password')

                content += 'Username: {0}<br>'.format(request.GET.get('username'))
                content += 'Password: {0}<br>'.format(request.GET.get('password'))

            # content += 'Body: {0}<br>'.format(body)

            token_url = 'https://login.microsoftonline.com/{0}/oauth2/token'.format(request.GET.get('tenant'))
            
            response = requests.post(token_url, data=body)
            response.raise_for_status()

            json_response = response.json()

            if response.status_code == 200:
                request.session['access_token'] = json_response['access_token']
                request.session['token_type'] = json_response['token_type']

                status = 'Logged in'

            content += 'Response code: {0}<br>'.format(response.status_code)
            content += 'Authorization: {0} {1}<br>'.format(json_response['token_type'], json_response['access_token'])

        else:
            status = 'Anonymous'

    html = '<html><body>Status <b>{0}</b>.<p>{1}</p></body></html>'.format(status, content)
    
    return render(request, 'home/index.html', {})

def dashboard(request):
    pass
