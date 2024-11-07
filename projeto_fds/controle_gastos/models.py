from django.db import models
from django.contrib.auth.models import User

class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f'{self.descricao} - {self.valor}'


class MetaGasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_meta = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Meta de {self.valor_meta}'

    def checar_valor_ultrapassado(self, total_gastos):
        return total_gastos >= self.valor_meta

class FiltroGasto(models.Model):
    CATEGORIAS = [
        ('roupa', 'Roupa'),
        ('eletronico', 'Eletrônico'),
        ('comida', 'Comida'),
    ]
    gasto = models.ForeignKey(Gasto, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    
    def __str__(self):
        return f"{self.gasto.descricao} - {self.categoria}"
