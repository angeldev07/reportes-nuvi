from .base import *
from dotenv import load_dotenv
load_dotenv(Path.joinpath(BASE_DIR, '.env'))

 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# En producción se debe cambiar a False
DEBUG = False

# Configuración de CORS
CORS_ALLOW_ALL_ORIGINS = True

# Configuración de ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']


# En caso de que se necesite mas adelante agregar una base de datos diferente a SQLite
# se puede hacer en este archivo solo para producción.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# ===============================================================================================================================
# Configuración de REST_FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    # Otras configuraciones...
}

# ===============================================================================================================================
