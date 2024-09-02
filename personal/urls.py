from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('new_medico',views.create_medico, name='new_medico')
]