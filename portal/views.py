from django.shortcuts import render, redirect
from django.contrib.auth import views, forms
#-- login_site
from django.contrib.auth import login, authenticate
from portal.forms import SignUpForm, LoginForm, ValidateLoginForm
from django.contrib.auth.decorators import login_required

#-- end login_site

# Create your views here.

def validate(request):
    if request.method == "GET":
        form = ValidateLoginForm()
        if form.is_valid():
            post = form.save(commit=False)
            post.login = request.GET['login']
            post.password = request.GET['password']
            post.token = request.GET['token']
    return post.login


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
