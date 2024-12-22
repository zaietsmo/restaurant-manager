from decimal import Decimal

from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Cook
from restaurant.models import Dish, DishType


class DishListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dish_type = DishType.objects.create(name="Salad")
        self.cook = Cook.objects.create_user(
            username="saladcook",
            password="password123",
            first_name="Diana",
            last_name="Prince",
            email="diana@example.com",
            years_of_experience=6,
        )
        self.dish = Dish.objects.create(
            name="Caesar Salad",
            description="Fresh romaine lettuce with Caesar dressing.",
            price=Decimal("7.99"),
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("restaurant:dish_list"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("accounts:login")))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username="saladcook", password="password123")
        response = self.client.get(reverse("restaurant:dish_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "restaurant/dish_list.html")
        self.assertContains(response, "Caesar Salad")


class DishCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dish_type = DishType.objects.create(name="Appetizer")
        self.cook = Cook.objects.create_user(
            username="appetizercook",
            password="password123",
            first_name="Eve",
            last_name="Adams",
            email="eve@example.com",
            years_of_experience=3,
        )

    def test_create_dish_requires_login(self):
        response = self.client.get(reverse("restaurant:dish_create"))
        self.assertEqual(response.status_code, 302)

    def test_create_dish_form_valid(self):
        self.client.login(username="appetizercook", password="password123")
        form_data = {
            "name": "Bruschetta",
            "description": "Grilled bread topped with diced tomatoes and basil.",
            "price": "5.50",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id],
        }
        response = self.client.post(reverse("restaurant:dish_create"), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="Bruschetta").exists())

    def test_create_dish_form_invalid(self):
        self.client.login(username="appetizercook", password="password123")
        form_data = {
            "name": "",
            "description": "Incomplete form data.",
            "price": "0",
            "dish_type": self.dish_type.id,
            "cooks": [],
        }
        response = self.client.post(reverse("restaurant:dish_create"), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context, "Form not found in response context.")
        form = response.context.get("form")

        self.assertIsNotNone(form, "Form is None in response context.")
        self.assertTrue(
            hasattr(form, "is_valid"), "Form does not have is_valid method."
        )

        print(f"Form type: {type(form)}")
        print(f"Form errors: {form.errors}")

        self.assertFalse(form.is_valid(), "Form should be invalid but is valid.")

        self.assertIn("name", form.errors, "Name field should have errors.")
        self.assertIn("price", form.errors, "Price field should have errors.")
        self.assertEqual(
            form.errors["name"],
            ["This field is required."],
            "Incorrect error message for name.",
        )
        self.assertEqual(
            form.errors["price"],
            ["Price must be greater than zero."],
            "Incorrect error message for price.",
        )


class DishDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.dish_type = DishType.objects.create(name="Dessert")
        self.cook = Cook.objects.create_user(
            username="dessertcook",
            password="password123",
            first_name="Frank",
            last_name="Miller",
            email="frank@example.com",
            years_of_experience=8,
        )
        self.dish = Dish.objects.create(
            name="Tiramisu",
            description="Classic Italian dessert with coffee and mascarpone.",
            price=Decimal("6.50"),
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_delete_dish_requires_login(self):
        response = self.client.get(
            reverse("restaurant:dish_delete", args=[self.dish.id])
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_dish_successfully(self):
        self.client.login(username="dessertcook", password="password123")
        response = self.client.post(
            reverse("restaurant:dish_delete", args=[self.dish.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())
