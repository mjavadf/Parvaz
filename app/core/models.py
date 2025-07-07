from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

PROFILE_TYPES = (
    ("client", "Client"),
    ("therapist", "Therapist"),
    ("superuser", "Superuser"),
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(
        self, username, email, profile_type="client", password=None, **extra_fields
    ):
        """Create, save and return a new user."""
        if not username:
            raise ValueError("User must have a username.")
        if not email:
            raise ValueError("User must have an email address.")
        if profile_type not in [type for type, _ in PROFILE_TYPES]:
            raise ValueError("Invalid profile type.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            profile_type=profile_type,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """Create and return a new superuser."""
        user = self.create_user(username, email, "superuser", password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    """User Model"""

    email = models.EmailField(unique=True, blank=False)

    profile_type = models.CharField(
        max_length=10, choices=PROFILE_TYPES, default="client"
    )

    REQUIRED_FIELDS = ["email"]

    objects = UserManager()  # type: ignore
