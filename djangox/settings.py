import os
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4(j*7q=-dm@4&d8hb)-ivy#b(&_3ew19ujzo#h_hq-39!6-5d+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables it
#     # '...
# }

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'sweetify',

    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    'crispy_forms',
    'debug_toolbar',

    # Local
    'users',
    'petitions',
    'mathfilters',
    'debug_permissions',
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

ROOT_URLCONF = 'djangox.urls'

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

WSGI_APPLICATION = 'djangox.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#      'default': {
#          'ENGINE': 'mysql_cymysql',
#          'NAME': 'pomac',
#          'USER': 'root',
#          'PASSWORD': '',
#          'HOST': '127.0.0.1',
#          'PORT': '3306',
#      }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'pomac',
#          'USER': 'postgres',
#          'PASSWORD': 'root',
#          'HOST': '127.0.0.1',
#          'PORT': '5432',
#      }
# }
#
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'itdkpbmo',
#          'USER': 'itdkpbmo',
#          'PASSWORD': 'zNrz30GjX1WBhMhxByUvI_r_KWcU2o9K',
#          'HOST': 'stampy.db.elephantsql.com',
#          'PORT': '5432',
#      }
# }


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Bootstrap Crispy-Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django-debug-toolbar settings
INTERNAL_IPS = ['127.0.0.1']

# Authentication settings
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dwaichari@gmail.com'
EMAIL_HOST_PASSWORD = 'PASSnimimi003'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

AUTH_USER_MODEL = 'users.CustomUser'

# DJANGO-ALLAUTH SETTINGS
# Site id required for using 'sites' framework with django-allauth
SITE_ID = 1


LOGIN_REDIRECT_URL = 'petitions_dashboard'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGOUT_ON_GET = True

# Don't collect usernames, use email instead
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_SIGNUP_FORM_CLASS = "users.forms.CustomSignupForm"


# default is 'True', use 'optional' for development purposes
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_UNIQUE_EMAIL = True

# default is 'True', only force user to enter password once
#ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =True

# controls life time of the session, default is 'None' to ask user "Remember me?"
ACCOUNT_SESSION_REMEMBER = None


django_heroku.settings(locals())

USE_TZ = False