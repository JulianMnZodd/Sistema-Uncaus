from django.db import models

class ObraSocial(models.Model):
    idobra_social = models.AutoField(db_column='idObra_social', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    cuit = models.IntegerField()
    tipo = models.CharField(max_length=70)

    class Meta:
        managed = True
        db_table = 'obra_social'

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    idpaciente = models.AutoField(db_column='idPaciente', primary_key=True)  # Clave primaria
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], blank=True)
    obra_social = models.ForeignKey(ObraSocial, models.SET_NULL, db_column='idObra_social', blank=True, null=True)  # Relación con ObraSocial
    nro_afiliado = models.IntegerField(blank=True, null=True)  # Número de afiliado
    descripcion = models.CharField(max_length=256)
    diabetes = models.BooleanField()
    hipertension = models.BooleanField()
    fumador = models.BooleanField()
    alergias = models.CharField(max_length=256, blank=True, null=True)
    antecedentes = models.CharField(max_length=256, blank=True, null=True)
    cirugias = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'paciente'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


