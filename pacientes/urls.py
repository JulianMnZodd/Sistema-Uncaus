from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('asignar_paciente_cama/', views.asignar_paciente_cama, name='asignar_paciente_cama'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('internaciones_historicas/<int:paciente_id>/', views.listar_internaciones_historicas, name='listar_internaciones_historicas'),
]