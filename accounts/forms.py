from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cook


class CookCreationForm(UserCreationForm):
    years_of_experience = forms.IntegerField(
        min_value=0, required=True, help_text="Enter years of experience."
    )

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )
