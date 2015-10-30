from django.apps import AppConfig

__title__ = 'django-bluebox'
__version__ = '0.0.1'
__license__ = 'MIT'


class BlueboxAppConfig(AppConfig):
    name = __title__
    label = 'bluebox'
    verbose_name = 'Django Bluebox'

default_app_config = 'BlueboxAppConfig'
