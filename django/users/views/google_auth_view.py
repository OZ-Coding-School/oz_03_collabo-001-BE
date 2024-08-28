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


# 구글 소셜로그인
class GoogleExchangeCodeForToken(APIView):
    permission_classes = [AllowAny]

    # 인가코드를 엔드포인트로 정보 담아서 보내는 코드
    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        print(code)
        print("여기냐")
        token_endpoint = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "redirect_uri": os.getenv("GOOGLE_REDIRECT_URI"),
            "grant_type": "authorization_code",
        }
        print(data)
        # 엑세스 토큰을 받는 코드
        try:
            response = requests.post(token_endpoint, data=data, headers={"Accept": "application/x-www-form-urlencoded"})
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
                "nickname": generate_random_nickname(),
            }
            # 유저 정보 생성
            user, created = User.objects.get_or_create(email=email, defaults=user_data)

            # jwt 토큰 생성
            refresh = RefreshToken.for_user(user)
            print("refresh\n :", str(refresh))
            # 쿠키에 토큰 저장 (세션 쿠키로 설정)
            # response = HttpResponseRedirect("https://dogandbaby.co.kr")  # 로그인 완료 시 리디렉션할 URL
            # # response = HttpResponseRedirect('http://localhost:8000/api/v1/users/myinfo')

            # # 배포 환경에서만 secure=True와 samesite='None' 설정
            # response.set_cookie("access_token", str(refresh.access_token), domain=".dogandbaby.co.kr", path="/")
            # response.set_cookie("refresh_token", str(refresh), domain=".dogandbaby.co.kr", path="/")

            # return response

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
