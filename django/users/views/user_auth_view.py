from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from users.serializers import EmptySerializer

from django.conf import settings


class UserTokenVerifyView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = EmptySerializer

    def post(self, request, *args, **kwargs):
        if getattr(self, "swagger_fake_view", False):
            return None  # Skip actual processing during schema generation

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


class RefreshAccessTokenView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = EmptySerializer

    def post(self, request, *args, **kwargs):
        if getattr(self, "swagger_fake_view", False):
            return None  # Skip actual processing during schema generation

        # 쿠키에서 refresh 토큰 가져오기
        refresh_token = request.COOKIES.get("refresh_token")

        # 리프레시 토큰이 없을 경우 400 Bad Request 반환
        if not refresh_token:
            return Response({"error": "Refresh token not found in cookies"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 리프레시 토큰 검증 및 새 액세스 토큰 생성
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            # 새 액세스 토큰을 쿠키에 설정
            response = Response({"message": "Access token refreshed successfully"}, status=status.HTTP_200_OK)
            response.set_cookie(
                "access_token",
                access_token,
                httponly=True,
                secure=settings.SESSION_COOKIE_SECURE,  # settings.py의 설정을 따름
                samesite="Lax",
                max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds(),
            )

            return response
        except TokenError:
            # 리프레시 토큰이 유효하지 않을 경우 401 Unauthorized 반환
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)
