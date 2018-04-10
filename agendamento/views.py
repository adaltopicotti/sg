from django.shortcuts import render
from agendamento.forms import *
from agendamento.models import *
# Create your views here.


def switch_form(argument):
    switcher = {
        "Frota": ["frota_form.html", FrotaForm],
        "Empresarial": ["emp_form.html", EmpresarialForm],
        "Transporte": ["transp_form.html", ''],

    }
    return switcher.get(argument)


def agendamento_novo(request):
    ramos = Ramo.objects.all().order_by('nome')
    if request.method == "POST":
        coopForm = CooperativaForm(request.POST)
        ramoForm = RamoForm(request.POST)
        ramoChoice = request.POST['inputRamo']
        if coopForm.is_valid():
            #coopForm.save()
            secondaryForm = switch_form(ramoChoice)
            seguradoForm = SeguradoForm(request.POST)
            if seguradoForm.is_valid():
                secForm = secondaryForm[1](request.POST)
                if secForm.is_valid():
                    coopForm.save()
                    seguradoForm.save()
                    #secForm.save()
                    return render(request, 'agendamento/novo2.html', {
                        'ramos': ramos,
                        'primaryFormSet': 'disabled',
                        'selected': ramoChoice,
                        'cooperativaForm': coopForm,
                        'seguradoForm': seguradoForm,
                        'secondaryForm': secForm,
                        'secondaryFormTemplate':secondaryForm[0]})
            return render(request, 'agendamento/novo2.html', {
                'ramos': ramos,
                'primaryFormSet': 'disabled',
                'selected': ramoChoice,
                'cooperativaForm': coopForm,
                'seguradoForm': SeguradoForm,
                'secondaryForm': secondaryForm[1],
                'secondaryFormTemplate':secondaryForm[0]})

    else:
        render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'collapseOpt': 4})
    return render(request, 'agendamento/novo2.html', {
    'cooperativaForm': CooperativaForm,
    'seguradoForm': SeguradoForm,
    'empresarialForm': EmpresarialForm,
    'collapseOpt': 3,
    'ramos':ramos})
