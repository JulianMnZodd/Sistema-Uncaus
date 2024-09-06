from django.db import models
from personal.models import Persona
# Create your models here.

class Paciente(models.Model):
    idpaciente = models.OneToOneField(Persona, models.DO_NOTHING, db_column='idPaciente', primary_key=True)  # Field name made lowercase.
    obra_social = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'paciente'

class Diagnostico(models.Model):
    iddiagnostico = models.AutoField(db_column='idDiagnostico', primary_key=True)  # Field name made lowercase.
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idPaciente')  # Field name made lowercase.
    fecha = models.IntegerField()
    descripcion = models.CharField(max_length=256)
    gravedad = models.CharField(max_length=256)
    tratamiento = models.CharField(max_length=256)
    codigo_cie_10 = models.CharField(db_column='codigo_CIE-10', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'diagnostico'


class ObraSocial(models.Model):
    idobra_social = models.AutoField(db_column='idObra_social', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    cuit = models.IntegerField()
    tipo = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'obra_social'



class PacienteObraSocial(models.Model):
    idpaciente_obra_social = models.AutoField(db_column='idPaciente_Obra_Social', primary_key=True)  # Field name made lowercase.
    paciente_obra_social = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='Paciente_Obra_Social')  # Field name made lowercase.
    obra_social_paciente = models.ForeignKey(ObraSocial, models.DO_NOTHING, db_column='Obra_Social_Paciente')  # Field name made lowercase.
    nro_afiliado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'paciente_obra_social'


class SignosVitales(models.Model):
    idsignos_vitales = models.AutoField(db_column='idSignos_vitales', primary_key=True)  # Field name made lowercase.
    temperatura_corporal = models.CharField(max_length=45)
    pulso = models.CharField(max_length=45)
    frecuencia_respiratoria = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'signos_vitales'
