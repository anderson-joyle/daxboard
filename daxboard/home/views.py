import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Access
from services.sessioning import SessionManager

# Create your views here.
def index(request):
    sessionManager = SessionManager(request)
    sessionManager.init_session()

    if request.user.is_authenticated:
        return redirect('/operations')

    html = '<html><body><b>{0}</b></body></html>'.format(__name__)
    return HttpResponse(html)
    # return render(request, 'home/index.html', {})

def logout(request):
    request.session.reset()
    redirect('index')    

def dashboard(request):
    pass
