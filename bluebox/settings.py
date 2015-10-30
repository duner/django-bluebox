DEFAULT_SETTINGS = {
    BLUEBOX_PARSER = {}
    BLUEBOX_APPLE_NEWS_PARSER: {}
    BLUEBOX_AMP_HTML_PARSER: {}
    BLUEBOX_FB_INSTANT_ARTICLES_PARSER: {}
}

def update_django_settings():
    from django.conf import settings
    
    for key, value in DEFAULT_SETTINGS.iteritems():
        if not hasattr(settings, key):
            setattr(settings, key, value)