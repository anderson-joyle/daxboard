from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<html><body><b>{0}</b></body></html>'.format(__name__))