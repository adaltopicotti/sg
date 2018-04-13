from django.db import models

# Create your models here. s




class Cooperativa(models.Model):
    cooperativa = models.CharField(max_length=200, null=False)
    agencia = models.CharField(max_length=200, null=False, unique=True)
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
    cnpj = models.CharField(max_length=14, unique=True, null=False )

    endereco = models.CharField(max_length=200, null= False)
    municipio = models.CharField(max_length=100, null=False)

    def __str__(self):
        return  self.nome

class Ramo(models.Model):
    TYPE_CHOICES = (
        ('Empresarial', 'Empresarial',),
        ('Vida', 'Vida',),
        ('Frota', 'Frota',),
    )
    nome = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return self.nome

class Empresarial(models.Model):
    atividade = models.CharField(max_length=200, null=False)
    qnt_local_risco = models.IntegerField(null=False)
    IS = models.FloatField(null=False)
    renovacao_cia = models.CharField(max_length=200)
    final_vigencia = models.DateField(("Date"), null=False )

class VidaGrupo(models.Model):
    TYPE_CHOICES = (
        ('GLOBAL', 'Global',),
        ('ESPECIFICA', 'Específica',),
    )
    tipo = models.CharField(max_length=20, choices=TYPE_CHOICES)
    IS = models.FloatField(null=False)
    atividade = models.CharField(max_length=200, null=False)
    qnt_vida_seg = models.IntegerField(null=False)
    renovacao_cia = models.CharField(max_length=200)
    final_vigencia = models.DateField(("Date"), null=False )

class VeiculoTipo(models.Model):
    CHOICES = (
        ('Leve', 'Leve'),
        ('Pesado', 'Pesado'),
    )
    name = models.CharField(max_length=20,choices=CHOICES, unique=True)

    def __str__(self):
        return self.name

class Frota(models.Model):
    segurado = models.ForeignKey(Segurado, on_delete=models.CASCADE)
    tipo_leve = models.BooleanField(blank=True, default=False)
    tipo_pesado = models.BooleanField(blank=True, default=False)
    qnt_itens_seg = models.IntegerField(null=False)
    renovacao_cia = models.CharField(max_length=200)
    final_vigencia = models.DateField(("Date"), null=False)
    def __str__(self):
        return self.segurado.nome


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
    tipo_empresa = models.ManyToManyField(TransporteTipo)
    cobertura = models.ManyToManyField(TransporteCobertura)
    IS = models.FloatField(null=False)
    mercadoria_transportada = models.CharField(max_length=200, null=False)
    renovacao_cia = models.CharField(max_length=200)
    final_vigencia = models.DateField(("Date"), null=False)

class Produto(models.Model):
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):

    #name = models.CharField(max_length=20,choices=CHOICES, unique=True)
    cooperativa = models.ForeignKey(Cooperativa,on_delete=models.CASCADE)
    segurado = models.ForeignKey(Segurado,on_delete=models.CASCADE)
    ramo = models.ForeignKey(Ramo,on_delete=models.CASCADE)
    bem = models.IntegerField(null=False)
    colaborador = models.CharField(max_length=200)
    pa = models.CharField(max_length=200)
    inclusao = models.DateField(("Date"))
    observacao = models.TextField(max_length=500)

    def __str__(self):
        title = self.cooperativa + " - " + self.segurado + " - " + self.ramo
        return title
