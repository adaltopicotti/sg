from django.shortcuts import render
from agendamento.forms import CooperativaForm, SeguradoForm
# Create your views here.

def agendamento_novo(request):

    return render(request, 'agendamento/novo.html', {
        'cooperativaForm': CooperativaForm,
        'seguradoForm': SeguradoForm,
        'collapseOpt': 1} )
