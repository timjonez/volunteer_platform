from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import User, Volunteer
from .forms import CreateUserForm, CreateVolunteerForm


class SignUpView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/signup.html'

