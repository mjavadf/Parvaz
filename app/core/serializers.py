from djoser.serializers import UserSerializer as DjoserUserSerializer
from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


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
            raise serializers.ValidationError(
                "Superuser profile cannot be created via API."
            )
        return value

    def validate(self, attrs):
        """
        Validate password against auth validators
        """
        user = self.Meta.model(**attrs)
        password = attrs.get("password")
        try:
            validate_password(password, user)
        except ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)

    