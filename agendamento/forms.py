from django import forms
from .models import *

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
        attrs={'class':'form-control', 'id':'inputSegCNPJ'}))
    endereco = forms.CharField(label='Endereço',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegEndereco'}))
    municipio = forms.CharField(label='Municipio',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputSegMunicipio'}))

    class Meta:
        model = Segurado
        fields = ('nome', 'email','telefone', 'celular', 'cnpj', 'endereco', 'municipio',)



class EmpresarialForm(forms.ModelForm):
    atividade = forms.CharField(label='Atividade',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputEmpAtividade'}))
    qnt_local_risco = forms.CharField(label='Quantidade de Locais de Risco',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputEmpQntLRisc'}))
    IS = forms.CharField(label='Importância Segurada',widget=forms.TextInput(
        attrs={'type':'number', 'class':'form-control', 'id':'inputEmpIS'}))
    renovacao_cia = forms.CharField(label='Renovação - Seguradora',widget=forms.TextInput(
        attrs={'class':'form-control', 'id':'inputEmpRenovacaoCia'}))
    final_vigencia = forms.CharField(label='Final de Vigência',widget=forms.TextInput(
        attrs={'type':'date', 'class':'form-control', 'id':'inputEmpFinalVig'}))

    class Meta:
        model = Empresarial
        fields = ('atividade', 'qnt_local_risco', 'IS', 'renovacao_cia', 'final_vigencia')


class FrotaForm(forms.ModelForm):
    tipo_leve = forms.CharField(label='Leve', required=False, widget=forms.CheckboxInput(
    attrs={'class':'form-control'}))
    tipo_pesado = forms.CharField(label='Pesado', required=False, widget=forms.CheckboxInput(
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
