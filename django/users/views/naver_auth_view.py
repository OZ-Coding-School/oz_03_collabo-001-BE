import requests
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# 사용자 모델 가져오기
User = get_user_model()


# 네이버 OAuth2.0 관련 함수들
def exchange_code_for_token_naver(code):
    token_endpoint = "https://nid.naver.com/oauth2.0/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.NAVER_CLIENT_ID,
        "client_secret": settings.NAVER_CLIENT_SECRET,
        "redirect_uri": "http://localhost:8000/auth/naver/callback/",
        "code": code,
        "state": "random_state_string",  # 실제 애플리케이션에서는 랜덤한 상태 값을 생성하여 검증하는 것이 좋습니다
    }
    response = requests.post(token_endpoint, data=data)
    response.raise_for_status()
    token_data = response.json()
    return token_data["access_token"]


def get_user_info_naver(access_token):
    userinfo_endpoint = "https://openapi.naver.com/v1/nid/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(userinfo_endpoint, headers=headers)
    response.raise_for_status()
    user_data = response.json()
    return user_data


def handle_naver_callback(request):
    code = request.GET.get("code")
    try:
        access_token = exchange_code_for_token_naver(code)
        user_info = get_user_info_naver(access_token)
        user, _ = User.objects.get_or_create(
            email=user_info["response"]["email"], defaults={"nickname": user_info["response"]["nickname"]}
        )
        refresh = RefreshToken.for_user(user)
        return JsonResponse({"refresh": str(refresh), "access": str(refresh.access_token)})

    except Exception as e:
        print(f"Error handling Naver callback: {e}")
        return JsonResponse(
            {"error": "An error occurred during Naver authentication"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
