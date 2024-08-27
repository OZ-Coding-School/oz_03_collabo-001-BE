from common.models import *
from common.serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from geopy.distance import geodesic
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser, ViewHistory

from django.views.decorators.csrf import csrf_exempt

from .models import CommentImage, Place, PlaceSubcategory, RecommendedPlace
from .serializers import *


class AegaPlaceWholeView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="애개플레이스 전체 게시글 조회",
        operation_description=(
            "애개플레이스 전체 게시글을 조회합니다. \n"
            "place_region, place_subcategory에 따라 필터링할 수 있으며, 거리순으로 정렬할 수 있습니다. \n"
            "예시: place_region=1, place_subcategory=2, ordering=-created_at \n"
            "예시 URL: http://127.0.0.1:8000/places/?place_region=1&place_subcategory=2&ordering=-created_at \n"
            "또는 위도와 경도에 따라 장소를 거리순으로 정렬할 수 있습니다. \n"
            "예시: http://127.0.0.1:8000/places/?latitude=37.5665&longitude=126.9780"
        ),
        manual_parameters=[
            openapi.Parameter(
                "main_category",
                openapi.IN_QUERY,
                description="펫존, 키즈존 구분 없으면, 전부조회 / pet or kids or bd or (공백 or 랜덤문자)",
                type=openapi.TYPE_STRING,
            ),
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
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):

        main_category = request.GET.get("main_category")

        if main_category == "":
            main_category = "전체"
        elif main_category == "pet":
            main_category = "펫존"
        elif main_category == "kids":
            main_category = "키즈존"
        elif main_category == "bd":
            main_category = "애개플레이스"

        place_region_id = request.GET.get("place_region")
        place_subcategory_id = request.GET.get("place_subcategory")
        ordering = request.GET.get("ordering", "-created_at")
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")
        page = request.GET.get("page", 1)
        page_size = request.GET.get("page_size", 10)

        if main_category == "전체":
            queryset = Place.objects.all()
        elif main_category == "펫존":
            queryset = Place.objects.filter(category__in=["pet_zone", "bd_zone"])
        elif main_category == "키즈존":
            queryset = Place.objects.filter(category__in=["kid_zone", "bd_zone"])
        elif main_category == "애개플레이스":
            queryset = Place.objects.filter(category="bd_zone")
        else:
            queryset = Place.objects.all()
            
            
            

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


class AegaPlaceMainView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="애개플레이스 or 펫존 or 키즈존 조회",
        operation_description="애개플레이스 카테고리에 속하는 장소들의 상세 정보를 조회합니다. \n"
        "/places/main/main/ 애개플레이스 정보 조회\n"
        "/places/pet/main/ 펫존 정보 조회\n"
        "/places/kids/main/ 키즈존 정보 조회\n",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        manual_parameters=[
            openapi.Parameter(
                "main_category", openapi.IN_PATH, description="main, pet, kids, bd", type=openapi.TYPE_STRING
            ),
        ],
        tags=["AegaPlace - 1 - mainpage"],
    )
    def get(self, request, *args, **kwargs):
        main_category = kwargs.get("main_category")

        if main_category == "main":
            main_category = "전체"
        elif main_category == "pet":
            main_category = "펫존"
        elif main_category == "kids":
            main_category = "키즈존"
        elif main_category == "bd":
            main_category = "애개플레이스"

        if main_category == "전체":
            banner_obj = Banner.objects.filter(visible=True)
            recommandedplace_obj = RecommendedPlace.objects.all()
        else:
            banner_obj = Banner.objects.filter(category__name=main_category, visible=True)
            recommandedplace_obj = RecommendedPlace.objects.filter(category__name=main_category)

        banner_serializer = MainPageBannerSerializer(banner_obj, many=True)
        recommandedplace_serializer = MainPageRecommendedPlaceSerializer(
            recommandedplace_obj, many=True, context={"request": request}
        )
        
        if main_category == "애개플레이스":
            new_places_obj = Place.objects.filter(category="bd_zone").order_by("-created_at")[:6]
        elif main_category == "펫존":
            new_places_obj = Place.objects.filter(category__in=["pet_zone", "bd_zone"]).order_by("-created_at")[:6]
        elif main_category == "키즈존":
            new_places_obj = Place.objects.filter(category__in=["kid_zone", "bd_zone"]).order_by("-created_at")[:6]
        else:
            new_places_obj = Place.objects.all().order_by("-created_at")[:6]

        new_places_serializer = MainPagePlaceSerializer(new_places_obj, many=True, context={"request": request})

        place_subcategories = PlaceSubcategory.objects.all()
        place_regions = PlaceRegion.objects.all()

        subcategory_serializer = PlaceSubcategorySerializer(place_subcategories, many=True)
        region_serializer = PlaceRegionSerializer(place_regions, many=True)

        data = {
            "banners": banner_serializer.data,
            "recommandedplaces": recommandedplace_serializer.data,
            "new_places": new_places_serializer.data,
            "place_subcategories": subcategory_serializer.data,
            "region_places": new_places_serializer.data,
            "place_regions": region_serializer.data,
            "subcategory": new_places_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)


