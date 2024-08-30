from django.contrib import admin

from .models import (
    CommentImage,
    Comments,
    Place,
    PlaceDescriptionImage,
    PlaceImage,
    PlaceRegion,
    PlaceSubcategory,
    RecommendCategory,
    RecommendedPlace,
    RecommendTags,
    ServicesIcon,
)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "category", "rating", "user")
    search_fields = ("name", "address", "category")
    list_filter = ("category", "rating")
    ordering = ("name",)


class ServicesIconAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")
    search_fields = ("name",)
    ordering = ("name",)


class PlaceRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "region")


class PlaceSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "subcategory")


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "place", "rating", "created_at")
    search_fields = ("user__nickname", "place__name", "content")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)


class CommentImageAdmin(admin.ModelAdmin):
    list_display = ("id", "comment", "image")
    search_fields = ("comment__content",)
    ordering = ("comment",)


class RecommendedPlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "place", "category", "content")


class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ("id", "place", "image")


class RecommendCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class RecommendTagsAdmin(admin.ModelAdmin):
    list_display = ("id", "tag")


class PlaceDescriptionImageAdmin(admin.ModelAdmin):
    list_display = ("id", "place", "image")


# 모델을 Admin 사이트에 등록
admin.site.register(Place, PlaceAdmin)
admin.site.register(RecommendedPlace, RecommendedPlaceAdmin)
admin.site.register(ServicesIcon, ServicesIconAdmin)
admin.site.register(PlaceRegion, PlaceRegionAdmin)
admin.site.register(PlaceSubcategory, PlaceSubcategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(CommentImage, CommentImageAdmin)
admin.site.register(PlaceImage, PlaceImageAdmin)
admin.site.register(RecommendCategory, RecommendCategoryAdmin)
admin.site.register(RecommendTags, RecommendTagsAdmin)
admin.site.register(PlaceDescriptionImage, PlaceDescriptionImageAdmin)
