from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import CommentImage, Place, RecommendedPlace
from .serializers import *
from common.serializers import *
from common.models import *


class AegaPlaceWholeView(APIView):

    @swagger_auto_schema(
        operation_summary="애개플레이스 전체 게시글 조회",
        operation_description=(
            "애개플레이스 전체 게시글을 조회합니다. \n"
            "place_region, place_subcategory에 따라 필터링할 수 있으며, 정렬할 수 있습니다. \n"
            "예시: place_region=1, place_subcategory=2, ordering=-created_at \n"
            "예시 URL: http://127.0.0.1:8000/places/?place_region=1&place_subcategory=2&ordering=-created_at \n"
        ),
        manual_parameters=[
            openapi.Parameter("place_region", openapi.IN_QUERY, description="지역 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter(
                "place_subcategory", openapi.IN_QUERY, description="장소 카테고리 필터링", type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                "ordering", openapi.IN_QUERY, description="정렬 (예: -created_at, rating 등)", type=openapi.TYPE_STRING
            ),
        ],
        responses={
            200: openapi.Response(
                "성공",
                PlaceSerializer(many=True),
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
        place_region_id = request.GET.get('place_region')
        place_subcategory_id = request.GET.get('place_subcategory')
        ordering = request.GET.get('ordering', '-created_at')
                
        page = request.GET.get('page', 1)  # 기본 페이지 번호 및 페이지 크기 설정
        page_size = request.GET.get('page_size', 10)  # 기본 페이지 크기를 10으로 설정

        

        queryset = Place.objects.all()

        print(queryset.count())


        if place_region_id:
            queryset = queryset.filter(place_region__id=place_region_id)
        
        if place_subcategory_id:
            queryset = queryset.filter(place_subcategory__id=place_subcategory_id)

        queryset = queryset.order_by(ordering)

        # 페이지네이션 적용
        paginator = PageNumberPagination()
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(queryset, request)

        serializer = PlaceSerializer(queryset, many=True)
        return paginator.get_paginated_response(serializer.data)



class AegaPlaceMainView(APIView):
    permission_classes = [IsAuthenticated]
    

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
                "main_category", openapi.IN_PATH, description="main, pet, kids", type=openapi.TYPE_STRING
            ),
        ],
        tags=["AegaPlace - 1 - mainpage"],
    )
    def get(self, request, *args, **kwargs):
        main_category = kwargs.get("main_category")

        if main_category == "main":
            main_category = "애개플레이스"
        elif main_category == "pet":
            main_category = "펫존"
        elif main_category == "kids":
            main_category = "키즈존"


        banner_obj = Banner.objects.filter(category__name=main_category, visible=True)
        banner_serializer = BannerSerializer(banner_obj, many=True)
        
        recommandedplace_obj = RecommendedPlace.objects.filter(category__name=main_category)
        recommandedplace_serializer = RecommendedPlaceSerializer(recommandedplace_obj, many=True)


        if main_category == "애개플레이스":
            new_places_obj = Place.objects.all().order_by("-created_at")[:6]
        elif main_category == "펫존":
            new_places_obj = Place.objects.filter(category="pet_zone").order_by("-created_at")[:6]
        elif main_category == "키즈존":
            new_places_obj = Place.objects.filter(category="kid_zone").order_by("-created_at")[:6]

        
        new_places_serializer = PlaceSerializer(new_places_obj, many=True)

        data = {
            "banners": banner_serializer.data,
            "recommandedplaces": recommandedplace_serializer.data,
            "new_places": new_places_serializer.data,
            "region_places": new_places_serializer.data,
            "subcategory": new_places_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)




class AegaPlaceBannerView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 배너 조회",
        operation_description="애개플레이스 배너 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


class AegaPlaceRecommendationView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 추천장소 조회",
        operation_description="애개플레이스 추천장소 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


class AegaPlaceView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 상세페이지 개별 조회",
        operation_description="애개플레이스 상세페이지 개별 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        # viewhistory 추가하기 (조회기록추가)
        pass


class AegaPlaceRegionView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 상세페이지 지역별 조회",
        operation_description="애개플레이스 상세페이지 지역별 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


class AegaPlaceSubcategoryView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 상세페이지 장소별 조회",
        operation_description="애개플레이스 상세페이지 장소별 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


class AegaPlaceCommentsView(APIView):
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
        pass

    @swagger_auto_schema(
        operation_summary="애개플레이스 게시물별 댓글 수정",
        operation_description="애개플레이스 게시물별 댓글 수정",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def put(self, request, *args, **kwargs):
        pass

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
        pass


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
        pass

    @swagger_auto_schema(
        operation_summary="애개플레이스 게시물별 댓글 등록",
        operation_description="애개플레이스 게시물별 댓글 등록",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def post(self, request, *args, **kwargs):
        pass


class AegaPlaceCommentImagesView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 개별 게시물의 전체 댓글의 이미지 조회",
        operation_description="애개플레이스 개별 게시물의 전체 댓글의 이미지 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


class AegaPlaceMainShareView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 정보 공유 링크",
        operation_description="조회중인 플레이스 url 링크 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


class AegaPlaceMainBookmarkView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 북마크",
        operation_description="조회중인 플레이스 북마크",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def post(self, request, *args, **kwargs):
        pass
