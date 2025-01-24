from django import forms
from django.forms import SelectMultiple

from .models import Dish, DishType


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter dish name"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter dish description",
                }
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "min": "0", "step": "0.01"}
            ),
            "dish_type": forms.Select(attrs={"class": "form-select"}),
            "cooks": SelectMultiple(attrs={"class": "form-select"}),
        }
        help_texts = {
            "cooks": "Select the chefs responsible for preparing this dish.",
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter dish type name"}
            )
        }
