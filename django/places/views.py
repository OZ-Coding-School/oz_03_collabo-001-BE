from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CommentImage, Place, RecommendedPlace
from .serializers import *


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
        pass


class AegaPlaceMainView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 or 펫존 or 키즈존 조회",
        operation_description="애개플레이스 카테고리에 속하는 장소들의 상세 정보를 조회합니다.",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


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
