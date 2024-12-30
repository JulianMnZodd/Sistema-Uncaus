from django.db import models
from pacientes.models import Paciente
# Create your models here.

class Sector(models.Model):
    idsector = models.AutoField(db_column='idSector', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=256)
    cantidad_habitaciones = models.IntegerField()
    piso = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sector'

class Habitacion(models.Model):
    idhabitacion = models.AutoField(db_column='idHabitacion', primary_key=True)  # Field name made lowercase.
    idsector = models.ForeignKey(Sector, models.DO_NOTHING, db_column='idSector')  # Field name made lowercase.
    numero = models.IntegerField()
    piso = models.IntegerField()
    cantidad_camas = models.IntegerField()
    es_privada = models.BooleanField()
    es_vip = models.BooleanField()
    tipo = models.CharField(max_length=256)
    
    def __str__(self):
        return f"Habitación #{self.numero}"

    class Meta:
        managed= True
        db_table = 'habitacion'

class Cama(models.Model):
    
    ESTADOS = (
        ('L', 'Libre'),
        ('O', 'Ocupada'),
    )
    
    idcama = models.AutoField(db_column='idCama', primary_key=True)  # Field name made lowercase.
    habitacion = models.ForeignKey(Habitacion, models.DO_NOTHING, db_column='idHabitacion', related_name='camas')  # Relación inversa.
    estado = models.CharField(max_length=1, choices=ESTADOS, default='L')
    paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idPaciente',blank=True,null=True)  # Field name made lowercase.
    def __str__(self):
        return f"Cama en {self.habitacion.numero}"

    class Meta:
        managed: True
        db_table = 'cama'





