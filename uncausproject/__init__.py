from __future__ import absolute_import, unicode_literals

# Esto asegurará que la aplicación Celery se cargue cuando Django se inicie
from celery_app import app as celery_app

__all__ = ('celery_app',)