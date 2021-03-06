# coding:utf-8

"""
DCRM - Darwin Cydia Repository Manager
Copyright (C) 2017  WU Zheng <i.82@me.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

# Just set this to the first Site instance's id in database.
SITE_ID = 1

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$!#)nxr8rv83s(b%#kg*8a)m%igd+o%2=mgvqkba_zbc3(bpan'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'apt.82flex.com',
    '127.0.0.1',
    'localhost'
]

# Redis
# !!! Change the 'DB' number here if you have multiple DCRM installed !!!
RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 360,
    },
    'high': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 360,
    },
}

# Database
# You cannot use SQLite3 due to the lack of advanced database supports.
# !!! Change the 'NAME' here if you have multiple DCRM installed !!!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DCRM',
        'USER': 'root',
        'PASSWORD': 'r0pavoga',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Paris'

"""
!!! DO NOT EDIT ANYTHING BELOW !!!
!!! 如果你不知道下面各项配置的作用，请勿修改以下任何内容 !!!
"""

INSTALLED_APPS = [
    'WEIPDCRM',
    'WEIPDCRM.apps.SuitConfig',
    'WEIPDCRM.styles.DefaultStyle',
    'preferences',
    "django_rq",
    "suit_redactor",
    'sortedm2m',
    'photologue',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DCRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                "preferences.context_processors.preferences_cp"
            ],
        },
    },
]

WSGI_APPLICATION = 'DCRM.wsgi.application'

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

USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ('en', u'English'),
    ('zh_Hans', u'中文简体'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'WEIPDCRM/static')
STATICFILES_DIRS = [

]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'resources')
MEDIA_URL = '/resources/'
TEMP_ROOT = os.path.join(BASE_DIR, 'temp')
if not DEBUG:
    ENABLE_CACHE = True
    CACHE_TIME = 3600
else:
    ENABLE_CACHE = False
    CACHE_TIME = 0
