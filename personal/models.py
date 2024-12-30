from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Persona(AbstractUser):
    # Campos adicionales
    username=None
    dni = models.IntegerField(unique=True)
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')], blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    # Si prefieres usar el correo electrónico en lugar del username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dni']


    class Meta:
        db_table = 'persona'

class Medico(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, db_column='Persona_idPersona', primary_key=True)  # Field name made lowercase.
    especializacion = models.CharField(max_length=45)
    matricula = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'medico'

class Recepcionista(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, db_column='Persona_idPersona', primary_key=True)  # Field name made lowercase.
    turno = models.CharField(max_length=10, choices=[('M', 'Mañana'), ('T', 'Tarde')], blank=True)
    class Meta:
        managed = True
        db_table = 'recepcionista'

class Enfermero(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, db_column='Persona_idPersona', primary_key=True)  # Field name made lowercase.
    matricula = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'enfermero'
        


        


