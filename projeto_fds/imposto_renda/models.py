from django.db import models

class ImpostoRenda(models.Model):
    nome = models.CharField(max_length=100)
    renda_anual = models.DecimalField(max_digits=10, decimal_places=2)
    imposto_calculado = models.DecimalField(max_digits=10, decimal_places=2)
    data_calculo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - R$ {self.imposto_calculado}'

