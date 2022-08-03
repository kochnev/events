from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ui$dqal%9(%^2b5027p%h$57@gq-#1&21&g_v)t(-)lb-oq=zk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'events',
        'USER': 'events_admin',
        'PASSWORD': '123456789',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

