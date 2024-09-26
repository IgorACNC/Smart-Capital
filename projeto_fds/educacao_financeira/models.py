from django.db import models

class Aula(models.Model):
    titulo = models.CharField(max_length=200)
    numero = models.IntegerField()  # Número da aula (ex: Aula 1, Aula 2)
    conteudo = models.TextField()  # Conteúdo da aula
    youtube_id = models.CharField(max_length=50, blank=True, null=True)  # ID do YouTube

    def __str__(self):
        return f"Aula {self.numero}: {self.titulo}"


class Resumo(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE) 
    conteudo = models.TextField()

    def __str__(self):
        return f'Resumo de {self.aula.titulo}'