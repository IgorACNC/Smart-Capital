from django.db import models

class PlanejamentoAposentadoria(models.Model):
    idade_atual = models.IntegerField()
    idade_aposentadoria = models.IntegerField()
    meta_renda = models.DecimalField(max_digits=10, decimal_places=2)
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2, default=0) 

    def calcular_valor_mensal(self):
     
        anos_ate_aposentadoria = self.idade_aposentadoria - self.idade_atual
        
        if anos_ate_aposentadoria > 0:
            return self.meta_renda / (anos_ate_aposentadoria * 12)
        return 0

    def save(self, *args, **kwargs):
        if self.valor_mensal == 0:  
            self.valor_mensal = self.calcular_valor_mensal()
        super().save(*args, **kwargs)
