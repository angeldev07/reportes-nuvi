from .base import * 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d4gu+x4ceh%&j)bi3im5-_ix9p)f^d*@reaccir7ofguy05su4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

