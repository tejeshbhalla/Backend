"""
Django settings for Varency project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+)0aq35x-7qx!-7d%0cb*z227f+%yd3df4-8l*$i4h02t8(9^2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["api.varency.com",'localhost','tewg7.localtonet.com']

USE_X_FORWARDED_HOST = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'files.apps.FilesConfig',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_simplejwt',
    'corsheaders',
    'content.apps.ContentConfig',
    'ftp.apps.FtpConfig',
    'django_clamav',

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'Varency.rate_limit.RateLimitMiddleware',
    'Varency.referer_middleware.RefererMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'files.throttling.RateThrottle',
    
]
THROTTLE_RATES = {
    'myapi': '100/minute',
}

ROOT_URLCONF = 'Varency.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static', 
            }
        },
    },
]
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')


WSGI_APPLICATION = 'Varency.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER':'myprojectuser',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':'',
    }
}






# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema',

}




AUTH_USER_MODEL='files.NewUser'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#CORS_ALLOWED_ORIGINS = ['*']


CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.varency\.com$",
     r"^https://varency\.com$",
     r"^https://mail.google\.com$",
     r"^https://outlook.office\.com$",
      r"^https://outlook.office365\.com$",
      r"^https://ba26-223-190-82-174.ngrok\.io$",
      r"^http://tejesh\.localhost:3000$",
    
    

]

#email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER='noreply@varency.com'
EMAIL_HOST='us2.smtp.mailhostbox.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_PASSWORD='LLdsEPl4'


EXPIRY_SAS_TIME=15


FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880


#azure settings 
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = "filesmodelapp"
AZURE_ACCOUNT_KEY='Z5GLgOxy6HsZtbtOlwHOet5r1aZjdjKPAGYAlaEq/1fm8hwhpMYktxqHxaaIJ9udewnlsLrZ2v2r+AStbrgpZA=='
AZURE_CONTAINER='filesapp'
AZURE_SSL=True
AZURE_URL_EXPIRATION_SECS=timedelta(seconds=600).seconds
AZURE_CONNECTION_STRING='DefaultEndpointsProtocol=https;AccountName=filesmodelapp;AccountKey=Z5GLgOxy6HsZtbtOlwHOet5r1aZjdjKPAGYAlaEq/1fm8hwhpMYktxqHxaaIJ9udewnlsLrZ2v2r+AStbrgpZA==;EndpointSuffix=core.windows.net'



#url
FRONT_END_URL="varency.com/"


#function url
FUNC_URL='https://one-drive-sync.azurewebsites.net/api/orchestrators'
POST_URL='https://api.Varency.com/api/api/content/upload/file/'
SECRET_KEY_FUNC='AZURE_SYNC_Varency_8130173515'
#celery
CELERY_ENABLED=True
CELERY_BROKER_URL="amqps://wuouwjuy:aonSVk3-GtIOqSVvLL2pVISXj93TegWX@puffin.rmq2.cloudamqp.com/wuouwjuy"
CELERY_ACCEPT_CONTENT=['json']
CELERY_TASK_SERIALIZER='json'


#rclone_config
client_id = "986322288750-9cbcmheaaj78eqsbprt7qd7tim5m3c00.apps.googleusercontent.com"
client_secret = "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"

#google drive 
CLIENT_ID = '439305909942-2u20aq9v6jsn2okfpjd3tu5rhmdt991u.apps.googleusercontent.com'
CLIENT_SECRET_GOOGLE_DRIVE = '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'
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
REDIRECT_URI = 'https://api.varency.com/api/sync/google_drive/get_token'
TOKEN_URL_GOOGLE_DRIVE='https://accounts.google.com/o/oauth2/token'

#onedrive
CLIENT_ID_ONEDRIVE="c440bdf8-ff79-483e-be61-e653fbdb511b"
SCOPES_ONEDRIVE='files.read.all offline_access  files.readwrite.all sites.read.all sites.readwrite.all'
REDIRECT_URI_ONEDRIVE="https://api.varency.com/api/sync/get_token"
TOKEN_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
CLIENT_SECRET='eBA8Q~qUzW5kPTiMHUCowR1LG2zM1MYZcjZgXdya'


CSRF_TRUSTED_ORIGINS=["https://api.varency.com"]
#clam av
CLAMAV_UNIX_SOCKET = '/var/run/clamav/clamd.ctl'
CLAMAV_USE_TCP = False
CLAMAV_TCP_PORT = 3310
CLAMAV_TCP_ADDR = '127.0.0.1'
CLAMAV_ENABLED = False

BACKEND_URL='https://api.varency.com/'


ALLOWED_REFERERS = ['http://*.localhost:3000/', 'https://*.varency.com/','https://mail.google.com/','https://outlook.office.com/','https://outlook.office365.com/','https://login.microsoftonline.com/','https://varency.com/']

AWS_HEADERS = {
    'x-amz-server-side-encryption': 'aws:kms',
    'x-amz-server-side-encryption-aws-kms-key-id': '341e4021-6344-42d7-adbf-54f05b71c1ab'
}


#drm info
API_SECRET_KEY = "9WZ5eJyoIW0oHVvTIs8h0VPrm8eVsuU5lck77l47dHnV3AnaPwyK8EEDc41t8VoC"
UPLOAD_URL_VDOCIPHER='https://dev.vdocipher.com/api/videos'
VIDEO_STATUS_URL_VDOCIPHER='https://dev.vdocipher.com/api/videos/'
CONVERTER_URL='http://127.0.0.1:5000/convert'
LOCAL_STORAGE_PATH='content/videos'