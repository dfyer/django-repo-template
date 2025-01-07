# Project
from .base import *


STATIC_URL = "static/"

DEBUG = env('DEBUG') # Default is False
SECRET_KEY = env('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Database from .env
DATABASES = {
    'default': {
        **env.db(),
        'ATOMIC_REQUESTS': True
    }
}

ALLOWED_HOSTS = []

CORS_ALLOWED_ORIGINS = []
