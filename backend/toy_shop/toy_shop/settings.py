from pathlib import Path
from os import environ

from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d M Y H:i:s"
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-z-8cjo2w+i9pqq9r^gr$p7w^%2-j-#52ty+$luzv5oh9-)^&dq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ.get('DEBUG', True)

ALLOWED_HOSTS = [
    'backend', 'localhost', '139.28.222.160', 'bird-and-star.ru',
]


# Application definition

INSTALLED_APPS = [     
    'rest_framework',
    'corsheaders',
    'django.contrib.auth',    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',    
    'buying',   
    'users', 
    'cart',
    'shop',
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",    
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',    
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',       
]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',    
]


ROOT_URLCONF = 'toy_shop.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'toy_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB', 'db_name'),
        'USER' : environ.get('POSTGRES_USER', 'user_name'),
        'PASSWORD' : environ.get('POSTGRES_PASSWORD', 'password'),
        'HOST' : environ.get('HOST_DB', 'localhost'),
        'PORT' : '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#STATICFILES_DIRS  = BASE_DIR / "statics"
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}

CORS_ALLOW_CREDENTIALS = True #cookie разрешены 