from django.test import Client, TestCase
from django.urls import reverse

from accounts.forms import CookCreationForm
from accounts.models import Cook


class RegisterCookViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("accounts:register")

    def test_register_page_loads_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_register_new_cook(self):
        form_data = {
            "username": "newcook",
            "password1": "strongpassword",
            "password2": "strongpassword",
            "first_name": "Laura",
            "last_name": "Smith",
            "email": "laura@example.com",
            "years_of_experience": 4,
        }
        response = self.client.post(self.register_url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cook.objects.filter(username="newcook").exists())

    def test_register_cook_with_existing_email(self):
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
            "first_name": "Laura",
            "last_name": "Smith",
            "email": "existing@example.com",
            "years_of_experience": 4,
        }
        response = self.client.post(self.register_url, data=form_data)

        self.assertEqual(response.status_code, 200)

        self.assertIn("form", response.context)
        form = response.context["form"]

        self.assertFalse(form.is_valid())

        self.assertIn("email", form.errors)
        self.assertEqual(
            form.errors["email"], ["A cook with this email already exists."]
        )


class CookListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cook1 = Cook.objects.create_user(
            username="cook1",
            password="password123",
            first_name="Robert",
            last_name="Brown",
            email="robert@example.com",
            years_of_experience=12,
        )
        self.cook2 = Cook.objects.create_user(
            username="cook2",
            password="password123",
            first_name="Linda",
            last_name="Green",
            email="linda@example.com",
            years_of_experience=7,
        )
        self.cook_list_url = reverse("accounts:cook_list")

    def test_cook_list_requires_login(self):
        response = self.client.get(self.cook_list_url)
        self.assertEqual(response.status_code, 302)

    def test_cook_list_display_cooks(self):
        self.client.login(username="cook1", password="password123")
        response = self.client.get(self.cook_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Robert Brown")
        self.assertContains(response, "Linda Green")
