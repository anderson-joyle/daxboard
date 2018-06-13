import requests

from common.tokening import TokenManager

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth import authenticate, login

from requests.exceptions import HTTPError

from session.models import Session

def index(request):
    return redirect('/login')

def logout(request):
    request.session.flush()
    return redirect('/login')