from django.db import models

# Create your models here.
class Planilha(models.Model):
    nome = models.CharField(max_length=50)
    cliente = models.CharField(max_length=50)
    arquivo = models.FileField()
    