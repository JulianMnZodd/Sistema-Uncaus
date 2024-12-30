from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('crear-medico',views.crear_medico, name='crear_medico'),
    path('crear-recepcionista/', views.crear_recepcionista, name='crear_recepcionista'),
    path('crear-enfermero/', views.crear_enfermero, name='crear_enfermero'),
]