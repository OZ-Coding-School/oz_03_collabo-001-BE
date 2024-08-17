from django.urls import path

from .views.google_auth_view import ExchangeCodeForToken
from .views.mypage_views import MyProfileView

urlpatterns = [
    path("google/login/callback/", ExchangeCodeForToken.as_view, name="google_callback"),  # 인가 코드로 토큰 교환
    path("mypage/", MyProfileView.as_view(), name="mypage"),
]
