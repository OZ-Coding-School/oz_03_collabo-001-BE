# users/urls.py

from django.urls import path
from .views.google_auth_view import GoogleAuthView, GoogleCallbackView

urlpatterns = [
    path('google/', GoogleAuthView.as_view(), name='google_login'),
    path('google/callback/', GoogleCallbackView.as_view(), name='google_callback'),
]
