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
            fecha_admicion=timezone.now(),
            cama=cama,
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

def listar_internaciones(request):
    internaciones = Internacion.objects.all()
    return render(request, 'listar_internaciones.html', {'internaciones': internaciones})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AtencionForm
from .models import Paciente, Medico, Atencion

@login_required
def crear_atencion(request, paciente_id):
    paciente = get_object_or_404(Paciente, idpaciente=paciente_id)
    medico = get_object_or_404(Medico, persona=request.user)  # Usar el campo correcto para obtener el médico logeado

    if request.method == 'POST':
        form = AtencionForm(request.POST)
        if form.is_valid():
            atencion = form.save(commit=False)
            atencion.idpaciente = paciente
            atencion.idmedico = medico
            atencion.save()
            return redirect('listar_internaciones')  # Asegúrate de tener esta vista y URL configurada
    else:
        form = AtencionForm()
    return render(request, 'crear_atencion.html', {'form': form, 'paciente': paciente, 'medico': medico})