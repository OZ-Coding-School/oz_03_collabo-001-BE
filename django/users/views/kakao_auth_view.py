import requests
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# 사용자 모델 가져오기
User = get_user_model()


# 카카오 OAuth2.0 관련 함수들
def exchange_code_for_token_kakao(code):
    token_endpoint = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.KAKAO_CLIENT_ID,
        "redirect_uri": "http://localhost:8000/auth/kakao/callback/",
        "code": code,
    }
    response = requests.post(token_endpoint, data=data)
    response.raise_for_status()
    token_data = response.json()
    return token_data["access_token"]


def get_user_info_kakao(access_token):
    userinfo_endpoint = "https://kapi.kakao.com/v2/user/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(userinfo_endpoint, headers=headers)
    response.raise_for_status()
    user_data = response.json()
    return user_data


def handle_kakao_callback(request):
    code = request.GET.get("code")
    try:
        access_token = exchange_code_for_token_kakao(code)
        user_info = get_user_info_kakao(access_token)
        user, _ = User.objects.get_or_create(
            email=user_info["kakao_account"]["email"], defaults={"nickname": user_info["properties"]["nickname"]}
        )
        refresh = RefreshToken.for_user(user)
        return JsonResponse({"refresh": str(refresh), "access": str(refresh.access_token)})

    except Exception as e:
        print(f"Error handling Kakao callback: {e}")
        return JsonResponse(
            {"error": "An error occurred during Kakao authentication"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
