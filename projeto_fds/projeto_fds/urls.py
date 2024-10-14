from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('controle_gastos/', include('controle_gastos.urls')),
    path('educacao-financeira/', include('educacao_financeira.urls')),
    path('planejamento/', include('planejamento_aposentadoria.urls')),
<<<<<<< Updated upstream
    path('imposto_renda/', include('imposto_renda.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('simulacao/', include('simulacao_investimentos.urls') )
]
>>>>>>> Stashed changes
