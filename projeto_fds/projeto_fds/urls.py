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
    path('imposto_renda/', include('imposto_renda.urls')),
    path('simulacao/', include('simulacao_investimentos.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
