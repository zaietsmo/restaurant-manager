from django import forms
from .models import Dish, DishType


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "dish_type": forms.Select(attrs={"class": "form-select"}),
            "cooks": forms.SelectMultiple(attrs={"class": "form-select"}),
        }


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter dish type name"}
            )
        }
