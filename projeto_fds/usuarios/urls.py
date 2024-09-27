from django.urls import path
from .views import cadastro, login, logout1, home

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('logout/', logout1, name='logout'),
    path('', home, name='home'),
]
