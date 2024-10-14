from django.urls import path
from .views import calcular_imposto

urlpatterns = [
    path('calculo/', calcular_imposto, name='calcular_imposto'),
]
