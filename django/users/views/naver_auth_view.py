import os
import requests
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse

User = get_user_model()

# 네이버 소셜로그인
class NaverExchangeCodeForToken(APIView):
    def post(self, request):
        code = request.data.get("code")
        state = request.data.get("state")  # 네이버 로그인은 state 파라미터를 사용합니다
        token_endpoint = "https://nid.naver.com/oauth2.0/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": os.environ.get("NAVER_CLIENT_ID"),
            "client_secret": os.environ.get("NAVER_CLIENT_SECRET"),
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

            # 액세스 토큰을 통해 유저정보를 요청하는 코드
            userinfo_endpoint = "https://openapi.naver.com/v1/nid/me"
            headers = {"Authorization": f"Bearer {access_token}"}
            user_info_response = requests.get(userinfo_endpoint, headers=headers)
            user_info_response.raise_for_status()
            user_info = user_info_response.json()

            # user모델에서 필요한 정보 가져오는 코드
            email = user_info.get("response", {}).get("email")
            if not email:
                return JsonResponse({"error": "Email not found in user info"}, status=400)

            user_data = {
                "email": email,
                "profile_image": user_info.get("response", {}).get("profile_image"),
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