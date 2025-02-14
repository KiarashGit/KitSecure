from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bruf#a3wzcbxc^e-gg#v#@#c*_^=1(+_mwqugzc%rg5uf#@m^h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps 
    'account',
    'home',

    # frame works
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'rest_framework_simplejwt.token_blacklist',
    'mozilla_django_oidc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'KhaSecure.urls'

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

WSGI_APPLICATION = 'KhaSecure.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'statics'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'account.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'account.keycloak_auth_backend.KeycloakAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_SCHEMA_CLASS':
        'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Shorten token lifespan
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

AUTHENTICATION_BACKENDS = [
    "account.keycloak_auth_backend.KeycloakOIDCBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# region keycloak

OIDC_RP_CLIENT_ID = 'KharazmiID'
OIDC_RP_CLIENT_SECRET = 'N7FiFW0gebOn2rNmnELj9eXm1Jdg3coX'

OIDC_OP_AUTHORIZATION_ENDPOINT = 'http://localhost:8080/realms/Kharazmi/protocol/openid-connect/auth'
OIDC_OP_TOKEN_ENDPOINT = 'http://localhost:8080/realms/Kharazmi/protocol/openid-connect/token'
OIDC_OP_USER_ENDPOINT = 'http://localhost:8080/realms/Kharazmi/protocol/openid-connect/userinfo'
OIDC_OP_JWKS_ENDPOINT = 'http://localhost:8080/realms/Kharazmi/protocol/openid-connect/certs'
OIDC_RP_SIGN_ALGO = 'RS256'

# OIDC_USERNAME_ALGO = lambda claims: claims.get('preferred_username') or claims.get('email') or claims.get('sub')
OIDC_USERNAME_ALGO = lambda claims: claims.get('preferred_username', '') if isinstance(claims, dict) else ''

# LOGIN_REDIRECT_URL = '/login_message/'  # Adjust to frontend URL
# LOGOUT_URL = 'http://localhost:8080/realms/Kharazmi/protocol/openid-connect/logout'


LOGIN_URL = '/oidc/authenticate/'
LOGOUT_URL = 'account/logout'

OIDC_CREATE_USER = True  # Optional, allows automatic user creation
OIDC_RP_IDP_SIGN_KEY = None  # Optional, set if your Keycloak has custom signing
OIDC_USE_NONCE = True  # Enable nonce for security
OIDC_USE_PKCE = False  # Enable PKCE if supported by your provider

# SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# endregion
