"""Tests for the models in the profiles app"""

from django.contrib.auth import get_user_model
from django.test import TestCase

from profiles.models import (
    ClientProfile,
    Language,
    Specialization,
    SuperuserProfile,
    TherapistProfile,
)


class SpecializationModelTests(TestCase):
    """Tests for the Specialization model"""

    def test_create_specialization(self):
        """Test creating a specialization is successful"""
        specialization = Specialization.objects.create(
            name="Test Specialization", description="Test Description"
        )
        self.assertEqual(str(specialization), specialization.name)


class LanguageModelTests(TestCase):
    """Tests for the Language model"""

    def test_create_language(self):
        """Test creating a language is successful"""
        language = Language.objects.create(name="English", iso="en")
        self.assertEqual(str(language), language.name)


class TherapistProfileModelTests(TestCase):
    """Tests for the TherapistProfile model"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="therapist",
            password="password123",
            email="therapist@example.com",
            profile_type="therapist",
        )

    def test_create_therapist_profile(self):
        """Test creating a therapist profile is successful"""
        profile = TherapistProfile.objects.get(user=self.user)
        profile.licence_number = "12345"
        profile.save()
        self.assertEqual(
            str(profile), f"{self.user.username} - {profile.licence_number}"
        )

    def test_therapist_profile_with_specializations_and_languages(self):
        """Test creating a therapist profile with specializations and languages"""
        specialization1 = Specialization.objects.create(name="Anxiety")
        specialization2 = Specialization.objects.create(name="Depression")
        language1 = Language.objects.create(name="English", iso="en")
        language2 = Language.objects.create(name="Persian", iso="fa")

        profile = TherapistProfile.objects.get(user=self.user)
        profile.licence_number = "12345"
        profile.save()
        profile.specializations.add(specialization1, specialization2)
        profile.languages.add(language1, language2)

        self.assertEqual(profile.specializations.count(), 2)
        self.assertEqual(profile.languages.count(), 2)


class ClientProfileModelTests(TestCase):
    """Tests for the ClientProfile model"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="client",
            password="password123",
            email="client@example.com",
            profile_type="client",
        )

    def test_create_client_profile(self):
        """Test creating a client profile is successful"""
        profile = ClientProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def test_client_profile_with_languages(self):
        """Test creating a client profile with languages"""
        language1 = Language.objects.create(name="English", iso="en")
        language2 = Language.objects.create(name="Persian", iso="fa")

        profile = ClientProfile.objects.get(user=self.user)
        profile.languages.add(language1, language2)

        self.assertEqual(profile.languages.count(), 2)


class SuperuserProfileModelTests(TestCase):
    """Tests for the SuperuserProfile model"""

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="superuser", password="password123", email="superuser@example.com"
        )

    def test_create_superuser_profile(self):
        profile = SuperuserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)
