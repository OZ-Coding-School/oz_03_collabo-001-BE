from django.urls import path

from rest_framework_simplejwt.views import TokenVerifyView

from .views.google_auth_view import GoogleExchangeCodeForToken, GoogleSocialLogout
from .views.kakao_auth_view import KakaoExchangeCodeForToken
from .views.mypage_views import (
    MyProfileView,
    UpdateProfileImageView,
    UpdateProfileNameView,
)
from .views.naver_auth_view import NaverExchangeCodeForToken

urlpatterns = [
    #google social
    path("google/login/callback/", GoogleExchangeCodeForToken.as_view(), name="google_callback"),  # 구글 로그인
    path('google/logout/', GoogleSocialLogout.as_view(), name='google-logout'),    
    #naver social
    path("naver/login/callback/", NaverExchangeCodeForToken.as_view(), name="naver_callback"),  # 네이버 로그인
    #kakao social
    path("kakao/login/callback/", KakaoExchangeCodeForToken.as_view(), name="kakao_callback"),  # 카카오 로그인
    #토큰 유효성 검사 엔드포인트
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),    
    path("mypage/", MyProfileView.as_view(), name="mypage"),
    path("mypage/update-image/", UpdateProfileImageView.as_view(), name="mypage_update_profile_images"),
    path("mypage/update-name/", UpdateProfileNameView.as_view(), name="mypage_update_profile_names"),
]
