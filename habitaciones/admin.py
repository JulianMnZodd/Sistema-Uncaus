from django.contrib import admin
from .models import Habitacion,Cama,Sector,Reserva
# Register your models here.
admin.site.register(Habitacion)
admin.site.register(Cama)
admin.site.register(Sector)
admin.site.register(Reserva)