from django.db import models
from personal.models import Enfermero
from pacientes.models import Paciente
from habitaciones.models import Habitacion
# Create your models here.


class Atencion(models.Model):
    idatencion = models.AutoField(db_column='idAtencion', primary_key=True)  # Field name made lowercase.
    idmedico = models.ForeignKey('Medico', models.PROTECT, db_column='idMedico')  # Field name made lowercase.
    idpaciente = models.ForeignKey('Paciente', models.PROTECT, db_column='idPaciente')  # Field name made lowercase.
    fecha = models.DateTimeField()
    detalles = models.CharField(max_length=256)

    class Meta:
        
        db_table = 'atencion'
        
        
class Diagnostico(models.Model):
    iddiagnostico = models.AutoField(db_column='idDiagnostico', primary_key=True)  # Field name made lowercase.
    idpaciente = models.ForeignKey('Paciente', models.PROTECT, db_column='idPaciente')  # Field name made lowercase.
    fecha = models.IntegerField()
    descripcion = models.CharField(max_length=256)
    gravedad = models.CharField(max_length=256)
    tratamiento = models.CharField(max_length=256)
    codigo_cie_10 = models.CharField(db_column='codigo_CIE-10', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'diagnostico'
        
        

class Seguimiento(models.Model):
    idtratamiento = models.AutoField(db_column='idTratamiento', primary_key=True)  # Field name made lowercase.
    idenfermero = models.ForeignKey(Enfermero, models.PROTECT, db_column='idEnfermero')  # Field name made lowercase.
    idpaciente = models.ForeignKey(Paciente, models.PROTECT, db_column='idPaciente')  # Field name made lowercase.
    observacion = models.CharField(max_length=200)
    medicacion = models.CharField(max_length=100)
    signos_vitales = models.CharField(max_length=200)

    class Meta:
        
        db_table = 'seguimiento'
        


class Internacion(models.Model):
    idinternacion = models.AutoField(db_column='idInternacion', primary_key=True)  # Field name made lowercase.
    idpaciente = models.ForeignKey(Paciente, models.PROTECT, db_column='idPaciente')  # Field name made lowercase.
    idhabitacion = models.ForeignKey(Habitacion, models.PROTECT, db_column='idHabitacion')  # Field name made lowercase.
    fecha_admicion = models.DateTimeField()
    fecha_alta = models.DateTimeField()
    nota_ingreso = models.CharField(max_length=256)

    class Meta:
        
        db_table = 'internacion'