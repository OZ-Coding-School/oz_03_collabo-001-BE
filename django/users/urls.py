from django.urls import path

from .views.google_auth_view import (
    GoogleLogin,
    exchange_code_for_token,
    handle_google_callback,
)
from .views.mypage_views import MyProfileView
from .views import UpdateProfileImageView, UpdateProfileNameView

urlpatterns = [
    # Google 소셜 로그인 URL
    path("google/login/", GoogleLogin.as_view(), name="google_login"),  # Google OAuth2 로그인 시작
    path("google/callback/", handle_google_callback, name="google_callback"),  # Google OAuth2 콜백 URL
    path("google/token/", exchange_code_for_token.as_view(), name="google_token_exchange"),  # 인가 코드로 토큰 교환
    path("mypage/", MyProfileView.as_view(), name="mypage"),
    path("mypage/", UpdateProfileImageView.as_view(), name="mypage"),
    path("mypage/", UpdateProfileNameView.as_view(), name="mypage"),
]
