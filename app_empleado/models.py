from django.db import models

# Modelo principal: Empleado
class Empleado(models.Model):
    # Django automáticamente crea 'id' como clave primaria (Id_empleado)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Empleado")
    apellido = models.CharField(max_length=100, verbose_name="Apellido del Empleado")
    puesto = models.CharField(max_length=100, verbose_name="Puesto (Ej: Diseñador, Desarrollador)")
    correo = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Número de Teléfono")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['apellido', 'nombre'] # Order by last name, then first name

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.puesto})"

# Segunda tabla: Proyecto (relacionada con Empleado)
class Proyecto(models.Model):
    # id_proyecto is handled by Django automatically
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(verbose_name="Descripción detallada")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega Estimada")
    
    # id_empleado (Foreign Key) - One-to-Many Relationship
    empleado = models.ForeignKey(
        Empleado, 
        on_delete=models.CASCADE, # If employee is deleted, their projects are also deleted
        related_name='proyectos', # Name to access projects from the employee (e.g., empleado.proyectos.all())
        verbose_name="Empleado Asignado"
    )

    # id_campaña (Implemented as a simple text/reference field as Campaign model is not provided)
    id_campaña = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID de Campaña Asociada")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['fecha_entrega']

    def __str__(self):
        return self.nombre
