from django.views.generic import ListView, CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Dish, DishType, Cook
from .forms import DishForm, CookCreationForm, DishTypeForm


class RegisterCookView(FormView):
    template_name = "registration/register.html"
    form_class = CookCreationForm
    success_url = reverse_lazy("restaurant:dish_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CookListView(LoginRequiredMixin, ListView):
    model = Cook
    template_name = "restaurant/cook_list.html"
    context_object_name = "cooks"


class DishTypeListView(LoginRequiredMixin, ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "dish_types"


class DishTypeCreateView(LoginRequiredMixin, CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "restaurant/dish_type_form.html"
    success_url = reverse_lazy("restaurant:dish_type_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Dish type created successfully!")
        return response


class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "restaurant/dish_type_form.html"
    success_url = reverse_lazy("restaurant:dish_type_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Dish type updated successfully!")
        return response


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    template_name = "restaurant/dish_list.html"
    context_object_name = "dishes"


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    form_class = DishForm
    template_name = "restaurant/dish_form.html"
    success_url = reverse_lazy("restaurant:dish_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Dish created successfully!")
        return response


class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "restaurant/dish_form.html"
    success_url = reverse_lazy("restaurant:dish_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Dish updated successfully!")
        return response
