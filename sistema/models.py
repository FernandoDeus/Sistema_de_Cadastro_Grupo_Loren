from django.db import models

# Create your models here.

class cadastro(models.Model):
    nome_projeto = models.CharField(max_length=60)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    valor_projeto = models.FloatField()
    participante = models.CharField(max_length=150)


