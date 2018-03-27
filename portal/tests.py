from django.test import TestCase

# Create your tests here.
class Imagem(models.Model):
    titulo = models.CharField(max_length = 200)
    conteudo = models.TextField()
    logo = models.ImageField()
