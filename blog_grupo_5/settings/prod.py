import os
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lucasNahuel$default',
        'USER': 'lucasNahuel',
        'HOST': 'lucasNahuel.mysql.pythonanywhere-services.com',
        'PASSWORD': 'contrasenia123'
    }
}

DEBUG = False

ALLOWED_HOSTS = ['lucasNahuel.pythonanywhere.com']

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')