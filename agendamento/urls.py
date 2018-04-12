from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^agendamento/novo/$', views.agendamento_novo, name='agendamento_novo'),
    url(r'^relatorios/cooperativa$', views.relatorio_cooperativa, name='relatorio_cooperativa'),
    url(r'^relatorios/segurado$', views.relatorio_segurado, name='relatorio_segurado'),
    url(r'^relatorios/frota/$', views.relatorio_frota, name='relatorio_frota'),
    url(r'^cadastro/frota/(?P<pk>[0-9]+)$', views.cadastro_frota, name='cadastro_frota'),
    url(r'^cadastro/segurado/(?P<coopForm>)$', views.cadastro_segurado, name='cadastro_segurado'),

]
