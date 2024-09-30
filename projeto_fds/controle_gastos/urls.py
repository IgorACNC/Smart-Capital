from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos, name='gastos'),
    path('visualizar/', views.visualizar_gastos, name='visualizar_gastos'),
    path('adicionar/', views.add_gastos, name='add_gastos'),
    path('excluir/<int:id>/', views.excluir_gasto, name='excluir_gasto'),
]