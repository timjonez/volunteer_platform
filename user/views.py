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


def create_volunteer_view(request):
    user = User.objects.filter(email=request.user)
    if request.method == 'GET':
        form = CreateVolunteerForm()
    else:
        form = CreateVolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.user = user[0]
            volunteer.save()
            return redirect('home')
    return render(request, 'user/add_volunteer.html', {'form': form,})
