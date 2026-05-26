from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from django.conf import settings               # <-- Añade esta importación
from django.conf.urls.static import static     # <-- Añade esta importación

urlpatterns = [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
] 

# Esto le dice a Django que sirva los archivos de la carpeta media en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)