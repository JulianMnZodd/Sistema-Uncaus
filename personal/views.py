from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from personal.forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home') 

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

def home(request):
    return render(request, 'home.html')
      
from .forms import CustomUserCreationForm, MedicoForm, RecepcionistaForm, EnfermeroForm

@login_required
def crear_medico(request):
    if request.method == 'POST':
        # Crear ambos formularios
        persona_form = CustomUserCreationForm(request.POST)
        medico_form = MedicoForm(request.POST)

        if persona_form.is_valid() and medico_form.is_valid():
            # Guardar la persona primero
            persona = persona_form.save()

            # Crear el médico y asociarlo con la persona
            medico = medico_form.save(commit=False)
            medico.persona = persona  # Relacionar el médico con la persona
            medico.save()

            messages.success(request, '¡Médico creado exitosamente!')
            return redirect('crear_medico')
    else:
        persona_form = CustomUserCreationForm()
        medico_form = MedicoForm()

    return render(request, 'crear_medico.html', {
        'persona_form': persona_form,
        'medico_form': medico_form,
    })


@login_required
def crear_enfermero(request):
    if request.method == 'POST':
        # Crear ambos formularios
        persona_form = CustomUserCreationForm(request.POST)
        enfermero_form = EnfermeroForm(request.POST)

        if persona_form.is_valid() and enfermero_form.is_valid():
            # Guardar la persona primero
            persona = persona_form.save()

            # Crear el enfermero y asociarlo con la persona
            enfermero = enfermero_form.save(commit=False)
            enfermero.persona = persona  # Relacionar el enfermero con la persona
            enfermero.save()

            messages.success(request, '¡Enfermero creado exitosamente!')
            return redirect('crear_enfermero')
    else:
        persona_form = CustomUserCreationForm()
        enfermero_form = EnfermeroForm()

    return render(request, 'crear_enfermero.html', {
        'persona_form': persona_form,
        'enfermero_form': enfermero_form,
    })


@login_required
def crear_recepcionista(request):
    if request.method == 'POST':
        # Crear ambos formularios
        persona_form = CustomUserCreationForm(request.POST)
        recepcionista_form = RecepcionistaForm(request.POST)

        if persona_form.is_valid() and recepcionista_form.is_valid():
            # Guardar la persona primero
            persona = persona_form.save()

            # Crear el recepcionista y asociarlo con la persona
            recepcionista = recepcionista_form.save(commit=False)
            recepcionista.persona = persona  # Relacionar el recepcionista con la persona
            recepcionista.save()

            messages.success(request, '¡Recepcionista creado exitosamente!')
            return redirect('crear_recepcionista')
    else:
        persona_form = CustomUserCreationForm()
        recepcionista_form = RecepcionistaForm()

    return render(request, 'crear_recepcionista.html', {
        'persona_form': persona_form,
        'recepcionista_form': recepcionista_form,
    })