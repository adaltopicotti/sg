from django import forms
from .models import *

class CooperativaForm(forms.ModelForm):

    cooperativa = forms.CharField(label='Cooperativa',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputCooperativa',}))
    agencia = forms.CharField(label='Agência',widget=forms.TextInput(
        attrs={'type':'text', 'class':'form-control', 'id':'inputAgencia'}))
    solicitante = forms.CharField(label='Solicitante',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSolicitante'}))
    email = forms.EmailField(label='E-Mail',widget=forms.EmailInput(
        attrs={'class':'form-control', 'id':'inputSolEmail', 'placeholder':'exemplo@exemplo.com'}))
    telefone = forms.CharField(label='Telefone',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSolTelefone'}))
    celular = forms.CharField(label='Celular',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSolCelular'}))

    class Meta:
        model = Cooperativa
        fields = ('cooperativa', 'agencia', 'solicitante', 'email', 'telefone', 'celular',)


class RamoForm(forms.ModelForm):
    nome = forms.ModelChoiceField(label="Ramo",
        queryset=Ramo.objects.all().order_by('nome'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True)
    class Meta:
        model = Ramo
        fields = ('nome',)

#segurado
class SeguradoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegNome'}))
    email = forms.EmailField(label='E-Mail',widget=forms.EmailInput(
        attrs={'class':'form-control', 'id':'inputSegEmail', 'placeholder':'exemplo@exemplo.com'}))
    telefone = forms.CharField(label='Telefone',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegTelefone'}))
    celular = forms.CharField(label='Celular',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegCelular'}))
    cnpj = forms.CharField(label='CNPJ',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegCNPJ', 'autofocus':'autofocus' }))
    endereco = forms.CharField(label='Endereço',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegEndereco'}))
    municipio = forms.CharField(label='Municipio',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegMunicipio'}))

    class Meta:
        model = Segurado
        fields = ('nome', 'email','telefone', 'celular', 'cnpj', 'endereco', 'municipio',)



class EmpresarialForm(forms.ModelForm):
    atividade = forms.CharField(label='Atividade',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputEmpAtividade', 'autofocus':'autofocus'}))
    qnt_local_risco = forms.CharField(label='Qnt de Locais de Risco',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputEmpQntLRisc'}))
    IS = forms.CharField(label='Importância Segurada',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputEmpIS'}))
    renovacao_cia = forms.CharField(label='Renovação - Seguradora',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputEmpRenovacaoCia'}))

    class Meta:
        model = Empresarial
        fields = ('atividade', 'qnt_local_risco', 'IS', 'renovacao_cia',)


class FrotaForm(forms.ModelForm):
    tipo_leve = forms.BooleanField(label='Leve', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    tipo_pesado = forms.BooleanField(label='Pesado', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))

    qnt_itens_seg = forms.CharField(label='Quantidade de Itens',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputFrotaQntItem'}))
    renovacao_cia = forms.CharField(label='Renovação - Seguradora',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputFrotaRenovacaoCia'}))
    final_vigencia = forms.CharField(label='Final de Vigência',widget=forms.TextInput(
        attrs={'type':'date', 'class':'form-control', 'id':'inputFrotaFinalVig'}))


    class Meta:
        model = Frota
        fields = ( 'tipo_leve', 'tipo_pesado', 'qnt_itens_seg', 'renovacao_cia', 'final_vigencia',)


class TransporteForm(forms.ModelForm):
    tipo_comum = forms.BooleanField(label='Comum', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    tipo_transportadora = forms.BooleanField(label='Transportadora', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    tipo_nacional = forms.BooleanField(label='Nacional', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    tipo_internacional = forms.BooleanField(label='Internacional', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    cobertura_acidente = forms.BooleanField(label='Acidente', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    cobertura_roubo = forms.BooleanField(label='Roubo', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    IS = forms.CharField(label='Importância Segurada',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputTranspIS'}))
    mercadoria_transportada = forms.CharField(label='Mercadoria Transportada',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputTranspMercadoria'}))
    renovacao_cia = forms.CharField(label='Renovação - Seguradora',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputTranspRenovacaoCia'}))


    class Meta:
        model = Transporte
        fields = (
            'tipo_transportadora',
            'tipo_comum',
            'tipo_nacional',
            'tipo_internacional',
            'cobertura_acidente',
            'cobertura_acidente',
            'IS',
            'mercadoria_transportada',
            'renovacao_cia')



class BemForm(forms.ModelForm):

    class Meta:
        model = Bem
        fields = ( 'protocol',)

class AgendamentoForm(forms.ModelForm):
    colaborador = forms.CharField(label='Colaborador', required=False, widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputColaborador'}))
    pa = forms.CharField(label='Ponto de Ação', required=False, widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputPA'}))
    final_vigencia = forms.CharField(label='Final de Vigência',widget=forms.TextInput(
        attrs={'type':'date', 'class':'form-control', 'id':'inputAgendamentoFinalVig'}))
    observacao = forms.CharField(label='Observação', required=False, widget=forms.Textarea(
        attrs={'class':'form-control', 'id':'inputObservacao'}))

    class Meta:
        model = Agendamento
        fields = ( 'colaborador', 'pa', 'final_vigencia', 'observacao',)


class VidaForm(forms.ModelForm):
    TYPE_CHOICES = (
        ('GLOBAL', 'Global',),
        ('ESPECIFICA', 'Específica',),
    )
    tipo = forms.CharField(label='Tipo', widget=forms.Select(choices=TYPE_CHOICES,
        attrs={'class':'form-control', 'id':'inputColaborador'} ))
    IS = forms.DecimalField(label='Importância Segurada',widget=forms.NumberInput(
        attrs={'class':'form-control', 'id':'inputVidaIS'}))
    atividade_empresa = forms.CharField(label='Atividade da Empresa',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputAtividadeEmpresa'}))
    qnt_vida_seg = forms.CharField(label='Quantidade de Vida',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputVidaQnt'}))
    renovacao_cia = forms.CharField(label='Renovação - Seguradora',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputVidaRenovacaoCia'}))
    class Meta:
        model = Vida
        fields = ('tipo', 'IS', 'atividade_empresa', 'qnt_vida_seg','renovacao_cia')

class AgendamentoPostForm(forms.ModelForm):

    class Meta:
        model = AgendamentoPost
        fields = ('text',)