class AegaPlaceView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="애개플레이스 상세페이지 개별 조회",
        operation_description="애개플레이스 상세페이지 개별 조회",
        manual_parameters=[
            openapi.Parameter("place_pk", openapi.IN_PATH, description="Place ID", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        place_id = kwargs.get("place_pk")
        try:
            place = Place.objects.get(id=place_id)
        except Place.DoesNotExist:
            return Response({"detail": "Place not found"}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if user.is_authenticated:
            user = CustomUser.objects.get(id=request.user.id)
            ViewHistory.objects.create(user=user, place=place)

        serializer = AegaPlaceDetailSerializer(place, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AegaPlaceCommentsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="애개플레이스 게시물별 댓글 조회",
        operation_description="애개플레이스 게시물별 댓글 조회",
        responses={
            200: openapi.Response("성공", CommentsSerializer(many=True)),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        comment_id = kwargs.get("comment_pk")

        # 댓글 가져오기
        comments = Comments.objects.filter(id=comment_id)
        if not comments.exists():
            return Response({"detail": "No comments found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="애개플레이스 게시물별 댓글 수정",
        operation_description="애개플레이스 게시물별 댓글 수정",
        request_body=CommentsSerializer,  # 수정할 댓글 데이터를 받는 Serializer
        responses={
            200: openapi.Response("성공", CommentsSerializer),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def put(self, request, *args, **kwargs):
        comment_id = kwargs.get("comment_pk")

        try:
            comment = Comments.objects.get(id=comment_id)
        except Comments.DoesNotExist:
            return Response({"detail": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        # 유저 검사
        if comment.user != request.user:
            return Response({"detail": "자신의 후기만 수정할 수 있습니다."}, status=status.HTTP_403_FORBIDDEN)

        serializer = CommentsSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="애개플레이스 게시물별 댓글 삭제",
        operation_description="애개플레이스 게시물별 댓글 삭제",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def delete(self, request, *args, **kwargs):
        comment_id = kwargs.get("comment_pk")

        try:
            comment = Comments.objects.get(id=comment_id)
        except Comments.DoesNotExist:
            return Response({"detail": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

        # 유저 검사
        if comment.user != request.user:
            return Response({"detail": "자신의 후기만 삭제할 수 있습니다."}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response({"detail": "Comment deleted successfully"}, status=status.HTTP_200_OK)


class AegaPlaceCommentsAllView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 게시물별 댓글 조회",
        operation_description="애개플레이스 게시물별 댓글 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        place_id = kwargs.get("place_pk")

        try:
            place = Place.objects.get(id=place_id)
        except Place.DoesNotExist:
            return Response({"detail": "Place not found"}, status=status.HTTP_404_NOT_FOUND)

        comments = Comments.objects.filter(place=place)
        serializer = PlaceFullDetailCommentsSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="애개플레이스 게시물별 댓글 등록",
        operation_description="애개플레이스 게시물별 댓글 등록",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "content": openapi.Schema(type=openapi.TYPE_STRING, description="댓글 내용"),
                "rating": openapi.Schema(type=openapi.TYPE_INTEGER, description="평점"),
                "images": openapi.Schema(
                    type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING), description="이미지 리스트"
                ),
            },
            required=["content", "rating"],
        ),
        responses={
            201: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def post(self, request, *args, **kwargs):
        place_id = kwargs.get("place_pk")

        try:
            place = Place.objects.get(id=place_id)
        except Place.DoesNotExist:
            return Response({"detail": "Place not found"}, status=status.HTTP_404_NOT_FOUND)

        # Add the place and user to the data
        data = request.data.copy()

        data["user"] = request.user.id  # 사용자 ID를 명시적으로 사용

        # Pass the place into the context
        serializer = PlaceFullDetailCommentsSerializer(data=data, context={"place": place_id, "user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AegaPlaceCommentImagesView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 개별 게시물의 전체 댓글의 이미지 조회",
        operation_description="애개플레이스 개별 게시물의 전체 댓글의 이미지 조회",
        responses={
            200: openapi.Response("성공", CommentImageSerializer(many=True)),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        place_id = kwargs.get("place_pk")

        # 댓글 이미지 가져오기
        comment_images = CommentImage.objects.filter(comment__place_id=place_id)

        if not comment_images.exists():
            return Response({"detail": "No comment images found"}, status=status.HTTP_404_NOT_FOUND)

        # 시리얼라이저 사용
        serializer = CommentImageSerializer(comment_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AegaPlaceMainBookmarkView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="애개플레이스 북마크",
        operation_description="조회중인 플레이스 북마크",
        manual_parameters=[
            openapi.Parameter("place_pk", openapi.IN_PATH, description="Place ID", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        place_id = kwargs.get("place_pk")
        user = request.user

        try:
            place = Place.objects.get(id=place_id)
        except Place.DoesNotExist:
            return Response({"detail": "Place not found"}, status=404)

        # Toggle bookmark: if it exists, delete it; if it doesn't, create it
        bookmark, created = BookMark.objects.get_or_create(user=user, place=place)
        if not created:
            bookmark.delete()
            return Response({"detail": "Bookmark removed"}, status=200)
        else:
            return Response({"detail": "Bookmark added"}, status=200)
