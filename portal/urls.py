from django.conf.urls import include, url
from . import views as portal_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', portal_views.home, name='home'),
    url(r'^accounts/signup/$', portal_views.signup, name='signup'),
    url(r'^accounts/login/$', portal_views.login_site, name='login_site'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/auth/$', auth_views.login, name='login'),
]
