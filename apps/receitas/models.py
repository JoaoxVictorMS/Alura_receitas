from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Receita(models.Model):
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)   
    publicada = models.BooleanField(default=False)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_receita