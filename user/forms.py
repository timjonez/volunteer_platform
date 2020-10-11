from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Volunteer


class CreateUserForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'role', 'email', 'password1', 'password2')


class CreateVolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        exclude = ['user',]
