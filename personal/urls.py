from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('crear-medico',views.crear_medico, name='crear_medico'),
    path('crear-recepcionista/', views.crear_recepcionista, name='crear_recepcionista'),
    path('crear-enfermero/', views.crear_enfermero, name='crear_enfermero'),
    path('listar-medicos/', views.listar_medicos, name='listar_medicos'),
    path('listar-recepcionistas/', views.listar_recepcionistas, name='listar_recepcionistas'),
    path('listar-enfermeros/', views.listar_enfermeros, name='listar_enfermeros'),
    path('editar-medico/<int:medico_id>/', views.editar_medico, name='editar_medico'),
    path('editar-recepcionista/<int:recepcionista_id>/', views.editar_recepcionista, name='editar_recepcionista'),
    path('editar-enfermero/<int:enfermero_id>/', views.editar_enfermero, name='editar_enfermero'),
]