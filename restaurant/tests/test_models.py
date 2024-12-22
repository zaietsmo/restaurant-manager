from decimal import Decimal

from django.test import TestCase

from accounts.models import Cook
from restaurant.models import Dish, DishType


class DishTypeModelTest(TestCase):
    def test_str_representation(self):
        dish_type = DishType.objects.create(name="Appetizer")
        self.assertEqual(str(dish_type), "Appetizer")


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook1 = Cook.objects.create_user(
            username="cook1",
            password="password123",
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            years_of_experience=5,
        )
        self.cook2 = Cook.objects.create_user(
            username="cook2",
            password="password123",
            first_name="Bob",
            last_name="Johnson",
            email="bob@example.com",
            years_of_experience=7,
        )
        self.dish = Dish.objects.create(
            name="Grilled Salmon",
            description="Delicious grilled salmon with herbs.",
            price=Decimal("15.99"),
            dish_type=self.dish_type,
        )
        self.dish.cooks.set([self.cook1, self.cook2])

    def test_str_representation(self):
        self.assertEqual(str(self.dish), "Grilled Salmon")

    def test_cooks_assigned(self):
        cooks = self.dish.cooks.all()
        self.assertIn(self.cook1, cooks)
        self.assertIn(self.cook2, cooks)
