from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
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
        seguradoForm = SeguradoForm(request.POST)
        ramoChoice = request.POST['inputRamo']
        cooperativa = Cooperativa.objects.get(agencia=coopForm['agencia'].value())
        if Cooperativa.objects.get(agencia=coopForm['agencia'].value()):
            if seguradoForm.is_valid():
                seguradoForm.save()
                segurado = Segurado.objects.get(cnpj=seguradoForm.cleaned_data['cnpj'])
                return redirect('cadastro_frota',pk=segurado.pk)
            return render(request, 'agendamento/novo2.html', {
                'ramos': ramos,
                'cooperativaForm': coopForm,
                'seguradoForm': seguradoForm,
                'segurado':(cooperativa, coopForm['agencia'].value())})

        elif coopForm.is_valid(): #tentar com if in
            coopForm.save()
            secondaryForm = switch_form(ramoChoice)
            if seguradoForm.is_valid():
                return render(request, 'agendamento/novo2.html', {
                    'ramos': ramos,
                    'cooperativaForm': coopForm,
                    'seguradoForm': seguradoForm,})
            return render(request, 'agendamento/novo2.html', {
                'ramos': ramos,
                'cooperativaForm': coopForm,
                'seguradoForm': SeguradoForm,})


    else:
        render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'collapseOpt': 4})
    return render(request, 'agendamento/novo2.html', {
    'cooperativaForm': CooperativaForm,
    'empresarialForm': EmpresarialForm,
    'collapseOpt': 3,
    'ramos':ramos})

def cadastro_segurado(request, coopForm):
    if request.method == "POST":
        seguradoForm = SeguradoForm(request.POST)
        if seguradoForm.is_valid():
            seguradoForm.save()
            segurado = Segurado.objects.get(cnpj=seguradoForm.cleaned_data['cnpj'])
            return  redirect('cadastro_frota', pk=segurado.pk)

    return render(request, 'agendamento/novo2.html', {
    'coopForm': coopForm,
    'seguradoForm': SeguradoForm,
    'error': segurado})

def cadastro_agendamento(request):
    ramos = Ramo.objects.all().order_by('nome')
    if request.method == "POST":
        ramoChoice = request.POST['inputRamo']
        cooperativaForm = CooperativaForm(request.POST)
        secondaryForm = switch_form(ramoChoice)
        if cooperativaForm.is_valid():
            cooperativaForm.save()
            return render(request, 'agendamento/novo2.html', {
                'selected': ramoChoice,
                'cooperativaForm': cooperativaForm,
                'seguradoForm': SeguradoForm,
                'ramos':ramos})
        elif Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value()) in Cooperativa.objects.all():
            #include_agendamento(coop_id, seg_id, ramo_id, bem)
            try:
                seguradoForm = SeguradoForm(request.POST)
                if seguradoForm.is_valid():
                    seguradoForm.save()
                elif Segurado.objects.get(cnpj=seguradoForm['cnpj'].value()) in Segurado.objects.all():
                    #coop = Cooperativa.objects.get(agencia=cooperativaForm['agencia'].value())
                    seg = Segurado.objects.get(cnpj=seguradoForm['cnpj'].value())
                    ramo = Ramo.objects.get(nome=ramoChoice)
            except:
                return render(request, 'agendamento/novo2.html', {
                    'selected': ramoChoice,
                    'cooperativaForm': cooperativaForm,
                    'seguradoForm': SeguradoForm,
                    'ramos':ramos})
        return render(request, 'agendamento/novo2.html', {
            'selected': ramoChoice,
            'cooperativaForm': cooperativaForm,
            'seguradoForm': SeguradoForm,
            'ramos':ramos})

    return render(request, 'agendamento/novo2.html', {
        'cooperativaForm': CooperativaForm,
        'ramos':ramos})

def include_agendamento(coop_id, seg_id, ramo_id, bem):
    agendForm = AgendamentoForm()
    agendamento = agendForm.save(commit=False)
    agendamento.cooperativa_id = coop_id
    agendamento.segurado_id = seg_id
    agendamento.ramo_id = ramo_id
    agendamento.bem = bem
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
