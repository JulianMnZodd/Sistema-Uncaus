from django.urls import path
from . import views

urlpatterns = [
    path('asignar_cama/<int:idcama>/', views.asignar_cama, name='asignar_cama'),
    path('internaciones/', views.listar_internaciones, name='listar_internaciones'),
    path('crear_atencion/<int:paciente_id>/', views.crear_atencion, name='crear_atencion'),
    path('seleccionar_cama/<int:paciente_id>/', views.seleccionar_cama, name='seleccionar_cama'),
]