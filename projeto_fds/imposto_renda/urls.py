from django.urls import path
from .views import calcular_imposto, historico_calculos

urlpatterns = [
    path('calculo/', calcular_imposto, name='calculo_imposto'),
    path('historico/', historico_calculos, name='historico'),
]
