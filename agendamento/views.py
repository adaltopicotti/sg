from django.shortcuts import render
from agendamento.forms import *
# Create your views here.

def agendamento_novo(request):
    if request.method == "POST":
        form = FrotaForm(request.POST)
        teste = form['renovacao_cia']
        if form.is_valid():


            form.save()
            return render(request, 'agendamento/novo2.html', {
                'cooperativaForm': CooperativaForm,
                'seguradoForm': SeguradoForm,
                'empresarialForm': EmpresarialForm,
                'ramoForm': RamoForm,
                'frotaForm': FrotaForm,
                'collapseOpt': teste})
        else:
            render(request, 'agendamento/novo2.html', {
                'cooperativaForm': CooperativaForm,
                'seguradoForm': SeguradoForm,
                'empresarialForm': EmpresarialForm,
                'ramoForm': RamoForm,
                'frotaForm': FrotaForm,
                'collapseOpt': teste})
    return render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'seguradoForm': SeguradoForm,
        'empresarialForm': EmpresarialForm,
        'ramoForm': RamoForm,
        'frotaForm': FrotaForm,
        'collapseOpt': 1})
