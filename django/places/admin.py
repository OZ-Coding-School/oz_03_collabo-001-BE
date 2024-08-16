from django.contrib import admin

from .models import (
    CommentImage,
    Comments,
    Place,
    PlaceImage,
    PlaceRegion,
    PlaceSubcategory,
    RecommendedPlace,
    ServicesIcon,
)


# 기본 Admin 클래스 커스터마이징
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "category", "rating", "user")
    search_fields = ("name", "address", "category")
    list_filter = ("category", "rating")
    ordering = ("name",)


class RecommendedPlaceAdmin(admin.ModelAdmin):
    list_display = ("place", "tags", "created_at", "updated_at")
    search_fields = ("place__name", "tags")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)


class ServicesIconAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    search_fields = ("name",)
    ordering = ("name",)


class PlaceRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "region")


class PlaceSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "subcategory")


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user", "place", "rating", "created_at")
    search_fields = ("user__nickname", "place__name", "content")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)


class CommentImageAdmin(admin.ModelAdmin):
    list_display = ("comment", "image")
    search_fields = ("comment__content",)
    ordering = ("comment",)


# 모델을 Admin 사이트에 등록
admin.site.register(Place, PlaceAdmin)
admin.site.register(RecommendedPlace, RecommendedPlaceAdmin)
admin.site.register(ServicesIcon, ServicesIconAdmin)
admin.site.register(PlaceRegion, PlaceRegionAdmin)
admin.site.register(PlaceSubcategory, PlaceSubcategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(CommentImage, CommentImageAdmin)
admin.site.register(PlaceImage)
