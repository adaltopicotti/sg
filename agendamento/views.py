from django.shortcuts import render
from agendamento.forms import *
# Create your views here.

def agendamento_novo(request):

    if request.method == "POST":
        coopForm = CooperativaForm(request.POST)
        ramoForm = RamoForm(request.POST)
        if coopForm.is_valid():
            coopForm.save()
            return render(request, 'agendamento/novo2.html', {
                'cooperativaForm': CooperativaForm,
                'seguradoForm': SeguradoForm,
                'empresarialForm': EmpresarialForm,
                'ramoForm': RamoForm,
                'frotaForm': FrotaForm,
                'collapseOpt': ramoForm['nome'].text})
        else:
            render(request, 'agendamento/novo2.html', {
            'cooperativaForm': CooperativaForm,
            'seguradoForm': SeguradoForm,
            'empresarialForm': EmpresarialForm,
            'ramoForm': RamoForm,
            'frotaForm': FrotaForm,
            'collapseOpt': 2})
    else:
        render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'seguradoForm': SeguradoForm,
        'empresarialForm': EmpresarialForm,
        'ramoForm': RamoForm,
        'frotaForm': FrotaForm,
        'collapseOpt': 4})
    return render(request, 'agendamento/novo2.html', {
    'cooperativaForm': CooperativaForm,
    'seguradoForm': SeguradoForm,
    'empresarialForm': EmpresarialForm,
    'ramoForm': RamoForm,
    'frotaForm': FrotaForm,
    'collapseOpt': 3})
