"""
Django settings for plantsproject project.
Generated by 'django-admin startproject' using Django 1.8.5.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from pathlib import Path
#import django_rq
#import django.contrib.auth

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR:", BASE_DIR)
print("PROJECT_ROOT:", PROJECT_ROOT)

# Quick-start development settings - unsuitable for production

# <DIGITAL OCEAN MIGRATION>
from django.core.management.utils import get_random_secret_key
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())


# <DIGITAL OCEAN MIGRATION>
# SECURITY WARNING: don't run with debug turned on in production!
#This allows us to toggle Debug by setting an environment variable (locally or on the server).
DEBUG = os.getenv("DEBUG", "False") == "True" 


# <DIGITAL OCEAN MIGRATION>
# This defines a list of the server’s addresses or domain names that may be used to connect to the Django instance. 
# Any incoming request with a Host header that is not in this list will raise an exception. 
# Django requires that you set this to prevent a certain class of security vulnerability.
# attempt to read the hosts from an environment variable. 
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'plants',
    'login',
    'frontend',
    'django_comments_xtd',
    'django_comments',
    'django.contrib.auth',
    'django.contrib.admin',
    'rest_framework',
    'api',
    #'django_rq',
    #'composer',
)

MIDDLEWARE = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

)

ROOT_URLCONF = 'plantsproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'plantsproject.wsgi.application'

#Django 3.2 Update
DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

#SITE_ID = 2 #should be set to 2 for heroku
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_XTD_CONFIRM_EMAIL = True

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "softwareforagroecosystems@gmail.com"
EMAIL_HOST_PASSWORD = "apse4-cactus"
EMAIL_SUBJECT_PREFIX = "[SAGE] "
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

 
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
# Database

# POSTGRES_DB = os.environ.get("POSTGRES_DB")
# POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
# POSTGRES_USER = os.environ.get("POSTGRES_USER")
# POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
# POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

# POSTGRES_READY = (
#     POSTGRES_DB is not None
#     and POSTGRES_PASSWORD is not None
#     and POSTGRES_USER is not None
#     and POSTGRES_HOST is not None
#     and POSTGRES_PORT is not None
# )

# if POSTGRES_READY:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.postgresql",
#             "NAME": POSTGRES_DB,
#             "USER": POSTGRES_USER,
#             "PASSWORD": POSTGRES_PASSWORD,
#             "HOST": POSTGRES_HOST,
#             "PORT": POSTGRES_PORT,
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-plants',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '../frontend/static'),
)
LOGIN_REDIRECT_URL = '/'
LOGIN_URL="/login"
LOGOUT_REDIRECT_URL="/login"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

AUTH_USER_MODEL = "login.AuthUser"

# RQ_QUEUES = {
#     'default': {
#         'HOST': 'localhost',
#         'PORT': 6379,
#         'DB': 0,
#         'PASSWORD': '',
#         'DEFAULT_TIMEOUT': 360,
#     },
#     'with-sentinel': {
#        'SENTINELS': [('localhost', 26736), ('localhost', 26737)],
#        'MASTER_NAME': 'redismaster',
#        'DB': 0,
#        'PASSWORD': 'secret',
#        'SOCKET_TIMEOUT': None,
#     },
#     'high': {
#         'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'), # If you're on Heroku
#         'DEFAULT_TIMEOUT': 500,
#     },
#     'low': {
#         'HOST': 'localhost',
#         'PORT': 6379,
#         'DB': 0,
#     }
# }
# 
# #RQ_EXCEPTION_HANDLERS = ['path.to.my.handler'] # If you need custom exception handlers
