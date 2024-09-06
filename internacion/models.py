from django.db import models
from personal.models import Enfermero,Medico
from pacientes.models import Paciente,SignosVitales
from habitaciones.models import Habitacion

# Create your models here.


class Atencion(models.Model):
    idatencion = models.AutoField(db_column='idAtencion', primary_key=True)  # Field name made lowercase.
    idmedico = models.ForeignKey(Medico, models.DO_NOTHING, db_column='idMedico')  # Field name made lowercase.
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idPaciente')  # Field name made lowercase.
    fecha = models.DateTimeField()
    detalles = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'atencion'

class Internacion(models.Model):
    idinternacion = models.AutoField(db_column='idInternacion', primary_key=True)  # Field name made lowercase.
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idPaciente')  # Field name made lowercase.
    idhabitacion = models.ForeignKey(Habitacion, models.DO_NOTHING, db_column='idHabitacion')  # Field name made lowercase.
    fecha_admicion = models.DateTimeField()
    fecha_alta = models.DateTimeField()
    nota_ingreso = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'internacion'


class Medicacion(models.Model):
    idmedicacion = models.AutoField(db_column='idMedicacion', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    hora_medicacion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'medicacion'

class Seguimiento(models.Model):
    idtratamiento = models.AutoField(db_column='idTratamiento', primary_key=True)  # Field name made lowercase.
    idenfermero = models.ForeignKey(Enfermero, models.DO_NOTHING, db_column='idEnfermero')  # Field name made lowercase.
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idPaciente')  # Field name made lowercase.
    observacion = models.CharField(max_length=200)
    medicacion = models.ForeignKey(Medicacion, models.DO_NOTHING, db_column='medicacion')
    signos_vitales = models.ForeignKey(SignosVitales, models.DO_NOTHING, db_column='signos_vitales')

    class Meta:
        managed = False
        db_table = 'seguimiento'
        