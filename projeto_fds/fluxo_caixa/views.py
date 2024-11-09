from django.shortcuts import render, redirect
from .models import FluxoCaixa
from django.contrib.auth.decorators import login_required

@login_required
def calcular_fluxo_caixa(request):
    if request.method == "POST":
        periodo = request.POST.get("periodo")
        ebit = float(request.POST.get("ebit"))
        ir = float(request.POST.get("ir"))
        depreciacao = float(request.POST.get("depreciacao"))
        receita_total = float(request.POST.get("receita_total"))
        despesa_total = float(request.POST.get("despesa_total"))

        # Calcular o fluxo de caixa operacional (FCO)
        fco = ebit - ir + depreciacao

        # Armazenar no banco de dados
        FluxoCaixa.objects.create(
            usuario=request.user,
            periodo=periodo,
            ebit=ebit,
            ir=ir,
            depreciacao=depreciacao,
            receita_total=receita_total,
            despesa_total=despesa_total,
            fluxo_caixa_operacional=fco
        )
        return redirect('historico_fluxo_caixa')

    return render(request, 'calculo_fluxo_caixa.html')

@login_required
def historico_fluxo_caixa(request):
    historico = FluxoCaixa.objects.filter(usuario=request.user).order_by('-data_calculo')
    return render(request, 'historico_fluxo_caixa.html', {'historico': historico})
