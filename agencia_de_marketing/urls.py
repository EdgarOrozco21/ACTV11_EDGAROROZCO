from django.contrib import admin
from django.urls import path, include
# Importaciones necesarias para servir archivos estáticos/media en desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye las rutas de tu aplicación 'app_empleado'
    path('', include('app_empleado.urls')),
]

# BLOQUE CLAVE PARA CARGAR CSS Y MEDIA EN DESARROLLO
# Este bloque es el que te faltaba y le dice a Django dónde buscar los archivos estáticos.
if settings.DEBUG:
    # Configuración para archivos estáticos (CSS, JS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Configuración para archivos media (imágenes de empleados)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
