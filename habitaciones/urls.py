from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.lista_habitaciones, name='lista_habitaciones'),
    #path('liberar-cama/<int:cama_id>/', views.liberar_cama, name='liberar_cama'),
]