from django import forms
from .models import Cooperativa

class CooperativaForm(forms.ModelForm):

    cooperativa = forms.CharField(label='Cooperativa',widget=forms.TextInput(
        attrs={'class':'form-control'}))
    agencia = forms.CharField(label='Agência',widget=forms.TextInput(
        attrs={'class':'form-control'}))
    solicitante = forms.CharField(label='Solicitante',widget=forms.TextInput(
        attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-Mail',widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'exemplo@exemplo.com'}))
    telefone = forms.CharField(label='Telefone',widget=forms.TextInput(
        attrs={'class':'form-control'}))
    celular = forms.CharField(label='Celular',widget=forms.TextInput(
        attrs={'class':'form-control'}))

    class Meta:
        model = Cooperativa
        fields = ('cooperativa',)
