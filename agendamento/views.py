from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from agendamento.forms import *
from agendamento.models import *
# Create your views here.


def switch_form(argument):
    switcher = {
        "Frota": ["frota_form.html", FrotaForm, Frota, 'FRT'],
        "Empresarial": ["emp_form.html", EmpresarialForm, Empresarial, 'EMP'],
        "Transporte": ["transp_form.html", '', Transporte, 'TRN'],

    }
    return switcher.get(argument)

def cadastro_segurado(request, coopForm):
    # CRIAR TEMPLATE PARA CADASTRO INDIVIDUAL DO SEGURADO
    return render()


def cadastro_agendamento(request):
    ramos = Ramo.objects.all().order_by('nome')
    dataRender = {
        'ramoChoice': '',
        'cooperativaForm': CooperativaForm,
        'seguradoForm': '',
        'secondaryFormTemplate': '',
        'ramos':ramos}

    coop_pk = 0
    seg_pk = 0
    secondary_pk = 0
    if request.method == "POST":
        ramoChoice = request.POST['inputRamo']
        cooperativaForm = CooperativaForm(request.POST)
        seguradoForm = SeguradoForm(request.POST)
        secondarySwitch = switch_form(ramoChoice)
        if cooperativaForm.is_valid():
            try:
                cooperativa = Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value())
                #include_agendamento(coop_id, seg_id, ramo_id, bem)
            except Cooperativa.DoesNotExist:
                cooperativaForm.save()
            dataRender['cooperativaForm'] = cooperativaForm
            dataRender['seguradoForm'] = SeguradoForm
            dataRender['ramoChoice'] = ramoChoice

        if seguradoForm.is_valid():
            try:
                segurado = Segurado.objects.get(cnpj=seguradoForm['cnpj'].value())
            except Segurado.DoesNotExist:
                seguradoForm.save()
            dataRender['seguradoForm'] = seguradoForm
            dataRender['agendamentoForm'] = AgendamentoForm
            dataRender['secondaryForm'] = secondarySwitch[1](request.POST)
            dataRender['secondaryFormTemplate'] = secondarySwitch[0]
            secondaryModel = secondarySwitch[2]

        if 'secondaryForm' in dataRender.keys():
            if dataRender['secondaryForm'].is_valid():
                agendamentoForm = AgendamentoForm(request.POST)
                cooperativa = Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value())
                segurado = Segurado.objects.get(cnpj=seguradoForm['cnpj'].value())
                ramo_id = Ramo.objects.get(nome=ramoChoice).id
                coop_pk = cooperativa.pk
                seg_pk = segurado.pk
                segToForm = Segurado.objects.get(id=seg_pk)
                secondaryForm = dataRender['secondaryForm'].save(commit=False)
                secondaryForm.segurado_id = segToForm.id
                try:
                    ramo_protocol = "{0}{1}".format(secondarySwitch[3], str(secondaryModel.objects.all().latest('id').id +1))
                except secondaryModel.DoesNotExist:
                    ramo_protocol = "{0}{1}".format(secondarySwitch[3], 1)
                secondaryForm.protocol = ramo_protocol
                secondaryForm.save()
                bem_protocol = include_bem(seg_pk, ramo_id, ramo_protocol)
                bem = Bem.objects.get(protocol=bem_protocol)
                if agendamentoForm.is_valid():
                    include_agendamento(agendamentoForm, coop_pk, seg_pk, ramo_id, bem,  bem_protocol)
                    dataRender['agendamentoForm'] = agendamentoForm

    return render(request, 'agendamento/novo2.html', dataRender)


def include_bem(seg_id, ramo_id, ramo_protocol):
    bemForm = BemForm()
    bem = bemForm.save(commit=False)
    try:
        bem.protocol = 10111000000 + (Bem.objects.all().latest('id').id +1)
    except Bem.DoesNotExist:
        bem.protocol =  1011100001
    bem.segurado_id = seg_id
    bem.ramo_id = ramo_id
    bem.ramo_protocol = ramo_protocol
    bem.save()
    return bem.protocol

def include_agendamento(form, coop_id, seg_id, ramo_id, bem, bem_protocol):
    agendForm = form
    agendamento = form.save(commit=False)
    agendamento.cooperativa_id = coop_id
    agendamento.segurado_id = seg_id
    agendamento.ramo_id = ramo_id
    agendamento.bem_id = bem.id
    agendamento.colaborador = 'Usuário'
    agendamento.inclusao = timezone.now()
    agendamento.protocol = (bem_protocol)
    agendamento.save()

def cadastro_frota(request, pk):

    return render()


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

def relatorio_agendamento(request):
    agendamentos = Agendamento.objects.all().order_by('protocol')

    return render(request, 'relatorios/agendamento.html', {
    'agendamentos': agendamentos,
    })
