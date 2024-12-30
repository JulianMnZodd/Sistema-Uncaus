from django.urls import path
from . import views

urlpatterns = [
    path('asignar_cama/<int:idcama>/', views.asignar_cama, name='asignar_cama'),
    path('seleccionar_cama/<int:paciente_id>/', views.seleccionar_cama, name='seleccionar_cama'),
]