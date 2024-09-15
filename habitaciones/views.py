from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Habitacion,Cama

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
    camas_context = [
        {"paciente": cama.paciente if cama.estado == 'O' else 'Libre', 
         "color": "#FF0000" if cama.estado == 'O' else "#00FF00"}
        for cama in camas
    ]

    return render(request, 'habitacion_detalle.html', {
        "habitacion": habitacion,
        "camas": camas_context
    })


