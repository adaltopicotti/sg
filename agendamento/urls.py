from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^agendamento/novo/$', views.agendamento_novo, name='agendamento_novo'),
]
