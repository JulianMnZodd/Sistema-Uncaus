# mi_app/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/camas/$', consumers.CamaConsumer.as_asgi()),  # Ruta WebSocket para el estado de camas
]
