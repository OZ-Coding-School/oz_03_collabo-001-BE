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


# 카카오 소셜 로그인
class KakaoExchangeCodeForToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        code = request.data.get("code")
        token_endpoint = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": "YOUR_KAKAO_CLIENT_ID",
            "redirect_uri": "YOUR_KAKAO_REDIRECT_URI",
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

            email = user_info.get("kakao_account", {}).get("email")
            if not email:
                return JsonResponse({"error": "Email not found in user info"}, status=400)

            user_data = {
                "email": email,
                "profile_image": user_info.get("properties", {}).get("profile_image"),
                "nickname": generate_random_nickname(),
            }
            user, created = User.objects.get_or_create(email=email, defaults=user_data)

            refresh = RefreshToken.for_user(user)
            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            response = JsonResponse(response_data)
            response.set_cookie(
                "refresh_token",
                str(refresh),
                httponly=True,
                secure=settings.SESSION_COOKIE_SECURE,
                max_age=6060247,
                samesite="Lax",
            )
            response.set_cookie(
                "access_token",
                str(refresh.access_token),
                httponly=True,
                secure=settings.SESSION_COOKIE_SECURE,
                max_age=6060247,
                samesite="Lax",
            )

            return response

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)


class KakaoSocialLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie("refresh_token")
        response.delete_cookie("access_token")
        return response
