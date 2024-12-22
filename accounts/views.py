from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from .forms import CookCreationForm
from .models import Cook

# Create your views here.


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
