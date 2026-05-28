from pathlib import Path

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

    # WhiteNoise for Render Static Files
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

# WhiteNoise Static File Storage

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ================= MEDIA FILES =================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# ================= DEFAULT AUTO FIELD =================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ================= EMAIL SETTINGS =================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'vinothkumarj651@gmail.com'

EMAIL_HOST_PASSWORD = 'vwyf wacy fojh frdj'