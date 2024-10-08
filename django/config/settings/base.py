import os
from datetime import timedelta
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
            "NAVER_CLIENT_ID=your_naver_client_id\n"
            "NAVER_CLIENT_SECRET=your_naver_client_secret\n"
            "NAVER_SOCIAL_KEY=your_naver_social_key\n"
            "KAKAO_CLIENT_ID=your_kakao_client_id\n"
            "KAKAO_CLIENT_SECRET=your_kakao_client_secret\n"
            "KAKAO_SOCIAL_KEY=your_kakao_social_key\n"
        )

# .env 파일을 로드
load_dotenv(os.path.join(BASE_DIR, ".env"))

# 서비스 배포시 수정해야함.(물어보기)
SECRET_KEY = os.getenv("SECRET_KEY")

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
    "rest_framework",
    "drf_yasg",
    "django_cleanup.apps.CleanupConfig",
    "storages",
]

INSTALLED_APPS = DEFAULT_DJANGO_APPS + CUSTOM_APPS + CUSTOM_INSTALLED_APPS

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = "config.urls"

SITE_ID = 1

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware", csrf꺼두고 테스트 진행중
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# Google allauth 설정
# Google 설정
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
GOOGLE_SOCIAL_KEY = os.getenv("GOOGLE_SOCIAL_KEY")

# Naver 설정
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

# Kakao 설정
KAKAO_CLIENT_ID = os.getenv("KAKAO_CLIENT_ID")
KAKAO_CLIENT_SECRET = os.getenv("KAKAO_CLIENT_SECRET")
KAKAO_SOCIAL_KEY = os.getenv("KAKAO_SOCIAL_KEY")

# Google 소셜 로그인 제공자 설정
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "key": os.getenv("GOOGLE_SOCIAL_KEY"),
        }
    },
    "naver": {
        "APP": {
            "client_id": os.getenv("NAVER_CLIENT_ID"),
            "secret": os.getenv("NAVER_CLIENT_SECRET"),
            "key": os.getenv("NAVER_SOCIAL_KEY"),
        }
    },
    "kakao": {
        "APP": {
            "client_id": os.getenv("KAKAO_CLIENT_ID"),
            "secret": os.getenv("KAKAO_CLIENT_SECRET"),
            "key": os.getenv("KAKAO_SOCIAL_KEY"),
        }
    },
}

# jwt토큰 값 설정
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=int(os.getenv("ACCESS_TOKEN_LIFETIME_MINUTES", 1))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.getenv("REFRESH_TOKEN_LIFETIME_DAYS", 7))),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "email",  # 사용자 모델에서 ID로 사용되는 필드
    "USER_ID_CLAIM": "email",  # JWT 클레임에서 ID를 나타내는 필드 이름
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "AUTH_COOKIE": "access_token",  # 쿠키에 사용될 키 이름
    "AUTH_COOKIE_SECURE": True,  # HTTPS에서만 쿠키 전송
    "AUTH_COOKIE_HTTP_ONLY": True,  # JavaScript에서 쿠키에 접근 불가
    "AUTH_COOKIE_PATH": "/",  # 쿠키의 경로
    "AUTH_COOKIE_SAMESITE": "Strict",  # CSRF 방지
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


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "authentication.custom_authentication.CustomJWTAuthentication",
    ],
}
