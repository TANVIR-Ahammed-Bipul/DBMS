from django.apps import AppConfig

class CoreConfig(AppConfig):  # Change 'CoreConfig' to the actual class name for your app
    name = 'core'  # Change 'core' to your actual app name

    def ready(self):
        import core.signals  # Make sure signals are imported
