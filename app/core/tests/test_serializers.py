from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from profiles.models import ClientProfile, SuperuserProfile, TherapistProfile


class UserCreationSerializerTests(APITestCase):
    """Tests for custom user creation serializer"""

    def setUp(self):
        self.create_user_url = reverse("djoser:user-list")
        self.User = get_user_model()

    def test_create_client_user_with_valid_data(self):
        """Test creating a client user with valid data"""
        payload = {
            "username": "testclient",
            "email": "client@example.com",
            "password": "password123",
            "re_password": "password123",
            "profile_type": "client",
        }
        response = self.client.post(self.create_user_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertTrue(self.User.objects.filter(username="testclient").exists())
        self.assertTrue(ClientProfile.objects.filter(user__username="testclient").exists())
        self.assertFalse(TherapistProfile.objects.filter(user__username="testclient").exists())
        self.assertFalse(SuperuserProfile.objects.filter(user__username="testclient").exists())

    def test_create_therapist_user_with_valid_data(self):
        """Test creating a therapist user with valid data"""
        payload = {
            "username": "testtherapist",
            "email": "therapist@example.com",
            "password": "password123",
            "re_password": "password123",
            "profile_type": "therapist",
        }
        response = self.client.post(self.create_user_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertTrue(self.User.objects.filter(username="testtherapist").exists())
        self.assertTrue(TherapistProfile.objects.filter(user__username="testtherapist").exists())
        self.assertFalse(ClientProfile.objects.filter(user__username="testtherapist").exists())
        self.assertFalse(SuperuserProfile.objects.filter(user__username="testtherapist").exists())

    def test_create_user_with_invalid_profile_type(self):
        """Test creating a user with an invalid profile type"""
        payload = {
            "username": "invaliduser",
            "email": "invalid@example.com",
            "password": "password123",
            "re_password": "password123",
            "profile_type": "invalid",
        }
        response = self.client.post(self.create_user_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.User.objects.count(), 0)
        self.assertIn("profile_type", response.data)

    def test_create_user_without_profile_type(self):
        """Test creating a user without specifying profile type creates a client user"""
        payload = {
            "username": "nouser",
            "email": "no@example.com",
            "password": "password123",
            "re_password": "password123",
        }
        response = self.client.post(self.create_user_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertTrue(self.User.objects.filter(username="nouser").exists())
        self.assertTrue(ClientProfile.objects.filter(user__username="nouser").exists())
        self.assertFalse(TherapistProfile.objects.filter(user__username="nouser").exists())
        self.assertFalse(SuperuserProfile.objects.filter(user__username="nouser").exists())
        

    def test_create_superuser_via_api_is_not_allowed(self):
        """Test that superuser cannot be created via API"""
        payload = {
            "username": "apisup",
            "email": "apisup@example.com",
            "password": "password123",
            "re_password": "password123",
            "profile_type": "superuser",
        }
        response = self.client.post(self.create_user_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.User.objects.count(), 0)
        self.assertIn("profile_type", response.data)
