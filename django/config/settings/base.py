import os
from pathlib import Path

from dotenv import load_dotenv

from django.utils.translation import gettext

# django.utils.translation.ugettext = gettext

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# .env 파일 경로
env_path = os.path.join(BASE_DIR, ".env")

# .env 파일이 없을 경우 파일 생성
if not os.path.exists(env_path):
    with open(env_path, "w") as env_file:
        env_file.write(
            "DB_NAME=oz_03_collabo_01_babydog\n"
            "DB_USER=myuser\n"
            "DB_PASSWORD=mypassword\n"
            "DB_HOST=localhost\n"
            "DB_PORT=5432\n\n"
            "GOOGLE_CLIENT_ID=your_google_client_id_value\n"
            "OTHER_ENV_VARIABLE=your_value\n"
            "GOOGLE_CLIENT_SECRET=efef\n"
            "GOOGLE_REDIRECT_URI=ef\n"
            "GOOGLE_SOCIAL_KEY=efef\n"
        )

# .env 파일을 로드
load_dotenv(os.path.join(BASE_DIR, ".env"))

# 서비스 배포시 수정해야함.
SECRET_KEY = "django-insecure-g2$d_7hc#kw_^2%6sk4va_&xg1gsd#s8mgwwbi)r7+fkli4c^m"

# 서비스 배포시 False
DEBUG = True

ALLOWED_HOSTS = []


AUTH_USER_MODEL = "users.CustomUser"

# Application definition
DEFAULT_DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "users.apps.UsersConfig",
    "places.apps.PlacesConfig",
    "common.apps.CommonConfig",
]

CUSTOM_INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.naver",
    "rest_framework.authtoken",
]

INSTALLED_APPS = DEFAULT_DJANGO_APPS + CUSTOM_APPS + CUSTOM_INSTALLED_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware", csrf꺼두고 테스트 진행중
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

# 모든 출처를 허용하려면 (개발 환경에서만 사용하는 것이 좋습니다)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True  # 쿠키 및 인증 헤더를 허용합니다.

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# SESSION_COOKIE_DOMAIN = 'localhost:5173/'
# SESSION_COOKIE_PATH = '/'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = "config.urls"

SITE_ID = 1

# Google allauth 설정
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

GOOGLE_OAUTH2_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_OAUTH2_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
# Google 소셜 로그인 제공자 설정
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": GOOGLE_CLIENT_ID,
            "secret": GOOGLE_CLIENT_SECRET,
            "key": os.getenv("GOOGLE_SOCIAL_KEY"),
        }
    }
}


# 로그인 후 리디렉션할 URL
LOGIN_REDIRECT_URL = "/"
# 로그아웃 후 리디렉션할 URL
LOGOUT_REDIRECT_URL = "/"


# 계정 관련 기본 설정
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# 마이그레이션 오류로 sqllite로 진행함
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER"),
#         "PASSWORD": os.getenv("DB_PASSWORD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": os.getenv("DB_PORT"),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
