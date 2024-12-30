# Generated by Django 5.1 on 2024-12-24 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcionista',
            name='turno',
            field=models.CharField(blank=True, choices=[('M', 'Mañana'), ('T', 'Tarde')], max_length=10),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
