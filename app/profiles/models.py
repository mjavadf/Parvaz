from django.conf import settings
from django.db import models


class Specialization(models.Model):
    """Model for specializations"""

    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name


class Language(models.Model):
    """
    Represents a language with its name and ISO code.
    """

    name = models.CharField(max_length=256)
    iso = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class TherapistProfile(models.Model):
    """Model for therapist profiles"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="therapist_profile",
    )
    # TODO: add country field
    licence_number = models.CharField(max_length=32, unique=True)
    specializations = models.ManyToManyField(
        Specialization,
        related_name="therapist_profiles",
        verbose_name="Specializations",
    )
    languages = models.ManyToManyField(
        Language, related_name="therapist_profiles", verbose_name="Languages"
    )
    bio = models.TextField(blank=True)
    # TODO: add profile photo

    def __str__(self):
        return f"{self.user.username} - {self.licence_number}"


class ClientProfile(models.Model):
    """Model for client profiles"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="client_profile",
    )
    # TODO: add country of origin field
    # TODO: add country of residence field
    languages = models.ManyToManyField(
        Language, related_name="+", verbose_name="Languages"
    )
    phone_number = models.CharField(max_length=32, blank=True)
    # TODO: add timezone field https://pypi.org/project/django-timezone-field/

    def __str__(self):
        return f"{self.user.username}"


class SuperuserProfile(models.Model):
    """Model for superuser profiles"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="superuser_profile",
    )
    phone_number = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f"{self.user.username}"
