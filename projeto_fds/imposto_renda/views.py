from django.shortcuts import render
from .models import ImpostoRenda

def calcular_imposto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        renda_anual = float(request.POST.get('renda_anual'))

        imposto = 0
        explicacao = []

        # Faixa de isenção
        if renda_anual <= 22847.76:
            explicacao.append("Renda isenta de imposto.")
        else:
            # Faixa de 7,5%
            if renda_anual <= 33919.80:
                imposto_faixa = (renda_anual - 22847.76) * 0.075
                imposto += imposto_faixa
                explicacao.append(f"Faixa de 7,5%: R$ {imposto_faixa:.2f}")
            else:
                imposto_faixa = (33919.80 - 22847.76) * 0.075
                imposto += imposto_faixa
                explicacao.append(f"Faixa de 7,5%: R$ {imposto_faixa:.2f}")

            # Faixa de 15%
            if renda_anual > 33919.80:
                if renda_anual <= 45012.60:
                    imposto_faixa = (renda_anual - 33919.80) * 0.15
                    imposto += imposto_faixa
                    explicacao.append(f"Faixa de 15%: R$ {imposto_faixa:.2f}")
                else:
                    imposto_faixa = (45012.60 - 33919.80) * 0.15
                    imposto += imposto_faixa
                    explicacao.append(f"Faixa de 15%: R$ {imposto_faixa:.2f}")

            # Faixa de 22,5%
            if renda_anual > 45012.60:
                if renda_anual <= 55976.16:
                    imposto_faixa = (renda_anual - 45012.60) * 0.225
                    imposto += imposto_faixa
                    explicacao.append(f"Faixa de 22,5%: R$ {imposto_faixa:.2f}")
                else:
                    imposto_faixa = (55976.16 - 45012.60) * 0.225
                    imposto += imposto_faixa
                    explicacao.append(f"Faixa de 22,5%: R$ {imposto_faixa:.2f}")

            # Faixa de 27,5%
            if renda_anual > 55976.16:
                imposto_faixa = (renda_anual - 55976.16) * 0.275
                imposto += imposto_faixa
                explicacao.append(f"Faixa de 27,5%: R$ {imposto_faixa:.2f}")
                
        imposto_registrado = ImpostoRenda.objects.create(nome=nome, renda_anual=renda_anual, imposto_calculado=imposto)

        return render(request, 'resultados.html', {'nome': nome, 'imposto': imposto, 'explicacao': explicacao})

    return render(request, 'calculo.html')

def historico_calculos(request):
    calculos = ImpostoRenda.objects.all().order_by('-data_calculo')
    return render(request, 'historico.html', {'calculos': calculos})