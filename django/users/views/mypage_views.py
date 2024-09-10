from common.models import Banner
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from geopy.distance import geodesic
from places.models import Comments, Place, PlaceRegion
from places.serializers import (
    MainPagePlaceSerializer,
    PlaceRegionSerializer,
    PlaceSubcategory,
    PlaceSubcategorySerializer,
)
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, MultiPartParser
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
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["MyPage"],
    )
    def get(self, request):
        # 액세스 토큰을 쿠키에서 가져오기
        token = request.COOKIES.get("access_token")

        # 토큰이 없을 경우
        if not token:
            logger.warning("Access token not found in cookies")

        # 로그에 토큰 정보 남기기 (주의: 민감한 정보를 로그에 남기는 것은 보안에 위험할 수 있습니다)
        # logger.debug(f"Access token: {token}")

        user = request.user
        profile_serializer = UserProfileSerializer(user, context={"request": request})

        # 내 최근 북마크 3건 조회
        recent_bookmarks = BookMark.objects.filter(user=user).order_by("-created_at")[:3]
        recent_places = [bookmark.place for bookmark in recent_bookmarks]
        recent_bookmarks_serializer = MainPagePlaceSerializer(recent_places, many=True, context={"request": request})

        # ViewHistory를 통해 최근 본 장소 목록 가져오기
        view_history_objects = ViewHistory.objects.filter(user=user).order_by("-updated_at")[:3]

        # ViewHistory에서 Place 객체만 추출
        places = [vh.place for vh in view_history_objects]
        history_places_serializer = MainPagePlaceSerializer(places, many=True, context={"request": request})

        # Get recent 2 comments from all users
        recent_comments = Comments.objects.filter(user=user).order_by("-created_at")[:2]
        comments_serializer = CommentsSerializer(recent_comments, many=True, context={"request": request})

        # Get banners
        banners = Banner.objects.filter(category__name="마이페이지", visible=True)
        banner_serializer = BannerSerializer(banners, many=True, context={"request": request})

        data = {
            "profile": profile_serializer.data,
            "recent_bookmarks": recent_bookmarks_serializer.data,
            "recent_view_histories": history_places_serializer.data,
            "recent_comments": comments_serializer.data,
            "banners": banner_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)


import logging

logger = logging.getLogger(__name__)


class UpdateProfileImageView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_summary="Update Profile Image",
        operation_description="Update the user's profile image.",
        manual_parameters=[
            openapi.Parameter(
                "profile_image",
                openapi.IN_FORM,
                description="Profile image file",
                type=openapi.TYPE_FILE,
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                "성공",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(type=openapi.TYPE_STRING, description="Response message"),
                    },
                ),
            ),
            400: "잘못된 요청",
        },
        tags=["MyPage"],
    )
    def post(self, request):
        user = request.user
        profile_image = request.FILES.get("profile_image")

        if not profile_image:
            raise ValidationError("No profile image provided.")

        user.profile_image = profile_image
        user.save()

        image_url = request.build_absolute_uri(user.profile_image.url)

        return Response(
            {"message": "Profile image updated successfully.", "image_url": image_url}, status=status.HTTP_200_OK
        )


class UpdateProfileNameView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Update Profile Name",
        manual_parameters=[
            openapi.Parameter(
                "name", openapi.IN_QUERY, description="New name for the user", type=openapi.TYPE_STRING, required=True
            ),
        ],
        responses={
            200: openapi.Response(
                "Success",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(type=openapi.TYPE_STRING, description="Response message"),
                    },
                ),
            ),
            212: openapi.Response(
                "Duplicate nickname",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(type=openapi.TYPE_STRING, description="Response message"),
                    },
                ),
            ),
            210: openapi.Response(
                "Empty nickname",
                openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "message": openapi.Schema(type=openapi.TYPE_STRING, description="Response message"),
                    },
                ),
            ),
            400: "Bad request",
        },
        tags=["MyPage"],
    )
    def post(self, request):
        user = request.user
        new_name = request.query_params.get("name")

        if not new_name or not new_name.strip():
            return Response({"message": "Nickname cannot be empty or contain only spaces."}, status=210)

        # Strip leading and trailing whitespaces
        new_name = new_name.strip()

        # Check if the new nickname already exists
        if CustomUser.objects.filter(nickname=new_name).exists():
            return Response({"message": "Nickname already exists."}, status=212)

        user.nickname = new_name
        user.save()

        return Response({"message": "Name updated successfully."}, status=status.HTTP_200_OK)


