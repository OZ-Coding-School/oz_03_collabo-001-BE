from django.contrib import admin

from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "url_link")  # 목록 화면에 표시할 필드들
    search_fields = ("category",)  # 검색할 수 있는 필드
    ordering = ("id",)  # 목록을 정렬할 기준 필드


# 모델을 Admin 사이트에 등록
admin.site.register(Banner, BannerAdmin)
