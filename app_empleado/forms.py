from django import forms
from .models import Empleado, Proyecto

# Define la clase CSS de Tailwind para los campos de texto estándar
TAILWIND_CLASS = 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-indigo-500 focus:border-indigo-500'

# **************************************
# NUEVO: Formulario para Empleado
# (Para usar en EmpleadoCreateView y EmpleadoUpdateView)
# **************************************
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica la clase Tailwind a todos los campos
        for field in self.fields:
            # No aplica clases a campos de tipo FileField, ya que se renderizan diferente
            if self.fields[field].widget.__class__.__name__ != 'ClearableFileInput':
                self.fields[field].widget.attrs.update(
                    {'class': TAILWIND_CLASS}
                )

# Formulario usado por ProyectoCreateView y ProyectoUpdateView
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        # Excluir 'empleado' ya que se asigna automáticamente en la vista (views.py)
        # o puedes incluirlo si quieres seleccionarlo desde el formulario.
        # Aquí lo dejamos para que puedas definirlo más fácilmente.
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_entrega', 'id_campaña', 'empleado']
        
        # Personalizar los widgets para que se vean mejor (ej. añadir clases)
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': TAILWIND_CLASS}),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date', 'class': TAILWIND_CLASS}),
            # Aplicar la clase Tailwind al resto de campos de texto
            'nombre': forms.TextInput(attrs={'class': TAILWIND_CLASS}),
            'descripcion': forms.Textarea(attrs={'class': TAILWIND_CLASS}),
            'id_campaña': forms.TextInput(attrs={'class': TAILWIND_CLASS}),
        }
