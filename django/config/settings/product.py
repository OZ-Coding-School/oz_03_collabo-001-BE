from .base import *

DEBUG = True

# 로드 밸런스 사용시 ip 더 추가

ALLOWED_HOSTS = [
    "api.dogandbaby.co.kr",
    "www.dogandbaby.co.kr",
    "dogandbaby.co.kr",
    "13.125.130.26",
    "localhost",
    "127.0.0.1",
]


CORS_ALLOWED_ORIGINS = [
    "https://api.dogandbaby.co.kr",
    "https://www.dogandbaby.co.kr",
    "https://dogandbaby.co.kr",
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    "https://api.dogandbaby.co.kr",
    "https://www.dogandbaby.co.kr",
    "https://dogandbaby.co.kr",
    "http://localhost",
    "http://127.0.0.1",
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True  # 쿠키 및 인증 헤더를 허용합니다.
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True  # HTTPS에서만 CSRF 쿠키 전송
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_DOMAIN = ".dogandbaby.co.kr"
CSRF_COOKIE_DOMAIN = ".dogandbaby.co.kr"

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
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
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


# AWS S3 설정
AWS_ACCESS_KEY_ID = os.getenv("AWS_S3_ACCESS_KEY_ID", "access_key")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_S3_SECRET_ACCESS_KEY", "secret_key")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_S3_STORAGE_BUCKET_NAME", "some_bucket_name")
AWS_S3_REGION_NAME = os.getenv("AWS_S3_S3_REGION_NAME", "ap-northeast-2")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"


# S3를 기본 파일 저장 위치로 설정
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# 업로드된 파일의 URL 형식 설정
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

# 미디어 파일이 저장될 폴더 경로 설정
MEDIAFILES_LOCATION = "media"
AWS_LOCATION = MEDIAFILES_LOCATION

# s3 storage 설정
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "authentication.custom_authentication.CustomJWTAuthentication",
    ],
}
