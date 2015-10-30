DEFAULT_SETTINGS = {
    
}

def update_django_settings():
    from django.conf import settings

    for key, value in DEFAULT_SETTINGS.iteritems():
        if not hasattr(settings, key):
            setattr(settings, key, value)