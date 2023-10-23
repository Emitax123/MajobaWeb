from django.apps import AppConfig


class MajobawebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MajobaWebApp'

    def ready(self):
        from .views import create_notification
