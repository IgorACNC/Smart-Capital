from django.db import models
from django.contrib.auth.models import User

class SimulacaoInvestimento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_investimento = models.DecimalField(max_digits=10, decimal_places=2)
    periodo_investimento = models.IntegerField()
    perfil_risco = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.valor_investimento} - {self.periodo_investimento} meses"
