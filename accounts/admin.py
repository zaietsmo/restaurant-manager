from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook

@admin.register(Cook)
class CookAdmin(UserAdmin):
    model = Cook
    list_display = ("username", "email", "first_name", "last_name", "years_of_experience", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("years_of_experience",)}),
    )
