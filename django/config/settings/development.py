from .base import *

# 서비스 배포시 수정해야함.
SECRET_KEY = "django-insecure-g2$d_7hc#kw_^2%6sk4va_&xg1gsd#s8mgwwbi)r7+fkli4c^m"

# 서비스 배포시 False
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# 개발용 데이터베이스 설정
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db",
        "USER": "admin",
        "PASSWORD": "admin",
        "HOST": "db",
        "PORT": "5432",
    }
}
