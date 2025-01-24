from django.test import TestCase

from accounts.models import Cook


class CookModelTest(TestCase):
    def test_str_representation(self):
        cook = Cook.objects.create_user(
            username="chefjohn",
            password="password123",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            years_of_experience=10,
        )
        self.assertEqual(str(cook), "John Doe")
