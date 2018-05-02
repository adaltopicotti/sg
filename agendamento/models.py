from django.db import models
from django.utils import timezone
# Create your models here. s




class Cooperativa(models.Model):
    cooperativa = models.CharField(max_length=200, null=False)
    agencia = models.CharField(max_length=200, null=False)
    solicitante = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=100, null=False)
    telefone = models.CharField(max_length=50, null=True)
    celular = models.CharField(max_length=50, null=True)


    def __str__(self):
        return  self.cooperativa


class Segurado(models.Model):
    nome = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=100, null=False)
    telefone = models.CharField(max_length=50, null=True)
    celular = models.CharField(max_length=50, null=True)
    cnpj = models.CharField(max_length=14, null=False )
    cep = models.CharField(max_length=10, null=False)
    endereco = models.CharField(max_length=200, null= False)
    municipio = models.CharField(max_length=100, null=False)

    def __str__(self):
        return  self.nome

class Ramo(models.Model):
    TYPE_CHOICES = (
        ('Empresarial', 'Empresarial',),
        ('Vida', 'Vida',),
        ('Frota', 'Frota',),
        ('Transporte', 'Transporte',),
    )
    nome = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.nome

class Empresarial(models.Model):
    protocol = models.CharField(max_length=20, null=False)
    atividade = models.CharField(max_length=200, null=False)
    qnt_local_risco = models.IntegerField(null=False)
    IS = models.FloatField(null=False)
    renovacao_cia = models.CharField(max_length=200)
    def __str__(self):
        return self.protocol

class Vida(models.Model):
    TYPE_CHOICES = (
        ('GLOBAL', 'Global',),
        ('ESPECIFICA', 'Específica',),
    )
    protocol = models.CharField(max_length=20, null=False)
    tipo = models.CharField(max_length=20, choices=TYPE_CHOICES)
    IS = models.DecimalField(null=False, max_digits=15, decimal_places=2)
    atividade_empresa = models.CharField(max_length=200, null=False)
    qnt_vida_seg = models.IntegerField(null=False)
    renovacao_cia = models.CharField(max_length=200)
    def __str__(self):
        return self.protocol

class VeiculoTipo(models.Model):
    CHOICES = (
        ('Leve', 'Leve'),
        ('Pesado', 'Pesado'),
    )
    name = models.CharField(max_length=20,choices=CHOICES, unique=True)

    def __str__(self):
        return self.name

class Frota(models.Model):
    protocol = models.CharField(max_length=20, null=False)
    tipo_leve = models.BooleanField(blank=True, default=False)
    tipo_pesado = models.BooleanField(blank=True, default=False)
    qnt_itens_seg = models.IntegerField(null=False)
    renovacao_cia = models.CharField(max_length=200)
    def __str__(self):
        return self.protocol


class TransporteTipo(models.Model):
    CHOICES = (
        ('Transportadora', 'Transportadora'),
        ('Comum', 'Empresa Comum'),
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    )
    name = models.CharField(max_length=20,choices=CHOICES, unique=True)

    def __str__(self):
        return self.name

class TransporteCobertura(models.Model):
    CHOICES = (
        ('Acidente', 'Acidente'),
        ('Roubo', 'Roubo'),
    )
    name = models.CharField(max_length=20,choices=CHOICES, unique=True)

    def __str__(self):
        return self.name

class Transporte(models.Model):
    protocol = models.CharField(max_length=20)
    tipo_comum = models.BooleanField(blank=True, default=False)
    tipo_transportadora = models.BooleanField(blank=True, default=False)
    tipo_nacional = models.BooleanField(blank=True, default=False)
    tipo_internacional = models.BooleanField(blank=True, default=False)
    cobertura_acidente = models.BooleanField(blank=True, default=False)
    cobertura_roubo = models.BooleanField(blank=True, default=False)
    IS = models.FloatField(null=False)
    mercadoria_transportada = models.CharField(max_length=200, null=False)
    renovacao_cia = models.CharField(max_length=200)

    def __str__(self):
        return self.protocol

class Produto(models.Model):
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nome

class Bem(models.Model):
    protocol = models.CharField(max_length=20)
    segurado = models.ForeignKey(Segurado,on_delete=models.CASCADE)
    ramo = models.ForeignKey(Ramo,on_delete=models.CASCADE)
    ramo_protocol = models.CharField(max_length=20)
    def __str__(self):
        return self.protocol

class Agendamento(models.Model):
    protocol = models.TextField(max_length=20, null=False)
    #name = models.CharField(max_length=20,choices=CHOICES, unique=True)
    cooperativa = models.ForeignKey(Cooperativa,on_delete=models.CASCADE)
    segurado = models.ForeignKey(Segurado,on_delete=models.CASCADE)
    ramo = models.ForeignKey(Ramo,on_delete=models.CASCADE)
    bem = models.ForeignKey(Bem,on_delete=models.CASCADE)
    colaborador = models.CharField(max_length=200)
    pa = models.CharField(max_length=200)
    final_vigencia = models.DateField(("Date"), null=False)
    inclusao = models.DateField(("Date"))
    observacao = models.TextField(max_length=500)

    def __str__(self):
        return self.protocol


class AgendamentoPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.agendamento.protocol
