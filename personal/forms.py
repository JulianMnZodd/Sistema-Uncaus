from django import forms
from .models import Persona, Medico,Recepcionista,Enfermero
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-control'}))


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Persona

class CustomUserCreationForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = Persona
        fields = ['first_name', 'last_name', 'email', 'dni', 'telefono', 'domicilio', 'genero', 'fecha_nacimiento']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'dni': 'DNI',
            'telefono': 'Teléfono',
            'domicilio': 'Domicilio',
            'genero': 'Género',
            'fecha_nacimiento': 'Fecha de nacimiento',
            
            }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'dni': forms.NumberInput(attrs={'min': 0}),
            'telefono': forms.NumberInput(attrs={'min': 0}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Persona
        fields = ['first_name', 'last_name', 'email', 'telefono', 'domicilio',]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password': 'Contraseña',
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['especializacion', 'matricula']
        
class EnfermeroForm(forms.ModelForm):
    class Meta:
        model = Enfermero
        fields = ['matricula']
        
class RecepcionistaForm(forms.ModelForm):
    class Meta:
        model = Recepcionista
        fields = ['turno']
