from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from portal.models import ValidateLogin

class ValidateLoginForm(forms.ModelForm):
	class Meta:
		model = ValidateLogin
		fields = ('login', 'password', 'token')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Informe seu usuário.',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'type':'login', 'placeholder':'Digite seu usuário...'}))
    password = forms.CharField(max_length=30, required=False, help_text='Informe sua senha.',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'type':'password', 'placeholder':'Digite sua senha...'}))
