from django import forms
from .models import Cooperativa, Segurado, Empresarial

class CooperativaForm(forms.ModelForm):

    cooperativa = forms.CharField(label='Cooperativa',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputCooperativa'}))
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
        fields = ('cooperativa',)


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
        attrs={'class':'form-control', 'id':'inputSegCNPJ'}))
    endereco = forms.CharField(label='Endereço',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegEndereco'}))
    municipio = forms.CharField(label='Municipio',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegMunicippio'}))

    class Meta:
        model = Segurado
        fields = ('nome',)


class EmpresarialForm(forms.ModelForm):
    atividade = forms.CharField(label='Atividade',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputEmpAtividade'}))
    qnt_local_risco = forms.CharField(label='Quantidade de Locais de Risco',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputEmpQntLRisc'}))
    IS = forms.CharField(label='Importância Segurada',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputEmpIS'}))
    renovacao_cia = forms.CharField(label='Renovação - Seguradora',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputEmpRenovacaoCia'}))
    final_vigencia = forms.CharField(label='Final de Vigência',widget=forms.TextInput(
        attrs={'type':'date', 'class':'form-control', 'id':'inputEmpFinalVig'}))

    class Meta:
        model = Empresarial
        fields = ('atividade',)
