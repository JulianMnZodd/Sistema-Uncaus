# Generated by Django 5.1 on 2025-02-22 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internacion', '0003_diagnostico_idinternacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internacion',
            old_name='fecha_admicion',
            new_name='fecha_admision',
        ),
    ]
