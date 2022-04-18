"""
Django settings for urba_web project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$lr+=0@f0s#(%jm*6z-j7b2o182ivxe%u&f-pbtcp)8jeju%a$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#SECRET_KEY = os.environ.get("SECRET_KEY")
#DEBUG = int(os.environ.get("DEBUG", default=0))
# 'DJANGO_ALLOWED_HOSTS' должен быть в виде одной строки с хостами разделенными символом пробела
# Для примера: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
#ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    'home.apps.HomeConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
ROOT_URLCONF = 'urba_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #тут указывается где django искать шаблоны
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

WSGI_APPLICATION = 'urba_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

#DATABASES = {
#    "default": {
#        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
#        "USER": os.environ.get("SQL_USER", "user"),
#        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#        "HOST": os.environ.get("SQL_HOST", "localhost"),
#        "PORT": os.environ.get("SQL_PORT", "5432"),
#    }
#}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #собрать местную статику

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'urba_web/static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = ["127.0.0.1"]

#Настройка отправики писем

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 #2525
EMAIL_HOST_USER = 'imandreywebdeveloper@gmail.com'
EMAIL_HOST_PASSWORD = 'S0AkSqvxYsWB'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

#Настройка капчи
CKEDITOR_UPLOAD_PATH = "uploads/"
#Доп настройки для капчи
#CAPTCHA_LETTER_ROTATION = None
CAPTCHA_NOISE_FUNCTIONS = None

#настройка кэширования
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
    }
}
LOGGING ={
    'version':1,
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,

        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './logs/debug2.log',
            'formatter':'simpleRE',
        }
    },
    'formatters':{
        'simpleRE':{
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style':'{',
        }
    }
}






