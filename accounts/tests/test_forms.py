from django.test import TestCase

from accounts.forms import CookCreationForm
from accounts.models import Cook


class CookCreationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "username": "newcook",
            "password1": "strongpassword",
            "password2": "strongpassword",
            "first_name": "Anna",
            "last_name": "Williams",
            "email": "anna@example.com",
            "years_of_experience": 5,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_password_mismatch(self):
        form_data = {
            "username": "newcook",
            "password1": "strongpassword",
            "password2": "wrongpassword",
            "first_name": "Anna",
            "last_name": "Williams",
            "email": "anna@example.com",
            "years_of_experience": 5,
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_invalid_form_duplicate_email(self):
        Cook.objects.create_user(
            username="existingcook",
            password="password123",
            email="existing@example.com",
            years_of_experience=8,
        )
        form_data = {
            "username": "newcook",
            "password1": "strongpassword",
            "password2": "strongpassword",
            "first_name": "Anna",
            "last_name": "Williams",
            "email": "existing@example.com",
            "years_of_experience": 5,
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
