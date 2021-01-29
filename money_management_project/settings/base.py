import os
from pathlib import Path
from dotenv import load_dotenv

ENV_PATH = os.path.join(Path(__file__).resolve().parent.parent.parent, '.env')
load_dotenv(ENV_PATH)


def convert_to_bool(string):
    string = str(string)
    return string.lower() in ['true', '1']

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENVIRONMENT = os.environ.get("ENVIRONMENT")

SECRET_KEY = os.environ.get("SECRET_KEY")


ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'user.apps.UserConfig',
    'note.apps.NoteConfig',
    'transaction.apps.TransactionConfig',
    'tag.apps.TagConfig',

    # rest
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # other
    "drf_yasg",
]

WSGI_APPLICATION = 'money_management_project.wsgi.application'
SITE_ID = 1


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'money_management_project.urls'

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

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        "OPTIONS": {
            "min_length": 6
        }
    },
]

AUTHENTICATION_BACKENDS = ['user.backends.AuthBackend']


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'user.serializers.PasswordResetSerializer',
}

CORS_ALLOW_ALL_ORIGINS = True

# emails for sending error mails
ADMINS = [
    ("Farhad", os.environ.get("ADMIN_EMAIL")),
]

# Email settings
SERVER_EMAIL = os.environ.get("SERVER_EMAIL") # used for sending error messages to email
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = convert_to_bool(os.environ.get("EMAIL_USE_TLS"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

