from django.apps import AppConfig


class ShoppingConfig(AppConfig):
    name = 'store'

    def ready(self):
        import store.signals
