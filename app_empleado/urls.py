
from django.urls import path
from .views import (
    EmpleadoListView, EmpleadoDetailView, EmpleadoCreateView, 
    EmpleadoUpdateView, EmpleadoDeleteView, ProyectoCreateView,
    ProyectoDeleteView
)

urlpatterns = [
    # CRUD for Empleado (Main Table)
    path('', EmpleadoListView.as_view(), name='empleado_list'), # Home/List
    path('empleado/crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleado/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('empleado/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleado/<int:pk>/borrar/', EmpleadoDeleteView.as_view(), name='empleado_delete'),

    # CRUD for Proyecto (Secondary Table)
    path('proyecto/crear/', ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyecto/<int:pk>/borrar/', ProyectoDeleteView.as_view(), name='proyecto_delete'),
]
