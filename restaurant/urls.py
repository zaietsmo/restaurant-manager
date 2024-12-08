from django.urls import path
from . import views

app_name = "restaurant"

urlpatterns = [
    path("", views.DishListView.as_view(), name="dish_list"),
    path("dishes/", views.DishListView.as_view(), name="dishes"),
    path("dish/create/", views.DishCreateView.as_view(), name="dish_create"),
    path("dish/<int:pk>/edit/", views.DishUpdateView.as_view(), name="dish_edit"),
    path("dish/<int:pk>/delete/", views.DishDeleteView.as_view(), name="dish_delete"),
    path("dish-types/", views.DishTypeListView.as_view(), name="dish_type_list"),
    path(
        "dish-type/create/", views.DishTypeCreateView.as_view(), name="dish_type_create"
    ),
    path(
        "dish-type/<int:pk>/edit/",
        views.DishTypeUpdateView.as_view(),
        name="dish_type_edit",
    ),
    path(
        "dish-type/<int:pk>/delete/",
        views.DishTypeDeleteView.as_view(),
        name="dish_type_delete",
    ),
]
