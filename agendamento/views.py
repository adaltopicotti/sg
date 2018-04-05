from django.shortcuts import render
from agendamento.forms import *
from agendamento.models import *
# Create your views here.


def switch_form(argument):
    switcher = {
        "Frota": "frota_form.html",
        "Empresarial": "emp_form.html",
        "Transporte": "transp_form.html",

    }
    return switcher.get(argument)


def agendamento_novo(request):
    ramos = Ramo.objects.all().order_by('nome')
    if request.method == "POST":
        coopForm = CooperativaForm(request.POST)
        ramoForm = RamoForm(request.POST)

        if coopForm.is_valid():
            #coopForm.save()
            #secondaryForm = switch_form(ramoForm['nome'])
            return render(request, 'agendamento/novo2.html', {
                'cooperativaForm': CooperativaForm,
                'seguradoForm': SeguradoForm,
                'empresarialForm': EmpresarialForm,
                'ramoForm': RamoForm,
                'frotaForm': FrotaForm,
                'collapseOpt': ramoForm['nome'].value})
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
