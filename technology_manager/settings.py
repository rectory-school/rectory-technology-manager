"""
Django settings for technology_manager project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from environment import *

ADMINS = (('Adam Peacock', 'adam.peacock@rectoryschool.org'), )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_&d5-snr-p5i)7wf!4-lolafr$56n-2&31132xov=4r-=+l6a)'

EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_ACCESS_KEY_ID = 'AKIAJID26NSVBB2J6UPA'
AWS_SECRET_ACCESS_KEY = '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'

SERVER_EMAIL = 'technology@rectoryschool.org'

RQ_QUEUES = {
  'default': {
    'HOST': 'localhost',
    'PORT': 6379,
    'DB': 0,
    'DEFAULT_TIMEOUT': 360,
  },
  'syncthing_configurator': {
    'HOST': 'localhost',
    'PORT': 6379,
    'DB': 0,
    'DEFAULT_TIMEOUT': 600
  }
}

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = ('adminsortable', "django_rq",)

INTERNAL_APPS = (
	'munkimanager', 
  'syncthingmanager',
  'academics',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + INTERNAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'technology_manager.urls'

WSGI_APPLICATION = 'technology_manager.wsgi.application'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'rq_console': {
      'format': '%(asctime)s %(message)s',
      'datefmt': '%H:%M:%S',
    },
  },
  'handlers': {
    'rq_console': {
      'level': 'INFO',
      'class': 'rq.utils.ColorizingStreamHandler',
      'formatter': 'rq_console',
      'exclude': ['%(asctime)s'],
      
    },
    'mail_admins': {
      'level': 'ERROR',
      'class': 'django.utils.log.AdminEmailHandler',
    }
  },
  'loggers': {
    'rq.worker': {
      'handlers': ['rq_console', 'mail_admins']
    }
  }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
