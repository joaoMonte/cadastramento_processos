from django.db import models

# Create your models here.
class Processo(models.Model):
    pasta = models.CharField(max_length=50)
    comarca = models.CharField(max_length=50)
    uf = models.CharField(max_length=50)
    