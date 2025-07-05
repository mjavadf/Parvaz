# TODO: Fix d-compose and checks: https://www.notion.so/javaat/Database-20c3e76aeaaf80ef9b2ffa3c58bbf0a2?source=copy_link#20d3e76aeaaf80a6b830f0e630898aa4
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, username, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not username:
            raise ValueError("User must have a username.")
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(
            username=username, email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """Create and return a new superuser."""
        user = self.create_user(username, email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()  # type: ignore
