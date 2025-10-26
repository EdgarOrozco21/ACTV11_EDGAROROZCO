from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Empleado, Proyecto
from .forms import EmpleadoForm, ProyectoForm

# *********************************
# VISTAS DE EMPLEADO
# *********************************

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'app_empleado/lista_empleados.html'
    context_object_name = 'empleados'  # <--- mejor nombre para la plantilla

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'app_empleado/empleado_detail.html'
    context_object_name = 'empleado'  # <--- coincide con tu plantilla

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm  # <--- usa tu form para aplicar Tailwind
    template_name = 'app_empleado/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'app_empleado/empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'app_empleado/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')

# *********************************
# VISTAS DE PROYECTO
# *********************************

class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'app_empleado/proyecto_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleado_id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        # Asigna el empleado al proyecto antes de guardar
        empleado = get_object_or_404(Empleado, pk=self.kwargs['pk'])
        form.instance.empleado = empleado
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('empleado_detail', kwargs={'pk': self.kwargs['pk']})

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'app_empleado/proyecto_form.html'

    def get_success_url(self):
        return reverse_lazy('empleado_detail', kwargs={'pk': self.object.empleado.pk})

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'app_empleado/proyecto_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('empleado_detail', kwargs={'pk': self.object.empleado.pk})
