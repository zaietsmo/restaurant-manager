from decimal import Decimal

from django.test import TestCase

from accounts.models import Cook
from restaurant.forms import DishForm, DishTypeForm
from restaurant.models import Dish, DishType


class DishFormTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Dessert")
        self.cook = Cook.objects.create_user(
            username="cookdessert",
            password="password123",
            first_name="Charlie",
            last_name="Brown",
            email="charlie@example.com",
            years_of_experience=4,
        )

    def test_valid_dish_form(self):
        form_data = {
            "name": "Chocolate Cake",
            "description": "Rich and moist chocolate cake.",
            "price": "8.50",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_dish_form_negative_price(self):
        form_data = {
            "name": "Expensive Dish",
            "description": "Price is negative.",
            "price": "-10.00",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id],
        }
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)


class DishTypeFormTest(TestCase):
    def test_valid_dish_type_form(self):
        form_data = {"name": "Beverage"}
        form = DishTypeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_dish_type_form_duplicate_name(self):
        DishType.objects.create(name="Starter")
        form_data = {"name": "Starter"}
        form = DishTypeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
