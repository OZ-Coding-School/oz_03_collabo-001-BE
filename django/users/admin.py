from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomAdminAuthenticationForm
from .models import BookMark, ViewHistory

CustomUser = get_user_model()


class CustomUserAdmin(BaseUserAdmin):
    list_display = ("email", "nickname", "is_staff", "created_at")
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("email", "nickname")
    ordering = ("email",)
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("nickname", "profile_image")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "nickname", "password1", "password2"),
            },
        ),
    )


@admin.register(BookMark)
class BookMarkAdmin(admin.ModelAdmin):
    pass


@admin.register(ViewHistory)
class ViewHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)

# Custom authentication form for admin login
admin.site.login_form = CustomAdminAuthenticationForm
