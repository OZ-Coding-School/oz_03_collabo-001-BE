import os

import requests
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response

User = get_user_model()


# 구글 소셜로그인
class GoogleExchangeCodeForToken(APIView):
    # 인가코드를 엔드포인트로 정보 담아서 보내는 코드
    def post(self, request):
        code = request.data.get("code")
        token_endpoint = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": os.environ.get("GOOGLE_OAUTH2_CLIENT_ID"),
            "client_secret": os.environ.get("GOOGLE_OAUTH2_CLIENT_SECRET"),
            "redirect_uri": "http://localhost:5173",
            "grant_type": "authorization_code",
        }

        # 엑세스 토큰을 받는 코드
        try:
            response = requests.post(token_endpoint, data=data)
            response.raise_for_status()
            token_data = response.json()
            access_token = token_data.get("access_token")

            if not access_token:
                return JsonResponse({"error": "Failed to obtain access token"}, status=400)

            # 액세스토큰을 통해 유저정보를 요청하는 코드
            userinfo_endpoint = "https://www.googleapis.com/oauth2/v3/userinfo"
            headers = {"Authorization": f"Bearer {access_token}"}
            user_info_response = requests.get(userinfo_endpoint, headers=headers)
            user_info_response.raise_for_status()
            user_info = user_info_response.json()

            # user모델에서 필요한 정보 가져오는 코드
            email = user_info.get("email")
            if not email:
                return JsonResponse({"error": "Email not found in user info"}, status=400)

            user_data = {
                "email": email,
                "profile_image": user_info.get("picture"),
            }

            # 유저 정보 생성
            user, created = User.objects.get_or_create(email=email, defaults=user_data)

            # jwt 토큰 생성
            refresh = RefreshToken.for_user(user)
            response_data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            # jwt토큰을 json형태로 쿠키에 전달하는 코드
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
            # Handle token exchange or user info retrieval errors
            return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)


class GoogleSocialLogout(APIView):
    # 로그아웃 - 쿠키에서 토큰을 삭제하는 코드
    def post(self, request):
        response = JsonResponse({"message": "Successfully logged out"})

        # 쿠키에서 'refresh_token'과 'access_token'을 삭제합니다.
        response.delete_cookie("refresh_token")
        response.delete_cookie("access_token")

        return response
    
