from django.contrib import admin

from .models import Banner, Category


# Category 모델에 대한 관리자 클래스
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # 목록 화면에 표시할 필드들
    search_fields = ("name",)  # 검색할 수 있는 필드
    ordering = ("name",)  # 목록을 정렬할 기준 필드


# Banner 모델에 대한 관리자 클래스
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "url_link")  # 목록 화면에 표시할 필드들
    search_fields = ("category__name",)  # 카테고리 이름을 기준으로 검색
    ordering = ("id",)  # 목록을 정렬할 기준 필드


# 모델을 Admin 사이트에 등록
admin.site.register(Category, CategoryAdmin)
admin.site.register(Banner, BannerAdmin)
