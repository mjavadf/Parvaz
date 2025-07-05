"""Tests for models"""

from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Tests for models"""

    def test_create_user(self):
        """Test creating a user"""
        username = "testuser"
        email = "testuser@example.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(username, email, password)

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.has_usable_password())

        # Check that the user is in the database
        self.assertTrue(get_user_model().objects.filter(username=username).exists())

        # Check that the user can log in
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test creating a superuser."""
        username = "testsuperuser"
        email = "testsuperuser@example.com"
        password = "testpassword"
        user = get_user_model().objects.create_superuser(
            username=username, email=email, password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_with_no_email_raises_error(self):
        """Test that creating a user with no email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username="testuser", password="password", email=""
            )

    def test_create_user_with_no_username_raises_error(self):
        """Test that creating a user with no username raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username="", password="password", email="test@example.com"
            )

    def test_create_user_with_no_password_is_unusable(self):
        """Test that creating a user with no password is not usable"""
        username = "test_user_no_pass"
        user = get_user_model().objects.create_user(
            username=username, password=None, email="test@example.com"
        )

        self.assertFalse(user.has_usable_password())
