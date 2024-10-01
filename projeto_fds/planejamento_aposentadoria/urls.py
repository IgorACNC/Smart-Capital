from django.urls import path
from . import views

urlpatterns = [
    path('', views.planejamento_view, name='planejamento'),
    path('resultado/<int:pk>/', views.resultado_planejamento_view, name='resultado_planejamento'),
    path('listar/', views.listar_planejamentos_view, name='listar_planejamentos'),
]
