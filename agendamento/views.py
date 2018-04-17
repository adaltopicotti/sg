from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from agendamento.forms import *
from agendamento.models import *
# Create your views here.


def switch_form(argument):
    switcher = {
        "Frota": ["frota_form.html", FrotaForm, Frota],
        "Empresarial": ["emp_form.html", EmpresarialForm, Empresarial],
        "Transporte": ["transp_form.html", ''],

    }
    return switcher.get(argument)

def cadastro_segurado(request, coopForm):
    # CRIAR TEMPLATE PARA CADASTRO INDIVIDUAL DO SEGURADO
    return render()


def cadastro_agendamento(request):
    ramos = Ramo.objects.all().order_by('nome')
    coop_pk = 0
    seg_pk = 0
    secondary_pk = 0
    if request.method == "POST":
        ramoChoice = request.POST['inputRamo']
        cooperativaForm = CooperativaForm(request.POST)
        seguradoForm = SeguradoForm(request.POST)
        secondarySwitch = switch_form(ramoChoice)
        secondaryForm = EmpresarialForm(self)
        secondaryFormTemplate = secondarySwitch[0]
        if cooperativaForm.is_valid():
            try:
                cooperativa = Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value())
                #include_agendamento(coop_id, seg_id, ramo_id, bem)
            except Cooperativa.DoesNotExist:
                cooperativaForm.save()

        if seguradoForm.is_valid():
            try:
                segurado = Segurado.objects.get(cnpj=seguradoForm['cnpj'].value())
            except Segurado.DoesNotExist:
                seguradoForm.save()
            secondaryForm = secondarySwitch[1](request.POST)
            secondaryModel = secondarySwitch[2]

        if secondaryForm.is_valid():
            cooperativa = Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value())
            segurado = Segurado.objects.get(cnpj=seguradoForm['cnpj'].value())
            ramo_id = Ramo.objects.get(nome=ramoChoice).id
            coop_pk = cooperativa.pk
            seg_pk = segurado.pk
            segToForm = Segurado.objects.get(id=seg_pk)
            secondary = secondaryForm.save(commit=False)
            secondary.segurado_id = segToForm.id
            protocol = (10000000 + (secondaryModel.objects.all().latest('id').id +1))
            secondary.protocol = protocol
            secondary.save()
            #verificar o que fazer utilizando cadastro_frota
            secondary_pk = secondaryModel.objects.get(protocol=protocol)

            include_agendamento(coop_pk, seg_pk, ramo_id, protocol)
        return render(request, 'agendamento/novo2.html', {
            'selected': ramoChoice,
            'cooperativaForm': cooperativaForm,
            'seguradoForm': seguradoForm,
            'secondaryForm': secondaryForm,
            'secondaryFormTemplate': secondaryFormTemplate,
            'ramos':ramos,
            'pk':secondary_pk})

    return render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'ramos':ramos})

def include_agendamento(coop_id, seg_id, ramo_id, secondary_pk):
    agendForm = AgendamentoForm()
    agendamento = agendForm.save(commit=False)
    agendamento.cooperativa_id = coop_id
    agendamento.segurado_id = seg_id
    agendamento.ramo_id = ramo_id
    agendamento.bem = secondary_pk
    agendamento.inclusao = timezone.now()
    agendamento.save()

def cadastro_frota(request, pk):
    segurado = get_object_or_404(Segurado, pk=pk)
    seguradoForm = SeguradoForm(initial={'nome': segurado.nome})
    if request.method == "POST":
        frotaForm = FrotaForm(request.POST)
        if frotaForm.is_valid():
            frota = frotaForm.save(commit=False)
            seg = Segurado.objects.get(id=pk)
            frota.segurado_id = seg.id
            frota.save()
            return render(request, 'agendamento/novo2.html', {
                'cooperativaForm': coopform,
                'secondaryForm': frotaForm,
                'secondaryFormTemplate': 'frota_form.html',
                'error': frota.segurado_id})
        return render(request, 'agendamento/novo2.html', {
            'secondaryForm': frotaForm,
            'secondaryFormTemplate': 'frota_form.html',
            'error': frotaForm})
    return render(request, 'agendamento/novo2.html', {
    'secondaryForm': FrotaForm,
    'seguradoForm':seguradoForm,
    'secondaryFormTemplate': 'frota_form.html',
    'error': segurado.nome})


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
