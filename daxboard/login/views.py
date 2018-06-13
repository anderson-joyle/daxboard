import requests
import pickle

from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib import messages

from common.tokening import TokenManager

from .forms import LoginForm

from session.models import Session


# Create your views here.
def index(request):
    loginForm = LoginForm(request.POST or None)

    if request.method == 'POST':
        if loginForm.is_valid():
            client_id = loginForm['client_id'].value()
            resource = loginForm['dynamics_fo_url'].value()
            tenant = loginForm['tenant'].value()
            client_id = loginForm['client_id'].value()                       
            client_secret = loginForm['client_secret'].value()

            token_manager = TokenManager(
                                resource=resource,
                                tenant=tenant,
                                client_id=client_id,
                                client_secret=client_secret
                            )

            if token_manager.get_access_token():
                try:
                    user = authenticate(request, username=client_id, password=client_secret)
                    if user is None:
                        user = User.objects.get(username=client_id)
                        user.set_password(client_secret)
                        user.save()

                except ObjectDoesNotExist as err:    
                    user = User.objects.create_user(client_id, password=client_secret)

                if user is not None:
                    authenticate(request, username=client_id, password=client_secret)
                    login(request, user)

            request.session['token_pack'] = token_manager.pack()

            return redirect('/operations')

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/operations')

    return render(request, 'login/index.html', {'form':loginForm})