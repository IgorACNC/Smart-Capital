from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import Gasto, MetaGasto

@login_required
def visualizar_gastos(request):
    # Pegando os gastos do usuário
    gastos = Gasto.objects.filter(usuario=request.user)
    
    # Calculando o total de gastos
    total_gastos = sum(gasto.valor for gasto in gastos)
    
    # Buscando a meta do usuário, se existir
    meta = MetaGasto.objects.filter(usuario=request.user).first()

    # Verificando se o total de gastos ultrapassou a meta
    meta_ultrapassada = False
    if meta and total_gastos >= meta.valor_meta:
        meta_ultrapassada = True

    if request.method == 'POST':
        gasto_id = request.POST.get('gasto_id')
        try:
            gasto = Gasto.objects.get(id=gasto_id, usuario=request.user)
            gasto.delete()
            messages.success(request, 'Gasto excluído com sucesso!')
            return redirect('visualizar_gastos')  # Recarrega a página após exclusão para atualizar a soma
        except Gasto.DoesNotExist:
            messages.error(request, 'Gasto não encontrado!')

    # Renderizando a página com as informações necessárias
    return render(request, 'visualizar_gastos.html', {
        'gastos': gastos,
        'total_gastos': total_gastos,
        'meta': meta,
        'meta_ultrapassada': meta_ultrapassada
    })

@login_required
def add_gastos(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        data = request.POST.get('data')

        if descricao and valor and data:
            try:
                valor = float(valor)
                gasto = Gasto(usuario=request.user, descricao=descricao, valor=valor, data=data)
                gasto.save()

                messages.success(request, 'Gasto adicionado com sucesso!')
                return redirect('visualizar_gastos')
            except ValueError:
                messages.error(request, 'Valor inválido.')
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'add_gastos.html')

def gastos(req):
    return render(req, 'gastos.html')

def excluir_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    if request.method == 'POST':
        gasto.delete()
        messages.success(request, 'Gasto excluído com sucesso!')
        return redirect('visualizar_gastos')  # Volta para a página de visualização após excluir
    return render(request, 'confirmar_exclusao.html', {'gasto': gasto})


@login_required
def add_meta(request):
    if request.method == 'POST':
        valor_meta = request.POST.get('valor_meta')

        if valor_meta:
            try:
                valor_meta = float(valor_meta)
                MetaGasto.objects.create(usuario=request.user, valor_meta=valor_meta)
                messages.success(request, 'Meta de gastos adicionada com sucesso!')
                return redirect('visualizar_gastos')
            except ValueError:
                messages.error(request, 'Valor inválido.')
        else:
            messages.error(request, 'O campo de valor é obrigatório.')

    return render(request, 'add_meta.html')

@login_required
def excluir_meta(request):
    meta = MetaGasto.objects.filter(usuario=request.user).last()
    if meta:
        meta.delete()
        messages.success(request, 'Meta excluída com sucesso!')
    else:
        messages.error(request, 'Nenhuma meta encontrada para excluir.')

    return redirect('visualizar_gastos')