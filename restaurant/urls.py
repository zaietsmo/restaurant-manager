from django.urls import path

from . import views

app_name = "restaurant"

urlpatterns = [
    path("", views.DishListView.as_view(), name="dish_list"),
    path("dishes/", views.DishListView.as_view(), name="dishes"),
    path("dish/create/", views.DishCreateView.as_view(), name="dish_create"),
    path("dishes/<int:pk>/update/", views.DishUpdateView.as_view(), name="dish_update"),
    path("dishes/<int:pk>/delete/", views.DishDeleteView.as_view(), name="dish_delete"),
    path("dish-types/", views.DishTypeListView.as_view(), name="dish_type_list"),
    path(
        "dish-types/create/",
        views.DishTypeCreateView.as_view(),
        name="dish_type_create",
    ),
    path(
        "dish-types/<int:pk>/update/",
        views.DishTypeUpdateView.as_view(),
        name="dish_type_update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        views.DishTypeDeleteView.as_view(),
        name="dish_type_delete",
    ),
]
