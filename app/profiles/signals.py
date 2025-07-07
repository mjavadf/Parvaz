"""Signals for the profiles app"""

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ClientProfile, SuperuserProfile, TherapistProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.profile_type == "superuser":
            SuperuserProfile.objects.create(user=instance)
        elif instance.profile_type == "therapist":
            TherapistProfile.objects.create(user=instance)
        else:
            ClientProfile.objects.create(user=instance)
