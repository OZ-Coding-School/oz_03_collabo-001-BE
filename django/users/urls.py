from django.urls import path

from .views.google_auth_view import GoogleExchangeCodeForToken, GoogleSocialLogout
from .views.kakao_auth_view import KakaoExchangeCodeForToken
from .views.mypage_views import (
    MyProfileView,
    UpdateProfileImageView,
    UpdateProfileNameView,
)
from .views.naver_auth_view import NaverExchangeCodeForToken
from .views.user_auth_view import RefreshAccessTokenView, UserTokenVerifyView

urlpatterns = [
    # google social
    path("google/login/callback/", GoogleExchangeCodeForToken.as_view(), name="google_callback"),
    path("google/logout/", GoogleSocialLogout.as_view(), name="google-logout"),
    # naver social
    path("naver/login/callback/", NaverExchangeCodeForToken.as_view(), name="naver_callback"),
    # kakao social
    path("kakao/login/callback/", KakaoExchangeCodeForToken.as_view(), name="kakao_callback"),
    # user_auth
    path("token/verify/", UserTokenVerifyView.as_view(), name="token-verify"),
    path("token/refresh/", RefreshAccessTokenView.as_view(), name="token_refresh"),
    # mypage
    path("mypage/", MyProfileView.as_view(), name="mypage"),
    path("mypage/update-image/", UpdateProfileImageView.as_view(), name="mypage_update_profile_images"),
    path("mypage/update-name/", UpdateProfileNameView.as_view(), name="mypage_update_profile_names"),
]
