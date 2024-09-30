from django.db import models
from django.contrib.auth.models import User

class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def str(self):
        return f'{self.descricao} - {self.valor}'