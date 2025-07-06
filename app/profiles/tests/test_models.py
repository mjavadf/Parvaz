"""Tests for the models in the profiles app"""

from django.contrib.auth import get_user_model
from django.test import TestCase

from profiles.models import ClientProfile, Language, Specialization, TherapistProfile


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
        self.user = get_user_model().objects.create_user("therapist", "password123")

    def test_create_therapist_profile(self):
        """Test creating a therapist profile is successful"""
        profile = TherapistProfile.objects.create(
            user=self.user, licence_number="12345"
        )
        self.assertEqual(str(profile), f"{self.user.username} - {profile.licence_number}")

    def test_therapist_profile_with_specializations_and_languages(self):
        """Test creating a therapist profile with specializations and languages"""
        specialization1 = Specialization.objects.create(name="Anxiety")
        specialization2 = Specialization.objects.create(name="Depression")
        language1 = Language.objects.create(name="English", iso="en")
        language2 = Language.objects.create(name="Persian", iso="fa")

        profile = TherapistProfile.objects.create(
            user=self.user, licence_number="12345"
        )
        profile.specializations.add(specialization1, specialization2)
        profile.languages.add(language1, language2)

        self.assertEqual(profile.specializations.count(), 2)
        self.assertEqual(profile.languages.count(), 2)


class ClientProfileModelTests(TestCase):
    """Tests for the ClientProfile model"""

    def setUp(self):
        self.user = get_user_model().objects.create_user("client", "password123")

    def test_create_client_profile(self):
        """Test creating a client profile is successful"""
        profile = ClientProfile.objects.create(user=self.user)
        self.assertEqual(str(profile), self.user.username)

    def test_client_profile_with_languages(self):
        """Test creating a client profile with languages"""
        language1 = Language.objects.create(name="English", iso="en")
        language2 = Language.objects.create(name="Persian", iso="fa")

        profile = ClientProfile.objects.create(user=self.user)
        profile.languages.add(language1, language2)

        self.assertEqual(profile.languages.count(), 2)