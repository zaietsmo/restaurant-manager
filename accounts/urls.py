from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterCookView, CookListView

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="accounts:login"),
        name="logout",
    ),
    path("register/", RegisterCookView.as_view(), name="register"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
]
