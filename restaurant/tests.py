from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .forms import DishForm, DishTypeForm
from .models import Dish, DishType


class ModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=Decimal("9.99"),
            dish_type=self.dish_type,
        )

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), "Main Course")

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Test Dish")


class FormTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")

    def test_dish_form_valid(self):
        form_data = {
            "name": "New Dish",
            "description": "Description",
            "price": "10.99",
            "dish_type": self.dish_type.id,
            "cooks": [],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_form_valid(self):
        form_data = {"name": "New Type"}
        form = DishTypeForm(data=form_data)
        self.assertTrue(form.is_valid())


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=Decimal("9.99"),
            dish_type=self.dish_type,
        )

    def test_dish_list_view_requires_login(self):
        response = self.client.get(reverse("restaurant:dish_list"))
        self.assertEqual(response.status_code, 302)

    def test_dish_list_view_logged_in(self):
        cook = get_user_model().objects.create_user(
            username="testcook", password="testpass123"
        )
        self.client.login(username="testcook", password="testpass123")
        response = self.client.get(reverse("restaurant:dish_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "restaurant/dish_list.html")
        self.assertContains(response, "Test Dish")

    def test_dish_create_view(self):
        cook = get_user_model().objects.create_user(
            username="testcook", password="testpass123"
        )
        self.client.login(username="testcook", password="testpass123")
        response = self.client.get(reverse("restaurant:dish_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "restaurant/dish_form.html")
