from django.shortcuts import render, redirect
from django.contrib.auth import views, forms
#-- login_site
from django.contrib.auth import login, authenticate
from portal.forms import SignUpForm, LoginForm, ValidateLoginForm
from portal.models import ValidateLogin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
import json

#-- end login_site

# Create your views here.

def validate(request):
    if request.method == "GET":
        form = ValidateLoginForm()
        form.login = request.GET['login']
        form.password = request.GET['password']
        form.token = request.GET['token']
        valid_user = ValidateLogin.objects.filter(login=form.login)
        responseData = {
            'token': valid_user.token,
            'expirate_date': valid_user.expirate_date, 
        }
    return HttpResponse(responseData)


def home(request):
    return render(request, 'portal/structure/home.html', {'form': LoginForm} )



def login_site(request):
    return render(request, 'website/accounts/login.html', {'form': LoginForm} )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'website/accounts/signup.html', {'form': form})
