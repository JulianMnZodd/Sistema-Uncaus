# Generated by Django 5.1 on 2024-12-30 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_rename_persona_idpersona_enfermero_persona_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='username',
        ),
    ]
