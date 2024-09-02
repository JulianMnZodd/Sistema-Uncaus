from django.db import models

# Create your models here.

class Paciente(models.Model):
    idpaciente = models.AutoField(db_column='idPaciente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    obra_social = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    fecha_alta = models.DateTimeField()
    descripcion = models.CharField(max_length=256)

    class Meta:
        
        db_table = 'paciente'