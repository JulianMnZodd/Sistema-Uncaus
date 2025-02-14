from django.db import models

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
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    obra_social = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=256)
    diabetes = models.BooleanField()
    hipertension = models.BooleanField()
    fumador = models.BooleanField()
    alergias = models.CharField(max_length=256,blank=True, null=True)
    antecedentes = models.CharField(max_length=256,blank=True, null=True)
    cirugias = models.CharField(max_length=256,blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    
    class Meta:
        managed= True
        db_table = 'paciente'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# class Diagnostico(models.Model):
#     iddiagnostico = models.AutoField(db_column='idDiagnostico', primary_key=True)  # Field name made lowercase.
#     idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idPaciente')  # Field name made lowercase.
#     fecha = models.IntegerField()
#     descripcion = models.CharField(max_length=256)
#     gravedad = models.CharField(max_length=256)
#     tratamiento = models.CharField(max_length=256)
#     codigo_cie_10 = models.CharField(db_column='codigo_CIE-10', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

#     class Meta:
#         managed = True
#         db_table = 'diagnostico'


class ObraSocial(models.Model):
    idobra_social = models.AutoField(db_column='idObra_social', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    cuit = models.IntegerField()
    tipo = models.CharField(max_length=70)

    class Meta:
        managed = True
        db_table = 'obra_social'



class PacienteObraSocial(models.Model):
    idpaciente_obra_social = models.AutoField(db_column='idPaciente_Obra_Social', primary_key=True)  # Field name made lowercase.
    paciente_obra_social = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='Paciente_Obra_Social')  # Field name made lowercase.
    obra_social_paciente = models.ForeignKey(ObraSocial, models.DO_NOTHING, db_column='Obra_Social_Paciente')  # Field name made lowercase.
    nro_afiliado = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'paciente_obra_social'



