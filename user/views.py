from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import User
from .forms import CreateUserForm


class SignUpView(CreateView):
    form_class = CreateUserForm
    success = reverse_lazy('login')
    template_name = 'user/signup.html'

