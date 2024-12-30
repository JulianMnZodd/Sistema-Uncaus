from django.shortcuts import render
from pacientes.models import Paciente

def listar_pacientes(request):
    pacientes = Paciente.objects.all()  # Obtén todos los pacientes del sistema
    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})

