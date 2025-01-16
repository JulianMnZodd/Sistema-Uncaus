from django import forms
from .models import Atencion, Seguimiento, Medicacion, SignosVitales

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ['fecha', 'detalles']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'detalles': forms.Textarea(attrs={'rows': 4}),
        }

class MedicacionForm(forms.ModelForm):
    class Meta:
        model = Medicacion
        fields = ['tipo', 'nombre', 'hora_medicacion']
        widgets = {
            'hora_medicacion': forms.TimeInput(attrs={'type': 'time'}),
        }

class SignosVitalesForm(forms.ModelForm):
    class Meta:
        model = SignosVitales
        fields = ['temperatura_corporal', 'pulso', 'frecuencia_respiratoria']

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = ['observacion']
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 4}),
        }