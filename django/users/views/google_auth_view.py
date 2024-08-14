import requests
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


#구글 allauth에서 view를 받아서 기본 설정을 함
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/google/callback/"  # 프론트엔드 콜백 URL (개발 환경)
    client_class = OAuth2Client

#인가 코드를 받은 후 토큰 엔드포인트로 인가코드를 보내고 data를 보내서 액세스 토큰을 받는 코드
class exchange_code_for_token(APIView):
    def post(self, request):
        code = request.data.get("code")
        token_endpoint = "https://oauth2.googleapis.com/token"
        data = {
            "code": code, 
            "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
            "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            "redirect_uri": "http://localhost:8000/accounts/google/callback/",  # 실제 콜백 URL로 변경
            "grant_type": "authorization_code",
        }

        try:
            response = requests.post(token_endpoint, data=data)
            response.raise_for_status()  # 에러 발생 시 예외 처리

            token_data = response.json()
            access_token = token_data["access_token"]
            # 필요한 경우 id_token, refresh_token 등 다른 정보도 추출하여 사용

            return access_token

        except requests.exceptions.RequestException as e:
            # 에러 처리 (예: 로깅, 사용자에게 에러 메시지 표시 등)
            print(f"Error exchanging code for token: {e}")
            return None


User = get_user_model()

#엑세스 토큰을 받으면 유저인포 엔드포인트로 필요한 유저정보를 요청함
def get_user_info(access_token):
    userinfo_endpoint = "https://www.googleapis.com/oauth2/v3/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(userinfo_endpoint, headers=headers)
        response.raise_for_status()

        user_data = response.json()
        return user_data

    except requests.exceptions.RequestException as e:
        # 에러 처리
        print(f"Error getting user info: {e}")
        return None

#만약 유저가 없을 경우 유저를 이메일 값으로 만듬
def get_or_create_user(email, **extra_data):
    user, created = User.objects.get_or_create(email=email, defaults=extra_data)
    return user


User = get_user_model()

def get_user_info(access_token):
    userinfo_endpoint = "https://www.googleapis.com/oauth2/v3/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(userinfo_endpoint, headers=headers)
        response.raise_for_status()
        user_data = response.json()
        return user_data
    except requests.exceptions.RequestException as e:
        print(f"Error getting user info: {e}")
        return None

def get_or_create_user(email, **extra_data):
    user, created = User.objects.get_or_create(email=email, defaults=extra_data)
    return user

@csrf_exempt
def handle_google_callback(request):
    code = request.POST.get("authorizationCode")

    try:
        # 액세스 토큰 획득
        response = requests.post("http://localhost:8000/accounts/google/token/", data={"code": code})
        response.raise_for_status()
        token_data = response.json()
        access_token = token_data.get("access_token")

        if not access_token:
            raise ValueError("Failed to obtain access token")

        # 사용자 정보 가져오기 및 사용자 생성/업데이트
        user_info = get_user_info(access_token)
        if not user_info:
            raise ValueError("Failed to retrieve user info")

        user = get_or_create_user(user_info["email"], **user_info)

        # JWT 토큰 생성
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        refresh_token = str(refresh)

        # 응답 객체 생성
        response = JsonResponse(
            {
                "refresh": refresh_token,
                "access": access,
            }
        )

        # 쿠키에 리프레시 토큰 설정
        response.set_cookie(
            'refresh_token',
            refresh_token,
            httponly=True,
            secure=settings.SESSION_COOKIE_SECURE,
            max_age=6060247,
            samesite='Lax'
        )

        return response

    except Exception as e:
        print(f"Error handling Google callback: {e}")
        return JsonResponse(
            {"error": "An error occurred during Google authentication"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
