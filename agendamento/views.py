from django.shortcuts import render
from agendamento.forms import CooperativaForm
# Create your views here.

def agendamento_novo(request):
    return render(request, 'agendamento/novo.html', {'form': CooperativaForm} )
