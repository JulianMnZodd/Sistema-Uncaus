from django.urls import path
from . import views

urlpatterns = [
    path('asignar_cama/<int:idcama>/', views.asignar_cama, name='asignar_cama'),
    path('internaciones/', views.listar_internaciones, name='listar_internaciones'),
    path('crear_atencion/<int:internacion_id>/', views.crear_atencion, name='crear_atencion'),
    path('listar_atenciones/<int:paciente_id>/', views.listar_atenciones, name='listar_atenciones'),
    path('seleccionar_cama/<int:paciente_id>/', views.seleccionar_cama, name='seleccionar_cama'),
    path('seguimiento/<int:internacion_id>/', views.seguimiento, name='seguimiento'),
    path('listar_seguimientos/<int:internacion_id>/', views.listar_seguimientos, name='listar_seguimientos'),
    path('seguimiento_detalles/<int:seguimiento_id>/', views.seguimiento_detalles, name='seguimiento_detalles'),
]