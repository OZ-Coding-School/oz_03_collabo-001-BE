import os

import requests
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.utils import generate_random_nickname

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()


class NaverExchangeCodeForToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        code = request.data.get("code")
        state = request.data.get("state")
        token_endpoint = "https://nid.naver.com/oauth2.0/token"

        data = {
            "grant_type": "authorization_code",  # 혹은 필요한 값을 사용
            "client_id": os.getenv("NAVER_CLIENT_ID"),  # Google 예제
            "client_secret": os.getenv("NAVER_CLIENT_SECRET"),  # Google 예제
            "code": code,
            "state": state,
        }

        try:
            response = requests.post(token_endpoint, data=data)
            response.raise_for_status()
            token_data = response.json()
            access_token = token_data.get("access_token")

            if not access_token:
                return JsonResponse({"error": "Failed to obtain access token"}, status=400)

            userinfo_endpoint = "https://openapi.naver.com/v1/nid/me"
            headers = {"Authorization": f"Bearer {access_token}"}
            user_info_response = requests.get(userinfo_endpoint, headers=headers)
            user_info_response.raise_for_status()
            user_info = user_info_response.json().get("response", {})

            email = user_info.get("email")
            if not email:
                return JsonResponse({"error": "Email not found in user info"}, status=400)

            user_data = {
                "email": email,
                "profile_image": user_info.get("profile_image"),
                "nickname": generate_random_nickname(),
            }
            user, created = User.objects.get_or_create(email=email, defaults=user_data)
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
                samesite="Lax",
            )
            response.set_cookie(
                "access_token",
                str(refresh.access_token),
                domain=".dogandbaby.co.kr",
                httponly=True,
                secure=settings.SESSION_COOKIE_SECURE,
                max_age=6060247,
                samesite="Lax",
            )

            return response

        except Exception as e:
            # Handle token exchange or user info retrieval errors
            return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)
