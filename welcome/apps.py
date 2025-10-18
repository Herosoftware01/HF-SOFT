# from django.apps import AppConfig


# class WelcomeConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'welcome'


# apps.py inside your 'welcome' app

from django.apps import AppConfig

class WelcomeConfig(AppConfig):
    name = 'welcome'

    def ready(self):
        import welcome.signals