class MyBookmarksView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="사용자가 북마크한 전체 게시글 조회",
        operation_description=(
            "사용자가 북마크한 전체 게시글을 조회합니다. \n"
            "place_region, place_subcategory에 따라 필터링할 수 있으며, 거리순으로 정렬할 수 있습니다. \n"
            "예시: place_region=1, place_subcategory=2, ordering=-created_at \n"
            "예시 URL: http://127.0.0.1:8000/places/?place_region=1&place_subcategory=2&ordering=-created_at \n"
            "또는 위도와 경도에 따라 장소를 거리순으로 정렬할 수 있습니다. \n"
            "예시: http://127.0.0.1:8000/places/?latitude=37.5665&longitude=126.9780"
        ),
        manual_parameters=[
            openapi.Parameter("place_region", openapi.IN_QUERY, description="지역 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                "place_subcategory", openapi.IN_QUERY, description="장소 카테고리 필터링", type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter("page", openapi.IN_QUERY, description="페이지 번호", type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                "page_size", openapi.IN_QUERY, description="한번에 조회할 수 기본값:10", type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter("latitude", openapi.IN_QUERY, description="현재 위치의 위도", type=openapi.TYPE_NUMBER),
            openapi.Parameter("longitude", openapi.IN_QUERY, description="현재 위치의 경도", type=openapi.TYPE_NUMBER),
            openapi.Parameter(
                "is_active",
                openapi.IN_QUERY,
                description="거리순 정렬 활성 상태 필터 (True/False)",
                type=openapi.TYPE_BOOLEAN,
            ),
        ],
        responses={
            200: openapi.Response(
                "성공",
                MainPagePlaceSerializer(many=True),
                examples={
                    "application/json": [
                        {
                            "name": "My Place 1",
                            "address": "123 Example Street",
                            "rating": 4,
                            "description": "A lovely place for your pets.",
                            "price_text": "20,000 KRW",
                            "service_icons": ["Icon 1", "Icon 2"],
                            "place_images": [
                                "http://example.com/media/place_images/1.jpg",
                                "http://example.com/media/place_images/2.jpg",
                            ],
                            "comments": [
                                {
                                    "comment_content": "Great place!",
                                    "comment_images": ["http://example.com/media/comment_images/1.jpg"],
                                    "comment_rating": 5,
                                }
                            ],
                        }
                    ]
                },
            ),
            400: "잘못된 요청",
        },
        tags=["MyPage"],
    )
    def get(self, request, *args, **kwargs):
        user = request.user
        place_region_id = request.GET.get("place_region")
        place_subcategory_id = request.GET.get("place_subcategory")
        ordering = request.GET.get("ordering", "-created_at")
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")
        page = request.GET.get("page", 1)
        page_size = request.GET.get("page_size", 10)

        bookmark_places_ids = BookMark.objects.filter(user=user).values_list("place_id", flat=True)
        queryset = Place.objects.filter(id__in=bookmark_places_ids)

        if place_region_id:
            queryset = queryset.filter(place_region__id=place_region_id)

        if place_subcategory_id:
            queryset = queryset.filter(place_subcategory__id=place_subcategory_id)

        if latitude and longitude:
            try:
                user_location = (float(latitude), float(longitude))
                places_with_distance = []
                for place in queryset:
                    place_location = (place.latitude, place.longitude)
                    distance = geodesic(place_location, user_location).meters
                    places_with_distance.append((place, distance))

                # 거리순으로 정렬
                places_with_distance.sort(key=lambda x: x[1])
                queryset = [place for place, distance in places_with_distance]
            except ValueError:
                return Response({"error": "Invalid latitude or longitude format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = queryset.order_by(ordering)

        paginator = PageNumberPagination()
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(queryset, request)

        place_serializer = MainPagePlaceSerializer(result_page, many=True, context={"request": request})

        place_subcategories = PlaceSubcategory.objects.all()
        place_regions = PlaceRegion.objects.all()

        subcategory_serializer = PlaceSubcategorySerializer(place_subcategories, many=True)
        region_serializer = PlaceRegionSerializer(place_regions, many=True)

        response_data = {
            "place_subcategories": subcategory_serializer.data,
            "place_regions": region_serializer.data,
            "results": place_serializer.data,
        }

        return paginator.get_paginated_response(response_data)


class ViewHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get All ViewHistory",
        tags=["MyPage"],
    )
    def get(self, request):
        user = request.user
        viewHistory = ViewHistory.objects.filter(user=user).order_by("-created_at")
        viewHistorySerializer = ViewHistorySerializer(viewHistory, many=True, context={"request": request})

        return Response(viewHistorySerializer.data, status=status.HTTP_200_OK)


class MycommentView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get All MyComment",
        tags=["MyPage"],
    )
    def get(self, request):
        user = request.user
        mycomment = Comments.objects.filter(user=user).order_by("-created_at")
        comments_serializer = CommentsSerializer(mycomment, many=True, context={"request": request})

        return Response(comments_serializer.data, status=status.HTTP_200_OK)
