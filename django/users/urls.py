# users/urls.py

from django.urls import path

# from .views.google_auth_view import GoogleAuthView, GoogleCallbackView
from .views.mypage_views import MyProfileView

urlpatterns = [
    # path("google/", GoogleAuthView.as_view(), name="google_login"),
    # path("google/callback/", GoogleCallbackView.as_view(), name="google_callback"),
    path("mypage/", MyProfileView.as_view(), name="mypage"),
]
