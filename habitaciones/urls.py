from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.lista_habitaciones, name='lista_habitaciones'),
    path('liberar_cama/<int:idcama>/', views.liberar_cama, name='liberar_cama'),
    path('reservar_cama/<int:idcama>/', views.reservar_cama, name='reservar_cama'),
    path('ver_reserva/<int:idcama>/', views.ver_reserva, name='ver_reserva'),
]