# Generated by Django 5.1 on 2024-12-30 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_recepcionista_turno_alter_persona_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enfermero',
            old_name='persona_idpersona',
            new_name='persona',
        ),
        migrations.RenameField(
            model_name='medico',
            old_name='persona_idpersona',
            new_name='persona',
        ),
        migrations.RenameField(
            model_name='recepcionista',
            old_name='persona_idpersona',
            new_name='persona',
        ),
    ]
