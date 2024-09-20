from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import Gasto


@login_required
def visualizar_gastos(request):
    gastos = Gasto.objects.filter(usuario=request.user)
    if request.method == 'POST':
        gasto_id = request.POST.get('gasto_id')
        try:
            gasto = Gasto.objects.get(id=gasto_id, usuario=request.user)
            gasto.delete()
            messages.success(request, 'Gasto excluído com sucesso!')
        except Gasto.DoesNotExist:
            messages.error(request, 'Gasto não encontrado!')

    return render(request, 'visualizar_gastos.html', {'gastos': gastos})




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

from django.shortcuts import render, redirect, get_object_or_404

def excluir_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    if request.method == 'POST':
        gasto.delete()
        messages.success(request, 'Gasto excluído com sucesso!')
        return redirect('visualizar_gastos')  # Volta para a página de visualização após excluir
    return render(request, 'confirmar_exclusao.html', {'gasto': gasto})
