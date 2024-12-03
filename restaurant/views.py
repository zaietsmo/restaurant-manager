from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Dish, DishType, Cook
from .forms import DishForm, CookCreationForm, DishTypeForm


def register_cook(request):
    if request.method == "POST":
        form = CookCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("restaurant:dish_list")
    else:
        form = CookCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def cook_list(request):
    cooks = Cook.objects.all()
    return render(request, "restaurant/cook_list.html", {"cooks": cooks})


@login_required
def dish_type_list(request):
    dish_types = DishType.objects.all()
    return render(request, "restaurant/dish_type_list.html", {"dish_types": dish_types})


@login_required
def dish_type_create(request):
    if request.method == "POST":
        form = DishTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dish type created successfully!")
            return redirect("restaurant:dish_type_list")
    else:
        form = DishTypeForm()
    return render(request, "restaurant/dish_type_form.html", {"form": form})


@login_required
def dish_type_edit(request, pk):
    dish_type = get_object_or_404(DishType, pk=pk)
    if request.method == "POST":
        form = DishTypeForm(request.POST, instance=dish_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Dish type updated successfully!")
            return redirect("restaurant:dish_type_list")
    else:
        form = DishTypeForm(instance=dish_type)
    return render(request, "restaurant/dish_type_form.html", {"form": form})


@login_required
def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, "restaurant/dish_list.html", {"dishes": dishes})


@login_required
def dish_create(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save()
            messages.success(request, "Dish created successfully!")
            return redirect("restaurant:dish_list")
    else:
        form = DishForm()
    return render(request, "restaurant/dish_form.html", {"form": form})


@login_required
def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            dish = form.save()
            messages.success(request, "Dish updated successfully!")
            return redirect("restaurant:dish_list")
    else:
        form = DishForm(instance=dish)
    return render(request, "restaurant/dish_form.html", {"form": form})
