from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistemuncaus.settings')

app = Celery('sistemuncaus')

# Cargar la configuración de Celery desde el archivo de configuración de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks from all registered Django app configs
app.autodiscover_tasks()

from celery_app import Celery
from celery.schedules import crontab

app.conf.beat_schedule = {
    'liberar-camas-expiradas-cada-dia': {
        'task': 'internacion.tasks.liberar_camas_expiradas',
        'schedule': crontab(hour=0, minute=0),  # Ejecutar todos los días a medianoche
    },
}