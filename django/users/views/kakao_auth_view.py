import os

import requests
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.utils import generate_random_nickname

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()


# 카카오 소셜 로그인
class KakaoExchangeCodeForToken(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        code = request.data.get("code")
        token_endpoint = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": os.getenv("KAKAO_CLIENT_ID"),  # Kakao 예제
            "redirect_uri": os.getenv("KAKAO_REDIRECT_URI"),  # Kakao 예제, 환경 변수 사용
            "code": code,
        }

        try:
            response = requests.post(token_endpoint, data=data)
            response.raise_for_status()
            token_data = response.json()
            access_token = token_data.get("access_token")

            if not access_token:
                return JsonResponse({"error": "Failed to obtain access token"}, status=400)

            userinfo_endpoint = "https://kapi.kakao.com/v2/user/me"
            headers = {"Authorization": f"Bearer {access_token}"}
            user_info_response = requests.get(userinfo_endpoint, headers=headers)
            user_info_response.raise_for_status()
            user_info = user_info_response.json()

            nickname = user_info.get("properties", {}).get("nickname")
            if not nickname:
                return JsonResponse({"error": "Nickname not found in user info"}, status=400)

            # 고유한 식별자로 카카오 ID를 사용
            kakao_id = str(user_info.get("id"))
            if not kakao_id:
                return JsonResponse({"error": "Kakao ID not found"}, status=400)

            user_data = {
                "email": f"kakao_{kakao_id}@kakao.com",  # 고유한 이메일 생성
                "nickname": nickname,
                "profile_image": user_info.get("properties", {}).get("profile_image"),
            }

            # `email`을 사용자 식별자로 사용하여 사용자 생성 또는 가져오기
            user, created = User.objects.get_or_create(email=user_data["email"], defaults=user_data)

            # jwt 토큰 생성
            refresh = RefreshToken.for_user(user)
            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            response = JsonResponse(response_data)
            response.set_cookie(
                "refresh_token",
                str(refresh),
                domain=".dogandbaby.co.kr",
                httponly=True,
                secure=settings.SESSION_COOKIE_SECURE,
                max_age=6060247,
                samesite="Strict",
            )
            response.set_cookie(
                "access_token",
                str(refresh.access_token),
                domain=".dogandbaby.co.kr",
                httponly=True,
                secure=settings.SESSION_COOKIE_SECURE,
                max_age=6060247,
                samesite="Strict",
            )

            return response

        except Exception as e:
            # Handle token exchange or user info retrieval errors
            return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)
