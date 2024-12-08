from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cook
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CookCreationForm(UserCreationForm):
    years_of_experience = forms.IntegerField(
        min_value=0,
        required=True,
        help_text="Enter years of experience.",
        widget=forms.NumberInput(attrs={"placeholder": "Years of Experience"}),
    )

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email Address"}),
        }
        help_texts = {
            "username": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            "email": "A valid email address.",
        }

    def __init__(self, *args, **kwargs):
        super(CookCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Cook.objects.filter(email=email).exists():
            raise forms.ValidationError("A cook with this email already exists.")
        return email
