from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'usuario',
        'HOST': 'localhost',
        'PASSWORD': 'contrasenia123'
    }
}