from django.urls import path

from .views.google_auth_view import GoogleExchangeCodeForToken
from .views.kakao_auth_view import KakaoExchangeCodeForToken
from .views.mypage_views import (
    MyBookmarksView,
    MycommentView,
    MyProfileView,
    UpdateProfileImageView,
    UpdateProfileNameView,
    ViewHistoryView,
)
from .views.naver_auth_view import NaverExchangeCodeForToken

urlpatterns = [
    path("google/login/callback/", GoogleExchangeCodeForToken.as_view(), name="google_callback"),  # 구글 로그인
    path("naver/login/callback/", NaverExchangeCodeForToken.as_view(), name="naver_callback"),  # 네이버 로그인
    path("kakao/login/callback/", KakaoExchangeCodeForToken.as_view(), name="kakao_callback"),  # 카카오 로그인
    path("mypage/", MyProfileView.as_view(), name="mypage"),
    path("profile/", MyProfileView.as_view(), name="my-profile"),
    path("mypage/update-image/", UpdateProfileImageView.as_view(), name="mypage_update_profile_images"),
    path("mypage/update-name/", UpdateProfileNameView.as_view(), name="mypage_update_profile_names"),
    path("mypage/bookmark/", MyBookmarksView.as_view(), name="mypage_bookmark"),
    path("mypage/view-history/", ViewHistoryView.as_view(), name="mypage_view_history"),
    path("mypage/my-comment/", MycommentView.as_view(), name="mypage_my_comment"),
]
