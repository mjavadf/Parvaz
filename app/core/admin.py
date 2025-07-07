from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """
    Define the admin pages for the user model.
    """
    ordering = ["id"]
    list_display = ["username", "email", "profile_type", "is_staff", "is_superuser"]
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "profile_type",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    
    fieldsets = (
        (None, {"fields": ("username", "password", "profile_type",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    
    
    