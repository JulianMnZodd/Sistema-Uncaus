from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Medico

from .forms import MedicoForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

#@login_required
def create_medico(request):
    if request.method == "GET":
        return render(request, 'create_medico.html', {"form": MedicoForm})
    else:
        try:
            form = MedicoForm(request.POST)
            new_medico = form.save(commit=False)
            #new_medico.user = request.user
            new_medico.save()
            return redirect('home')
        except ValueError:
            return render(request, 'create_medico.html', {"form": MedicoForm, "error": "Error creating medico."})



