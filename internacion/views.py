from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from habitaciones.models import Cama
from pacientes.models import Paciente
from .models import Internacion

def asignar_cama(request, idcama):
    # Obtener la cama correspondiente
    cama = get_object_or_404(Cama, idcama=idcama)

    # Verificar si el estado de la cama es "Libre" (L)
    if cama.estado == 'L' and request.method == 'POST':
        # Suponemos que el paciente está siendo seleccionado o es predeterminado para la internación
        paciente_id = request.POST.get('paciente_id')
        paciente = get_object_or_404(Paciente, idpaciente=paciente_id)

        # Crear una nueva instancia de Internacion
        internacion = Internacion.objects.create(
            idpaciente=paciente,
            idhabitacion=cama.habitacion,  # Suponemos que Cama tiene una relación con Habitacion
            fecha_admicion=timezone.now(),
            fecha_alta=None,  # Este campo se llenará cuando el paciente sea dado de alta
            nota_ingreso="Nota de ingreso inicial"
        )

        # Cambiar el estado de la cama a "Ocupada"
        cama.estado = 'O'
        cama.paciente = paciente
        cama.save()

        # Redirigir a la página que desees después de asignar la cama
        return redirect('lista_habitaciones')
    
    return redirect('lista_habitaciones')


from django.shortcuts import render, get_object_or_404
from habitaciones.models import Cama, Habitacion
from pacientes.models import Paciente

def seleccionar_cama(request, paciente_id):
    paciente = get_object_or_404(Paciente, idpaciente=paciente_id)
    habitaciones = Habitacion.objects.prefetch_related('camas').all()  # Obtener todas las habitaciones con sus camas
    return render(request, 'seleccionar_cama.html', {'habitaciones': habitaciones, 'paciente': paciente})

