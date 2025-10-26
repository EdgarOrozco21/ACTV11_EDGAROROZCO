from django.contrib import admin
from .models import Empleado, Proyecto

# Register both models so they appear in the Django admin panel
admin.site.register(Empleado)
admin.site.register(Proyecto)