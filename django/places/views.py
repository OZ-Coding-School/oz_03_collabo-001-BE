from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CommentImage, Place, RecommendedPlace


class AegaPlaceWholeView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 전체 조회",
        operation_description="애개플레이스 전체 조회",
        responses={
            200: openapi.Response("성공"),
            400: "잘못된 요청",
        },
        tags=["AegaPlace"],
    )
    def get(self, request, *args, **kwargs):
        pass


class AegaPlaceMainView(APIView):
    @swagger_auto_schema(
        operation_summary="애개플레이스 정보 조회",
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
