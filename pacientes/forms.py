from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dni', 'domicilio','localidad','provincia', 'telefono', 'fecha_nacimiento', 'genero', 'obra_social', 'diabetes', 'hipertension', 'fumador', 'alergias', 'antecedentes', 'cirugias']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Juan'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Ej: Perez'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ej: 011-1234-5678'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ej: 12345678'}),
            'genero': forms.Select(choices=[('M', 'Masculino'), ('F', 'Femenino')]),
            'obra_social': forms.Select(choices=[('PAMI', 'PAMI'), ('OSDE', 'OSDE'), ('IOMA', 'IOMA'),('INSSSEP','INSSSEP'), ('Otra', 'Otra')]),
            'domicilio': forms.TextInput(attrs={'placeholder': 'Ej: Calle Falsa 123'}),
            'localidad': forms.TextInput(attrs={'placeholder': 'Ej: Ciudad Autónoma de Buenos Aires'}),
            'provincia': forms.TextInput(attrs={'placeholder': 'Ej: Buenos Aires'}),
            'diabetes': forms.CheckboxInput(),
            'hipertension': forms.CheckboxInput(),
            'fumador': forms.CheckboxInput(),
            'alergias': forms.Textarea(attrs={'rows': 4}),
            'antecedentes': forms.Textarea(attrs={'rows': 4}),
            'cirugias': forms.Textarea(attrs={'rows': 4}),
            
        }