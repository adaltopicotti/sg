from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from agendamento.forms import *
from agendamento.models import *
# Create your views here.

# TO DO

# TODO: Incluir agenda de ações realizadas  no Agendamento Detail
# TODO: Visualização de Agendamento, tentar utilizando tables
# TODO: Criar link no relatorio (frota, empresarial, transporte, vida) para indicar o segurado ou agendamento
# END TO DO


def teste(request):
    return render(request, 'portal/structure/teste.html', {
    })

def switch_form(argument):
    switcher = {
        "Frota": ["frota_form.html", FrotaForm, Frota, 'FRT'],
        "Empresarial": ["emp_form.html", EmpresarialForm, Empresarial, 'EMP'],
        "Transporte": ["transporte_form.html", TransporteForm, Transporte, 'TRN'],
        "Vida": ["vida_form.html", VidaForm, Vida, 'VID'],
    }
    return switcher.get(argument)

def cadastro_segurado(request, coopForm):
    # CRIAR TEMPLATE PARA CADASTRO INDIVIDUAL DO SEGURADO
    return render()


def cadastro_agendamento(request):
    ramos = Ramo.objects.all().order_by('nome')
    dataRender = {
        'primaryFormSet':'',
        'secondaryFormSet':'',
        'ramoChoice': '',
        'cooperativaForm': CooperativaForm,
        'seguradoForm': '',
        'secondaryFormTemplate': '',
        'ramos':ramos}

    coop_pk = 0
    seg_pk = 0
    secondary_pk = 0
    if request.method == "POST":

        cooperativaForm = CooperativaForm(request.POST)
        seguradoForm = SeguradoForm(request.POST)
        if cooperativaForm.is_valid():
            try:
                cooperativa = Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value())
                #include_agendamento(coop_id, seg_id, ramo_id, bem)
            except Cooperativa.DoesNotExist:
                cooperativaForm.save()
            dataRender['cooperativaForm'] = cooperativaForm
            dataRender['seguradoForm'] = SeguradoForm


        if seguradoForm.is_valid():
            try:
                segurado = Segurado.objects.get(cnpj=seguradoForm['cnpj'].value())
            except Segurado.DoesNotExist:
                seguradoForm.save()
            #dataRender['primaryFormSet'] = 'disabled'
            ramoChoice = request.POST['inputRamo']
            secondarySwitch = switch_form(ramoChoice)
            dataRender['ramoChoice'] = ramoChoice
            dataRender['seguradoForm'] = seguradoForm
            dataRender['agendamentoForm'] = AgendamentoForm
            dataRender['secondaryForm'] = secondarySwitch[1](request.POST)
            dataRender['secondaryFormTemplate'] = secondarySwitch[0]
            dataRender['primaryFormSet'] = 'collapse'
            dataRender['verif'] = str(secondarySwitch[1])
            secondaryModel = secondarySwitch[2]

        if 'secondaryForm' in dataRender.keys():
            if dataRender['secondaryForm'].is_valid():
                agendamentoForm = AgendamentoForm(request.POST)
                cooperativa = Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value())
                segurado = Segurado.objects.get(cnpj=seguradoForm['cnpj'].value())
                ramo_id = Ramo.objects.get(nome=ramoChoice).id
                coop_pk = cooperativa.pk
                seg_pk = segurado.pk
                secondaryForm = dataRender['secondaryForm'].save(commit=False)
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
        bem.protocol = 10111000001
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


def detail_agendamento(request, protocol):
    agendamento = Agendamento.objects.get(protocol=protocol)
    bem = switch_form(agendamento.bem.ramo.nome)
    # TODO Será necessário criar duas versões de SecondaryDetail
    #form = JournalForm(initial={'tank': 123})
    secondaryModel = bem[2].objects.get(protocol=agendamento.bem.ramo_protocol)
    agendamentoPost = AgendamentoPost.objects.filter(agendamento=agendamento)
    agendamentoPostForm = AgendamentoPostForm
    if request.method == "POST":
        form = agendamentoPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.agendamento = agendamento
            post.author = request.user
            post.save()
            agendamentoPostForm = AgendamentoPostForm
    return render(request, 'detail/agendamento.html', {
        'agendamento': agendamento,
        'secondaryModel': secondaryModel,
        'agendamentoPosts': agendamentoPost,
        'agendamentoPostForm': agendamentoPostForm
    })

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
    frotas = Frota.objects.all().order_by('protocol')
    return render(request, 'relatorios/frota.html', {
    'frotas': frotas,
    })

def relatorio_agendamento(request):
    agendamentos = Agendamento.objects.all().order_by('protocol')

    return render(request, 'relatorios/agendamento.html', {
    'agendamentos': agendamentos,
    })
