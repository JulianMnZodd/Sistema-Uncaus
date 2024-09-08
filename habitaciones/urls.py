from django.urls import path
from . import views

urlpatterns = [
    path('habitacion/<int:habitacion_id>/', views.habitacion_detalle, name='habitacion_detalle'),
    path('habitaciones/', views.lista_habitaciones, name='lista_habitaciones'),
]