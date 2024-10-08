from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('controle_gastos/', include('controle_gastos.urls')),
    path('educacao-financeira/', include('educacao_financeira.urls')),
    path('planejamento/', include('planejamento_aposentadoria.urls'))
]