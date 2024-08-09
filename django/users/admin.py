from django.contrib import admin
from django.utils.translation import gettext_lazy as lz
from .models import CustomUser

# Register your models here.
class UserTypeFilter(admin.SimpleListFilter):
    # '회원 유형' 필터의 제목
    title = lz('회원유형')
    #url 쿼리에서 사용될 파라미터 이름
    parameter_name = 'user_type'

    def lookups(self, request, model_admin):
        # 관리자 페이지에서 보여질 필터 옵션
        return (('is_staff', lz('운영진')),)
    def queryset(self, request, queryset):
        return queryset.filter(is_staff=True)

        
class UserAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 보여줄 필드 목록을 설정
    list_display = ('nickname', 'email', 'is_staff', 'created_at')
    # 필터 옵션을 제공팔 필드 목록을 설정
    list_filter = (UserTypeFilter,)
    # 읽기 전용 필드 목록을 설정
    readonly_fields = ('email', 'created_at', 'updated_at')

# user 모델을 관리자 페이지에 등록
admin.site.register(CustomUser, UserAdmin)