from .base import *

# SECRET_KEY = get_env_variable('SECRET_KEY')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': get_env_variable('DB_NAME'),
#         'USER': get_env_variable('DB_USER'),
#         'PASSWORD': get_env_variable('DB_PASSWORD'),
#         'HOST': get_env_variable('DB_HOST'),
#         'PORT': get_env_variable('DB_PORT'),
#     }
# }
DEBUG = False

SECRET_KEY = 'django-insecure-ui$dqal%9(%^2b5027p%h$57@gq-#1&21&g_v)t(-)lb-oq=zk'

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


ALLOWED_HOSTS = ['dili-event.com','www.dili-event.com']
