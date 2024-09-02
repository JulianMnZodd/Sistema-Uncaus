from django.forms import ModelForm
from .models import Medico

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__' 