from django.shortcuts import render, redirect, get_object_or_404
from .models import PlanejamentoAposentadoria

def planejamento_view(request):
    if request.method == 'POST':
        idade_atual = int(request.POST.get('idade_atual'))
        idade_aposentadoria = int(request.POST.get('idade_aposentadoria'))
        meta_renda = float(request.POST.get('meta_renda'))

        planejamento = PlanejamentoAposentadoria(
            idade_atual=idade_atual,
            idade_aposentadoria=idade_aposentadoria,
            meta_renda=meta_renda
        )
        planejamento.save()  
        return redirect('resultado_planejamento', pk=planejamento.pk) 

    return render(request, 'planejamento.html')

def resultado_planejamento_view(request, pk):
    planejamento = get_object_or_404(PlanejamentoAposentadoria, pk=pk)
    anos_para_aposentadoria = planejamento.idade_aposentadoria - planejamento.idade_atual
    meses_para_aposentadoria = anos_para_aposentadoria * 12
    valor_mensal = planejamento.meta_renda / meses_para_aposentadoria if meses_para_aposentadoria > 0 else 0

    return render(request, 'resultado.html', {'planejamento': planejamento, 'valor_mensal': valor_mensal})

def listar_planejamentos_view(request):
    planejamentos = PlanejamentoAposentadoria.objects.all()
    return render(request, 'listar_planejamentos.html', {'planejamentos': planejamentos})
