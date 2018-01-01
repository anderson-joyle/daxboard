import requests
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from common.fetching import Fetcher as DataFetcher
from common.tokening import TokenManager

# Create your views here.
def index(request):
    """
    Some description here.
    """
    if not request.user.is_authenticated:
        return redirect('/')

    context = {}    
    context['resource_url'] = request.session.get('resource')

    token_manager = TokenManager(
                        resource=request.session.get('resource'),
                        tenant=request.session.get('tenant'),
                        client_id=request.session.get('client_id'),
                        client_secret=request.session.get('client_secret'),
                        username=request.session.get('username'),
                        password=request.session.get('password')
                    )

    data_fetcher = DataFetcher(token_manager)

    return render(request, 'sales/index.html', context)