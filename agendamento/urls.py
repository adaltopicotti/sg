from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^agendamento/novo/$', views.agendamento_novo, name='agendamento_novo'),
    
    url(r'^teste$', views.teste, name='teste'),
    url(r'^relatorios/cooperativa$', views.relatorio_cooperativa, name='relatorio_cooperativa'),
    url(r'^relatorios/segurado$', views.relatorio_segurado, name='relatorio_segurado'),
    url(r'^relatorios/frota$', views.relatorio_frota, name='relatorio_frota'),
    url(r'^relatorios/agendamento$', views.relatorio_agendamento, name='relatorio_agendamento'),
    url(r'^cadastro/agendamento$', views.cadastro_agendamento, name='cadastro_agendamento'),
    url(r'^cadastro/segurado/(?P<coopForm>)$', views.cadastro_segurado, name='cadastro_segurado'),
    url(r'^detail/agendamento/(?P<protocol>[0-9]+)$', views.detail_agendamento, name='detail_agendamento'),

]
