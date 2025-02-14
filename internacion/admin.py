from django.contrib import admin
from .models import Internacion,Diagnostico,Seguimiento,Medicacion,SignosVitales
# Register your models here.
admin.site.register(Internacion)
admin.site.register(Diagnostico)
admin.site.register(Seguimiento)
admin.site.register(Medicacion)
admin.site.register(SignosVitales)