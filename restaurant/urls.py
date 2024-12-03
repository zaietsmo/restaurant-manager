from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "restaurant"

urlpatterns = [
    path("", views.DishListView.as_view(), name="dish_list"),
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
    path("register/", views.RegisterCookView.as_view(), name="register"),
    path("dishes/", views.DishListView.as_view(), name="dishes"),
    path("dish/create/", views.DishCreateView.as_view(), name="dish_create"),
    path("dish/<int:pk>/edit/", views.DishUpdateView.as_view(), name="dish_edit"),
    path("dish-types/", views.DishTypeListView.as_view(), name="dish_type_list"),
    path(
        "dish-type/create/", views.DishTypeCreateView.as_view(), name="dish_type_create"
    ),
    path(
        "dish-type/<int:pk>/edit/",
        views.DishTypeUpdateView.as_view(),
        name="dish_type_edit",
    ),
    path("cooks/", views.CookListView.as_view(), name="cook_list"),
]
