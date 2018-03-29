from django.shortcuts import render
from agendamento.forms import *
# Create your views here.

def agendamento_novo(request):

    return render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'seguradoForm': SeguradoForm,
        'empresarialForm': EmpresarialForm,
        'ramoForm': RamoForm,
        'frotaForm': FrotaForm,
        'collapseOpt': 1} )
