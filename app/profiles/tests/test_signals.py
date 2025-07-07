"""Tests for signals in the profiles app"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from profiles.models import ClientProfile, TherapistProfile, SuperuserProfile


class SignalTests(TestCase):
    """Tests for signals in the profiles app"""

    def test_create_client_profile(self):
        """Test creating a client user creates a client profile"""
        user = get_user_model().objects.create_user(
            username="client",
            password="password123",
            email="client@example.com",
            profile_type="client",
        )

        self.assertEqual(ClientProfile.objects.count(), 1)
        self.assertEqual(ClientProfile.objects.get(user=user).user, user)

        self.assertEqual(TherapistProfile.objects.count(), 0)
        self.assertEqual(SuperuserProfile.objects.count(), 0)

    def test_create_therapist_profile(self):
        """Test creating a therapist user creates a therapist profile"""
        user = get_user_model().objects.create_user(
            username="therapist",
            password="password123",
            email="therapist@example.com",
            profile_type="therapist",
        )

        self.assertEqual(TherapistProfile.objects.count(), 1)
        self.assertEqual(TherapistProfile.objects.get(user=user).user, user)

        self.assertEqual(ClientProfile.objects.count(), 0)
        self.assertEqual(SuperuserProfile.objects.count(), 0)

    def test_create_superuser_profile(self):
        """Test creating a superuser user creates a superuser profile"""
        superuser = get_user_model().objects.create_superuser(
            username="superuser",
            email="superuser@example.com",
            password="password123",
        )

        self.assertEqual(SuperuserProfile.objects.count(), 1)
        self.assertEqual(SuperuserProfile.objects.get(user=superuser).user, superuser)
        self.assertTrue(superuser.is_superuser)

        self.assertEqual(ClientProfile.objects.count(), 0)
        self.assertEqual(TherapistProfile.objects.count(), 0)
