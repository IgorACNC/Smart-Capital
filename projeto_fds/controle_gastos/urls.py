from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos, name='home'),
    path('visualizar/', views.visualizar_gastos, name='visualizar_gastos'),
    path('adicionar/', views.add_gastos, name='add_gastos'),
    path('gastos/excluir/<int:id>/', views.excluir_gasto, name='excluir_gasto'),
]