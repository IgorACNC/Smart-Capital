from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Aula, Resumo
from django.contrib import messages

def listar_aulas(request):
    aulas = Aula.objects.all().order_by('numero')  # Lista as aulas em ordem
    return render(request, 'listar_aulas.html', {'aulas': aulas})

def visualizar_resumo(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    resumo = get_object_or_404(Resumo, aula=aula)
    return render(request, 'visualizar_resumo.html', {'aula': aula, 'resumo': resumo})

def detalhes_aula(request, aula_id): 
    resumos = Resumo.objects.filter(aula=aula)

    # Truncar o texto ao exibir os resumos
    for resumo in resumos:
        resumo.conteudo_truncado = resumo.conteudo[:100] + '...' if len(resumo.conteudo) > 100 else resumo.conteudo

    if request.method == "POST":
        texto_resumo = request.POST.get('texto')
        usuario = request.user  # Obtendo o usuário logado
        
        if len(texto_resumo) > 250:
            return JsonResponse({'success': False, 'error': 'Seu resumo é muito longo. O máximo permitido é 250 caracteres.'})
        else:
            novo_resumo = Resumo.objects.create(aula=aula, conteudo=texto_resumo, usuario=usuario)
            return JsonResponse({
                'success': True,
                'conteudo': novo_resumo.conteudo,
                'username': novo_resumo.usuario.username
            })

    return render(request, 'detalhes_aula.html', {'aula': aula, 'resumos': resumos})
