import os

BASE_DIR = os.path.dirname(
	os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(" ")
WSGI_APPLICATION = os.environ.get('WSGI_APPLICATION', 'alumni.wsgi.dev.application')
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST').split(" ")

DJANGO_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',
]
PACKAGE_APPS = [
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'corsheaders',
	'rest_auth',
	'rest_auth.registration',
	'rest_framework',
	'rest_framework.authtoken',
]
OWNER_APPS = [
	'users',
]

INSTALLED_APPS = DJANGO_APPS + PACKAGE_APPS + OWNER_APPS

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

ROOT_URLCONF = 'alumni.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'build')],
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
SITE_ID = 1

DATABASES = {
	"default": {
		"ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
		"NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
		"USER": os.environ.get("SQL_USER", "users"),
		"PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
		"HOST": os.environ.get("SQL_HOST", "localhost"),
		"PORT": os.environ.get("SQL_PORT", "5432"),
	}
}

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
	),
}

CSRF_COOKIE_NAME = "csrftoken"

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
AUTH_USER_MODEL = 'users.User'

REST_AUTH_SERIALIZERS = {
	'USER_DETAILS_SERIALIZER': 'users.serializers.UserSerializer',
	'TOKEN_SERIALIZER': 'users.serializers.TokenSerializer'
}

REST_AUTH_REGISTER_SERIALIZERS = {
	'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer',
}
