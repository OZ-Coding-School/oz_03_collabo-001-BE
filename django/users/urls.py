from django.urls import path
from .views.google_auth_view import handle_google_callback, GoogleLogin, exchange_code_for_token

urlpatterns = [
    # Google 소셜 로그인 URL
    # path('google/login/', GoogleLogin.as_view(), name='google_login'),
    
    # Google OAuth2 콜백 URL
    path('google/callback/', handle_google_callback, name='google_callback'),
    path('google/login/', exchange_code_for_token.as_view(), name='google_login'),

]
