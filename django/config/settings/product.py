from .base import *

DEBUG = False

# 로드 밸런스 사용시 ip 더 추가
ALLOWED_HOSTS = ["api.dogandbaby.co.kr", "www.dogandbaby.co.kr", "13.125.130.26", "example.com", "web"]

CORS_ALLOWED_ORIGINS = [
    "http://api.dogandbaby.co.kr",
    "https://api.dogandbaby.co.kr",
    "http://www.dogandbaby.co.kr",
    "https://www.dogandbaby.co.kr",
]

CSRF_TRUSTED_ORIGINS = ["https://api.dogandbaby.co.kr"]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True  # 쿠키 및 인증 헤더를 허용합니다.
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True  # HTTPS에서만 CSRF 쿠키 전송
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

CORS_ALLOW_CREDENTIALS = True  # 쿠키 등 credential 정보 허용
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
