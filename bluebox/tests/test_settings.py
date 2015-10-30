

ROOT_URLCONF = 'bluebox.tests.testapp.urls'
SECRET_KEY = "test-app"

INSTALLED_APPS = [
    "bluebox.tests.testapp",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "bluebox",
        'TEST_NAME': 'test-bluebox',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

MIDDLEWARE_CLASSES = ()
