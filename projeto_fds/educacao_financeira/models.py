from django.contrib.auth.models import User
from django.db import models

class Aula(models.Model):
    titulo = models.CharField(max_length=200)
    numero = models.IntegerField() 
    conteudo = models.TextField()  
    youtube_id = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return f"Aula {self.numero}: {self.titulo}"


class Resumo(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE) 
    conteudo = models.TextField()
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # Campo do usuário

    def __str__(self):
        return f'Resumo de {self.aula.titulo}'