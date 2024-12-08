from django.db import models
from django.contrib.auth.models import AbstractUser


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
