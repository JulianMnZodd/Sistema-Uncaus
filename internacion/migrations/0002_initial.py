# Generated by Django 5.1 on 2024-12-23 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habitaciones', '0001_initial'),
        ('internacion', '0001_initial'),
        ('pacientes', '0001_initial'),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='idmedico',
            field=models.ForeignKey(db_column='idMedico', on_delete=django.db.models.deletion.DO_NOTHING, to='personal.medico'),
        ),
        migrations.AddField(
            model_name='atencion',
            name='idpaciente',
            field=models.ForeignKey(db_column='idPaciente', on_delete=django.db.models.deletion.DO_NOTHING, to='pacientes.paciente'),
        ),
        migrations.AddField(
            model_name='internacion',
            name='cama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitaciones.cama'),
        ),
        migrations.AddField(
            model_name='internacion',
            name='idpaciente',
            field=models.ForeignKey(db_column='idPaciente', on_delete=django.db.models.deletion.DO_NOTHING, to='pacientes.paciente'),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='idenfermero',
            field=models.ForeignKey(db_column='idEnfermero', on_delete=django.db.models.deletion.DO_NOTHING, to='personal.enfermero'),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='idpaciente',
            field=models.ForeignKey(db_column='idPaciente', on_delete=django.db.models.deletion.DO_NOTHING, to='pacientes.paciente'),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='medicacion',
            field=models.ForeignKey(db_column='medicacion', on_delete=django.db.models.deletion.DO_NOTHING, to='internacion.medicacion'),
        ),
        migrations.AddField(
            model_name='seguimiento',
            name='signos_vitales',
            field=models.ForeignKey(db_column='signos_vitales', on_delete=django.db.models.deletion.DO_NOTHING, to='internacion.signosvitales'),
        ),
    ]
