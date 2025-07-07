from djoser.serializers import UserSerializer as DjoserUserSerializer
from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model


class UserCreateSerializer(DjoserUserSerializer):
    """Custom User serializer for registration"""

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password",
            "profile_type",
        )

    def validate_profile_type(self, value):
        """
        Prevents superuser from being created via API.
        """
        if value == "superuser":
            raise serializers.ValidationError("Superuser profile cannot be created via API.")
        return value

    