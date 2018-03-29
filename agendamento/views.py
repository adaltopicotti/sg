from django.shortcuts import render
from agendamento.forms import CooperativaForm, SeguradoForm, EmpresarialForm
# Create your views here.

def agendamento_novo(request):

    return render(request, 'agendamento/novo0.html', {
        'cooperativaForm': CooperativaForm,
        'seguradoForm': SeguradoForm,
        'empresarialForm': EmpresarialForm,
        'collapseOpt': 1} )
