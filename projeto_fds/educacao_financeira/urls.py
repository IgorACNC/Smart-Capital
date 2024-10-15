from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_aulas, name='listar_aulas'),
    path('<int:aula_id>/resumo/', views.visualizar_resumo, name='visualizar_resumo'),
    path('<int:aula_id>/', views.detalhes_aula, name='detalhes_aula'),
]