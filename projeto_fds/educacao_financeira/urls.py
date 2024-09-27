from django.urls import path
from . import views

urlpatterns = [
    path('aulas/', views.listar_aulas, name='listar_aulas'),
    path('aulas/<int:aula_id>/resumo/', views.visualizar_resumo, name='visualizar_resumo'),
    path('aulas/<int:aula_id>/', views.detalhes_aula, name='detalhes_aula'),
    path('salvar/', views.salvar_resumo, name='salvar_resumo')
]