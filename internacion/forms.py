from django import forms
from .models import Diagnostico, Seguimiento, Medicacion, SignosVitales
from .models import Paciente, Cama


class AsignarCamaForm(forms.Form):
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(), label="Seleccionar Paciente"
    )
    # fecha_alta = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Alta")
    nota_ingreso = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}), label="Nota de Ingreso"
    )

    def clean_paciente(self):
        paciente = self.cleaned_data["paciente"]
        camas_ocupadas = Cama.objects.filter(paciente=paciente, estado="O")
        if camas_ocupadas.exists():
            raise forms.ValidationError(
                "Este paciente ya está asignado a una cama ocupada."
            )
        return paciente


class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['fecha', 'detalles', 'gravedad', 'tratamiento','idmedico_derivado']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'detalles': forms.Textarea(attrs={'rows': 4}),   
            'gravedad': forms.TextInput(attrs={'placeholder': 'Ej: Leve'}),
            'tratamiento': forms.Textarea(attrs={'rows': 4}),
        }
        


class MedicacionForm(forms.ModelForm):
    class Meta:
        model = Medicacion
        fields = ["tipo", "nombre", "hora_medicacion"]
        widgets = {
            "hora_medicacion": forms.TimeInput(attrs={"type": "time"}),
        }


class SignosVitalesForm(forms.ModelForm):
    class Meta:
        model = SignosVitales
        fields = ["temperatura_corporal", "pulso", "frecuencia_respiratoria"]


class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = ["observacion"]
        widgets = {
            "observacion": forms.Textarea(attrs={"rows": 4}),
        }
