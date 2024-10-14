from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SimulacaoInvestimento
from decimal import Decimal

def adicionar_simulacao(request):
    template = 'simulacao_investimentos/adicionar_simulacao.html'
    context = {}

    if request.method == 'POST':
        dados = {
            'valor_investimento': request.POST.get('valor_investimento'),
            'periodo_investimento': request.POST.get('periodo_investimento'),
            'perfil_risco': request.POST.get('perfil_risco')
        }
        context.update(dados)

        erros = []
        for campo, valor in dados.items():
            if not valor:
                erros.append(f"O campo '{campo}' é obrigatório.")
                
        try:
            dados['valor_investimento'] = float(dados['valor_investimento'])
            if dados['valor_investimento'] <= 0:
                erros.append('O valor do investimento deve ser maior que zero.')
        except (ValueError, TypeError):
            erros.append('Valor do investimento inválido.')

        try:
            dados['periodo_investimento'] = int(dados['periodo_investimento'])
            if dados['periodo_investimento'] <= 0:
                erros.append('O período do investimento deve ser maior que zero.')
        except (ValueError, TypeError):
            erros.append('Período do investimento inválido.')

        perfis_validos = ['baixo', 'medio', 'alto']
        if dados['perfil_risco'] not in perfis_validos:
            erros.append('Perfil de risco inválido.')

        if erros:
            for erro in erros:
                messages.error(request, erro)
        else:
            simulacao = SimulacaoInvestimento(
                usuario=request.user,
                valor_investimento=dados['valor_investimento'],
                periodo_investimento=dados['periodo_investimento'],
                perfil_risco=dados['perfil_risco']
            )
            simulacao.save()
            messages.success(request, 'Simulação adicionada com sucesso!')
            context = {}

    return render(request, template, context)

def listar_investimentos(request):
    investimentos = SimulacaoInvestimento.objects.filter(usuario=request.user)

    taxas_retorno = {
        'baixo': Decimal('0.03'),
        'medio': Decimal('0.06'),
        'alto': Decimal('0.10')
    }
    investimentos_com_retorno = [
        {
            'investimento': investimento,
            'retorno_estimado': investimento.valor_investimento * (
                (1 + taxas_retorno.get(investimento.perfil_risco, Decimal('0'))) ** 
                (investimento.periodo_investimento / Decimal('12'))
            )
        }
        for investimento in investimentos
    ]
    return render(request, 'simulacao_investimentos/listar_investimentos.html', {
        'investimentos_com_retorno': investimentos_com_retorno
    })
