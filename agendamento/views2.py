from django.shortcuts import render, get_object_or_404, redirect
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

def save(request, coop_pk, ):
    return ""

def agendamento_novo(request):
    ramos = Ramo.objects.all().order_by('nome')
    if request.method == "POST":
        coopForm = CooperativaForm(request.POST)
        ramoForm = RamoForm(request.POST)
        ramoChoice = request.POST['inputRamo']
        if coopForm.is_valid():
            coopForm.save()
            secondaryForm = switch_form(ramoChoice)
            return render(request, 'agendamento/novo2.html', {
                'ramos': ramos,
                'primaryFormSet': 'disabled111',
                'selected': ramoChoice,
                'cooperativaForm': coopForm,
                'seguradoForm': SeguradoForm})

    else:
        render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'collapseOpt': 4})
    return render(request, 'agendamento/novo2.html', {
    'cooperativaForm': CooperativaForm,
    'empresarialForm': EmpresarialForm,
    'collapseOpt': 3,
    'ramos':ramos})

def cadastro_segurado(request):
    if request.method == "POST":
        seguradoForm = SeguradoForm(request.POST)
        if seguradoForm.is_valid():
            seguradoForm.save()
            segurado = Segurado.objects.get(cnpj=seguradoForm.cleaned_data['cnpj'])
            return  redirect('cadastro_frota', pk=segurado.pk)

    return render(request, 'agendamento/novo2.html', {
    'seguradoForm': SeguradoForm,
    'error': segurado})


def cadastro_frota(request, pk):
    segurado = get_object_or_404(Segurado, pk=pk)
    if request.method == "POST":
        frotaForm = FrotaForm(request.POST)
        if frotaForm.is_valid():
            frota = frotaForm.save(commit=False)
            seg = Segurado.objects.get(id=pk)
            frota.segurado_id = seg.id
            frota.save()
            return render(request, 'agendamento/novo2.html', {
                'secondaryForm': frotaForm,
                'secondaryFormTemplate': 'frota_form.html',
                'error': frota.segurado_id})
        return render(request, 'agendamento/novo2.html', {
            'secondaryForm': frotaForm,
            'secondaryFormTemplate': 'frota_form.html',
            'error': frotaForm})
    return render(request, 'agendamento/novo2.html', {
    'secondaryForm': FrotaForm,
    'secondaryFormTemplate': 'frota_form.html',
    'error': segurado})


def relatorio_cooperativa(request):
    cooperativas = Cooperativa.objects.all().order_by('cooperativa')
    return render(request, 'relatorios/cooperativa.html', {
    'cooperativas': cooperativas
    })

def relatorio_segurado(request):
    segurados = Segurado.objects.all().order_by('nome')
    return render(request, 'relatorios/segurado.html', {
    'segurados': segurados
    })

def relatorio_frota(request):
    frotas = Frota.objects.all().order_by('segurado')
    return render(request, 'relatorios/frota.html', {
    'frotas': frotas,
    })
