import requests
from django.conf import settings
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views import View

class GoogleAuthView(View):
    def get(self, request, *args, **kwargs):
        # 구글 OAuth2 인증 요청을 위한 URL 생성
        google_auth_url = (
            f"https://accounts.google.com/o/oauth2/auth"
            f"?response_type=code"
            f"&client_id={settings.GOOGLE_CLIENT_ID}"
            f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
            f"&scope=email profile"
            f"&access_type=offline"
            f"&prompt=consent"
        )
        return redirect(google_auth_url)

class GoogleCallbackView(View):
    def get(self, request, *args, **kwargs):
        # 구글 인증 콜백에서 코드 얻기
        code = request.GET.get('code')
        if not code:
            return JsonResponse({'error': 'No code provided'}, status=400)

        # 구글 토큰 요청
        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': settings.GOOGLE_REDIRECT_URI,
            'grant_type': 'authorization_code'
        }
        token_r = requests.post(token_url, data=token_data)
        token_info = token_r.json()

        # 액세스 토큰으로 사용자 정보 요청
        access_token = token_info.get('access_token')
        user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
        user_info_params = {
            'access_token': access_token
        }
        user_info_r = requests.get(user_info_url, params=user_info_params)
        user_info = user_info_r.json()

        # 사용자 정보 반환 (또는 추가적인 처리)
        return JsonResponse(user_info)
