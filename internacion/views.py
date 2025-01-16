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
    es_medico = hasattr(request.user, 'medico')
    es_enfermero = hasattr(request.user, 'enfermero')
    return render(request, 'listar_internaciones.html', {'internaciones': internaciones,'es_medico': es_medico,
        'es_enfermero': es_enfermero,})


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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .forms import SeguimientoForm, MedicacionForm, SignosVitalesForm
from .models import Paciente, Enfermero, Seguimiento, Medicacion, SignosVitales

@login_required
def seguimiento(request, paciente_id):
    paciente = get_object_or_404(Paciente, idpaciente=paciente_id)
    enfermero = get_object_or_404(Enfermero, persona=request.user)  # Usar el campo correcto para obtener el enfermero logeado

    MedicacionFormSet = inlineformset_factory(Seguimiento, Medicacion, form=MedicacionForm, extra=1, can_delete=False)
    SignosVitalesFormSet = inlineformset_factory(Seguimiento, SignosVitales, form=SignosVitalesForm, extra=1,can_delete=False)

    if request.method == 'POST':
        form = SeguimientoForm(request.POST)
        medicacion_formset = MedicacionFormSet(request.POST, instance=Seguimiento())
        signos_vitales_formset = SignosVitalesFormSet(request.POST, instance=Seguimiento())

        if form.is_valid() and medicacion_formset.is_valid() and signos_vitales_formset.is_valid():
            seguimiento = form.save(commit=False)
            seguimiento.idpaciente = paciente
            seguimiento.idenfermero = enfermero
            seguimiento.save()
            medicacion_formset.instance = seguimiento
            signos_vitales_formset.instance = seguimiento
            medicacion_formset.save()
            signos_vitales_formset.save()
            return redirect('listar_internaciones')  # Asegúrate de tener esta vista y URL configurada
    else:
        form = SeguimientoForm()
        medicacion_formset = MedicacionFormSet(instance=Seguimiento())
        signos_vitales_formset = SignosVitalesFormSet(instance=Seguimiento())

    return render(request, 'seguimiento.html', {
        'form': form,
        'medicacion_formset': medicacion_formset,
        'signos_vitales_formset': signos_vitales_formset,
        'paciente': paciente,
        'enfermero': enfermero,
    })
    

def listar_seguimientos(request, paciente_id):
    paciente = get_object_or_404(Paciente, idpaciente=paciente_id)
    seguimientos = Seguimiento.objects.filter(idpaciente=paciente)
    return render(request, 'listar_seguimientos.html', {
        'paciente': paciente,
        'seguimientos': seguimientos,
    })
    
def seguimiento_detalles(request, seguimiento_id):
    seguimiento = get_object_or_404(Seguimiento, idseguimento=seguimiento_id)
    medicaciones = Medicacion.objects.filter(seguimiento=seguimiento)
    signos_vitales = SignosVitales.objects.filter(seguimiento=seguimiento)
    return render(request, 'seguimiento_detalles.html', {
        'seguimiento': seguimiento,
        'medicaciones': medicaciones,
        'signos_vitales': signos_vitales,
    })