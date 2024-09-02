from django.db import models

# Create your models here.

class Cama(models.Model):
    idcama = models.AutoField(db_column='idCama', primary_key=True)  # Field name made lowercase.
    nro_cama = models.TextField()
    estado = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'cama'
        
        
class Habitacion(models.Model):
    idhabitacion = models.AutoField(db_column='idHabitacion', primary_key=True)  # Field name made lowercase.
    idsector = models.ForeignKey('Sector', models.PROTECT, db_column='idSector')  # Field name made lowercase.
    idcama = models.ForeignKey(Cama, models.PROTECT, db_column='idCama')  # Field name made lowercase.
    numero = models.IntegerField()
    piso = models.IntegerField()
    cantidad_camas = models.IntegerField()
    es_privada = models.IntegerField()
    es_vip = models.IntegerField()
    tipo = models.CharField(max_length=256)
    disponibilidad = models.IntegerField()

    class Meta:
        
        db_table = 'habitacion'

class Sector(models.Model):
    idsector = models.AutoField(db_column='idSector', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=256)
    cantidad_habitaciones = models.IntegerField()
    piso = models.IntegerField()

    class Meta:
        
        db_table = 'sector'