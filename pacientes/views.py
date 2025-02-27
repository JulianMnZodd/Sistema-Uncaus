from django.shortcuts import render,redirect,get_object_or_404
from pacientes.models import Paciente
from .forms import PacienteForm
from internacion.models import Internacion
from django.contrib import messages

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Paciente creado exitosamente!')
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'crear_paciente.html', {'form': form})

def asignar_paciente_cama(request):
    pacientes = Paciente.objects.all()  # Obtén todos los pacientes del sistema
    return render(request, 'asignar_paciente_cama.html', {'pacientes': pacientes})

def listar_pacientes(request):
    pacientes = Paciente.objects.all()  # Obtén todos los pacientes del sistema
    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})

def listar_internaciones_historicas(request, paciente_id):
    paciente = get_object_or_404(Paciente, idpaciente=paciente_id)
    internaciones = Internacion.objects.filter(idpaciente=paciente)
    return render(request, 'listar_internaciones_historicas.html', {
        'paciente': paciente,
        'internaciones': internaciones,
    })

