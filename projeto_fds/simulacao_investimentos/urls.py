from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_simulacao, name='adicionar_simulacao'),
    path('investimentos/', views.listar_investimentos, name='listar_investimentos'),
]
