from django.urls import path
from . import views

urlpatterns = [
    path('calculo/', views.calcular_fluxo_caixa, name='calcular_fluxo_caixa'),
    path('historico/', views.historico_fluxo_caixa, name='historico_fluxo_caixa'),
]
