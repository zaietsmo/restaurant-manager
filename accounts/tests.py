from django.contrib.auth import get_user_model
from django.test import TestCase

from .forms import CookCreationForm


class AccountModelTests(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testcook",
            password="testpass123",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5,
            email="testcook@example.com",
        )

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "Test Cook")


class AccountFormTests(TestCase):
    def test_cook_creation_form_valid(self):
        form_data = {
            "username": "newcook",
            "password1": "testpass123",
            "password2": "testpass123",
            "first_name": "New",
            "last_name": "Cook",
            "email": "cook@test.com",
            "years_of_experience": 3,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_creation_form_invalid(self):
        form_data = {
            "username": "newcook",
            "password1": "testpass123",
            "password2": "testpass456",  # Mismatched passwords
            "first_name": "New",
            "last_name": "Cook",
            "email": "cook@test.com",
            "years_of_experience": -1,  # Invalid experience
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)
        self.assertIn("years_of_experience", form.errors)
