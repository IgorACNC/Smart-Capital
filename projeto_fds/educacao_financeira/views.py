from django.shortcuts import render, get_object_or_404
from .models import Aula, Resumo

def listar_aulas(request):
    aulas = Aula.objects.all().order_by('numero')  # Lista as aulas em ordem
    return render(request, 'listar_aulas.html', {'aulas': aulas})

def visualizar_resumo(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    resumo = get_object_or_404(Resumo, aula=aula)
    return render(request, 'visualizar_resumo.html', {'aula': aula, 'resumo': resumo})

def detalhes_aula(request, aula_id): 
    aula = get_object_or_404(Aula, id=aula_id)
    return render(request, 'detalhes_aula.html', {'aula': aula})

def salvar_resumo(request):
    return render(request, 'salvar_resumo.html')