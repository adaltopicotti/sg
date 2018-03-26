from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(request, 'website/structure/home.html', {'form': LoginForm} )
