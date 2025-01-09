from django import forms
from .models import Atencion

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = [ 'fecha', 'detalles']