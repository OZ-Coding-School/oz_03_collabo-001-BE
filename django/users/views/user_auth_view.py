from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from django.conf import settings
from django.middleware import csrf


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE"]) or None
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token


class UserTokenVerifyView(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        # 쿠키에서 access 토큰 가져오기
        token = request.COOKIES.get("access_token")

        # 토큰이 없을 경우 400 Bad Request 반환
        if not token:
            return Response({"error": "Access token not found in cookies"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 토큰 검증
            AccessToken(token)
            return Response({"message": "Access token is valid"}, status=status.HTTP_200_OK)
        except (InvalidToken, TokenError):
            # 토큰이 유효하지 않을 경우 401 Unauthorized 반환
            return Response({"error": "Invalid access token"}, status=status.HTTP_401_UNAUTHORIZED)


class RefreshAccessTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # 쿠키에서 refresh 토큰 가져오기
        refresh_token = request.COOKIES.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token not found in cookies"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            response = Response({"message": "Access token refreshed successfully"}, status=status.HTTP_200_OK)

            # CSRF 토큰 설정
            csrf.get_token(request)

            # 새 access token 설정
            response.set_cookie(
                settings.SIMPLE_JWT["AUTH_COOKIE"],
                access_token,
                max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds(),
                httponly=True,
                samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                domain=".dogandbaby.co.kr",
                path="/",
            )

            # 새 refresh token 설정 (선택적)
            if settings.SIMPLE_JWT.get("ROTATE_REFRESH_TOKENS", False):
                new_refresh_token = str(refresh)
                response.set_cookie(
                    "refresh_token",
                    new_refresh_token,
                    max_age=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds(),
                    httponly=True,
                    samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
                    secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
                    domain=".dogandbaby.co.kr",
                    path="/",
                )

            return response

        except (InvalidToken, TokenError) as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)


# 로그인시 생기는 쿠키와 로그아웃시 삭제할 쿠키의 속성이 같아야함class SocialLogout(APIView):
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)

        # 쿠키 삭제 시 도메인, 경로 등의 설정을 일치시킴
        response.delete_cookie(
            settings.SIMPLE_JWT["AUTH_COOKIE"],
            domain='.dogandbaby.co.kr',
            path='/'
        )
        response.delete_cookie(
            "refresh_token",
            domain='.dogandbaby.co.kr',
            path='/'
        )
        return response