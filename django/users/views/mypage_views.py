from common.models import Banner
from drf_yasg.utils import swagger_auto_schema
from places.models import Comments
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import BookMark, CustomUser, ViewHistory

from ..serializers import (
    BannerSerializer,
    BookMarkSerializer,
    CommentsSerializer,
    UserProfileSerializer,
    ViewHistorySerializer,
)


class MyProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema()
    def get(self, request):
        # user = request.user
        user = CustomUser.objects.get(id=1)
        profile_serializer = UserProfileSerializer(user)

        # Get recent 3 bookmarks
        bookmarks = BookMark.objects.filter(user=user).order_by("-created_at")[:3]
        bookmark_serializer = BookMarkSerializer(bookmarks, many=True)

        # Get recent 3 view histories
        view_histories = ViewHistory.objects.filter(user=user).order_by("-created_at")[:3]
        view_history_serializer = ViewHistorySerializer(view_histories, many=True)

        # Get recent 2 comments from all users
        recent_comments = Comments.objects.all().order_by("-created_at")[:2]
        comments_serializer = CommentsSerializer(recent_comments, many=True)

        # Get banners
        banners = Banner.objects.filter(category__name="마이페이지", visible=True)
        banner_serializer = BannerSerializer(banners, many=True)

        data = {
            "profile": profile_serializer.data,
            "recent_bookmarks": bookmark_serializer.data,
            "recent_view_histories": view_history_serializer.data,
            "recent_comments": comments_serializer.data,
            "banners": banner_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)
