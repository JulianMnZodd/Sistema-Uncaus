from django.apps import AppConfig

class TuAppConfig(AppConfig):
    name = 'habitaciones'

    def ready(self):
        import habitaciones.signals  # Importa los signals cuando la app esté lista
