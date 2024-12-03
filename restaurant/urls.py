from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "restaurant"

urlpatterns = [
    path("", views.dish_list, name="dish_list"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="restaurant:login"),
        name="logout",
    ),
    path("register/", views.register_cook, name="register"),
    path("dishes/", views.dish_list, name="dishes"),
    path("dish/create/", views.dish_create, name="dish_create"),
    path("dish/<int:pk>/edit/", views.dish_edit, name="dish_edit"),
    path("dish-types/", views.dish_type_list, name="dish_type_list"),
    path("dish-type/create/", views.dish_type_create, name="dish_type_create"),
    path("dish-type/<int:pk>/edit/", views.dish_type_edit, name="dish_type_edit"),
    path("cooks/", views.cook_list, name="cook_list"),
]
