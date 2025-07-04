from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for the user model"""

    ordering = ["id"]
    list_display = ["username", "email", "is_staff", "is_superuser"]
    list_filter = ["is_staff", "is_superuser"]
    search_fields = ["username", "email"]
