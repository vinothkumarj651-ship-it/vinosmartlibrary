from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ================= SECRET KEY =================

SECRET_KEY = 'django-insecure-change-this-key'

# ================= DEBUG =================

DEBUG = True

ALLOWED_HOSTS = ['*']

# ================= INSTALLED APPS =================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'books',

]

# ================= MIDDLEWARE =================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# ================= ROOT URL =================

ROOT_URLCONF = 'smartlibrary.urls'

# ================= TEMPLATES =================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates'
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]

# ================= WSGI =================

WSGI_APPLICATION = 'smartlibrary.wsgi.application'

# ================= DATABASE =================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}

# ================= PASSWORD VALIDATION =================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]

# ================= LANGUAGE =================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# ================= STATIC FILES =================

STATIC_URL = '/static/'

STATICFILES_DIRS = [

    BASE_DIR / 'static'

]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ================= MEDIA FILES =================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# ================= DEFAULT AUTO FIELD =================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ================= RESEND SETTINGS =================

RESEND_API_KEY = os.getenv("RESEND_API_KEY")