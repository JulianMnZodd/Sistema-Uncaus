from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Habitacion,Cama
from .models import Cama, Medico, Reserva

def lista_habitaciones(request):
    habitaciones = Habitacion.objects.prefetch_related('camas').all()  # Traemos todas las habitaciones con sus camas
    
    context = {
        'habitaciones': habitaciones,
    }
    
    return render(request, 'lista_habitaciones.html', context)

def habitacion_detalle(request, habitacion_id):
    # Obtener la habitación por su ID y sus camas
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    camas = habitacion.camas.all()  # Obtener las camas de la habitación

    # Crear el contexto para pasar a la plantilla
    camas_context = []

    for cama in camas:
        if cama.estado == 'O':
            color = "#FF0000"  # Rojo para ocupada
            paciente = cama.paciente
        elif cama.estado == 'R':
            color = "#FFFF00"  # Amarillo para reservada
            paciente = 'Reservada'
        else:
            color = "#00FF00"  # Verde para libre
            paciente = 'Libre'
        
        camas_context.append({
            "paciente": paciente,
            "color": color
        })

    return render(request, 'habitacion_detalle.html', {
        "habitacion": habitacion,
        "camas": camas_context
    })


def liberar_cama(request, idcama):
    cama = get_object_or_404(Cama, idcama=idcama)
    if request.method == 'POST':
        cama.liberar()
        return redirect('lista_habitaciones')  # Redirige a la lista de internaciones o a otra vista relevante
    return redirect('lista_habitaciones')

from django.utils import timezone
from datetime import timedelta
def reservar_cama(request, idcama):
    cama = get_object_or_404(Cama, idcama=idcama)
    medicos = Medico.objects.all()
    
    if request.method == 'POST':
        medico_id = request.POST.get('medico_id')
        medico = get_object_or_404(Medico, persona_id=medico_id)
        dias_expiracion = int(request.POST.get('dias_expiracion', 7))  # Por defecto 7 días
        fecha_expiracion = timezone.now() + timedelta(days=dias_expiracion)
        
        # Eliminar cualquier reserva existente para esta cama
        Reserva.objects.filter(cama=cama).delete()
        
        # Crear una nueva reserva
        reserva = Reserva.objects.create(cama=cama, medico=medico, fecha_expiracion=fecha_expiracion)
        cama.estado = 'R'  # Suponiendo que 'R' es el estado para 'Reservada'
        cama.save()
        return redirect('lista_habitaciones')  # Redirigir a la lista de habitaciones después de reservar
    
    return render(request, 'reservar_cama.html', {'cama': cama, 'medicos': medicos})

def ver_reserva(request, idcama):
    cama = get_object_or_404(Cama, idcama=idcama)
    reservas = Reserva.objects.filter(cama=cama).order_by('-fecha_reserva')
    reserva = reservas.first()  # Obtener la reserva más reciente
    return render(request, 'ver_reserva.html', {'cama': cama, 'reserva': reserva})

from celery import shared_task
from django.utils import timezone

@shared_task
def liberar_camas_expiradas():
    now = timezone.now()
    reservas_expiradas = Reserva.objects.filter(fecha_expiracion__lt=now)
    for reserva in reservas_expiradas:
        cama = reserva.cama
        cama.estado = 'L'  # Suponiendo que 'L' es el estado para 'Libre'
        cama.save()
        reserva.delete()