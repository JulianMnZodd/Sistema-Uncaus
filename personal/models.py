from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

# class CustomUser(AbstractUser):
#     groups = models.ManyToManyField(
#         Group,
#         related_name='customuser_set',  # Cambia el related_name para evitar conflicto
#         blank=True,
#         help_text=('The groups this user belongs to. A user will get all permissions '
#                    'granted to each of their groups.'),
#         verbose_name=('groups'),
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='customuser_set',  # Cambia el related_name para evitar conflicto
#         blank=True,
#         help_text=('Specific permissions for this user.'),
#         verbose_name=('user permissions'),
#     )

class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    fecha_nacimiento = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'persona'


class Recepcionista(models.Model):
    persona_idpersona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='Persona_idPersona', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'recepcionista'

class Enfermero(models.Model):
    persona_idpersona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='Persona_idPersona', primary_key=True)  # Field name made lowercase.
    matricula = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'enfermero'
        

class Medico(models.Model):
    persona_idpersona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='Persona_idPersona', primary_key=True)  # Field name made lowercase.
    especializacion = models.CharField(max_length=45)
    matricula = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'medico'
        


