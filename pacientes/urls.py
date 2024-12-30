from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
]