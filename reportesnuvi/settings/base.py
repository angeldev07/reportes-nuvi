from pathlib import Path
import os

# ===============================================================================================================================

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ===============================================================================================================================

# Application definition

LOCAL_APPS = ["reportes"]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
]

BASE_APPS  = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = BASE_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ===============================================================================================================================

# MIDDLEWARES CONFIGURATION 

BASE_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

LOCAL_MIDDLEWARES = []

THIRD_PARTY_MIDDLEWARES = [
    'corsheaders.middleware.CorsMiddleware',
]

MIDDLEWARE = THIRD_PARTY_MIDDLEWARES + BASE_MIDDLEWARE + LOCAL_MIDDLEWARES

# ===============================================================================================================================

ROOT_URLCONF = "reportesnuvi.urls"

# ===============================================================================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ===============================================================================================================================

WSGI_APPLICATION = "reportesnuvi.wsgi.application"

# ===============================================================================================================================

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ===============================================================================================================================

# Internationalization

LANGUAGE_CODE = "es-CO"

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True

# ===============================================================================================================================

# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ===============================================================================================================================

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ===============================================================================================================================