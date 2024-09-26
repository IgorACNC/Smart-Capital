from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import UserProfile  # Verifique se está correto



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo, {username}!')
                return render(request,'app.html')  # Redireciona para a página inicial
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')

    return render(request, 'login.html')


def logout1(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('/usuarios/home')


def home(request):
    return render(request, 'home.html')


from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import UserProfile

def cadastro(request):
    estados_brasil = UserProfile.ESTADOS_BRASIL

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        numero_telefone = request.POST.get('numero_telefone')
        estado = request.POST.get('estado')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html', {'estados': estados_brasil})

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'cadastro.html', {'estados': estados_brasil})

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já está em uso.')
            return render(request, 'cadastro.html', {'estados': estados_brasil})

        user = User.objects.create_user(username=username, email=email, password=password1)
        UserProfile.objects.create(user=user, numero_telefone=numero_telefone, estado=estado)

        login(request) 
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('/usuarios/login')

    return render(request, 'cadastro.html', {'estados': estados_brasil})