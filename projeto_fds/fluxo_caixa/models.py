from django.db import models
from django.contrib.auth.models import User

class FluxoCaixa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=20)  # Ex: "Janeiro 2024"
    ebit = models.DecimalField(max_digits=10, decimal_places=2)
    ir = models.DecimalField(max_digits=10, decimal_places=2)
    depreciacao = models.DecimalField(max_digits=10, decimal_places=2)
    receita_total = models.DecimalField(max_digits=10, decimal_places=2)
    despesa_total = models.DecimalField(max_digits=10, decimal_places=2)
    fluxo_caixa_operacional = models.DecimalField(max_digits=10, decimal_places=2)
    data_calculo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.periodo}"
