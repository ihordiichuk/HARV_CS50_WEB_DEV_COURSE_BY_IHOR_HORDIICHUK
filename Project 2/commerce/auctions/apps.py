from django.apps import AppConfig

class AuctionsConfig(AppConfig):
    # Default primary key field type for models
    default_auto_field = 'django.db.models.BigAutoField'

    # Name of the Django app
    name = 'auctions'