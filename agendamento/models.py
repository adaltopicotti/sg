from django.db import models

# Create your models here.

class Agendamento(models.Model):
    cliente = models.CharField(max_length=200, null=False)
    agencia = models.CharField(max_length=200, null=False)
    inicio_vigencia = models.DateField(("Date"), blank=False)
    fim_vigencia = models.DateField(("Date"), blank=False)
    acao = models.TextField(max_length=500, null=True)

    def __str__(self):
        return  self.cliente
