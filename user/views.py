from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
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


class VolunteerDetailView(DetailView):
    model = Volunteer
    slug_field = 'user__email'

@login_required
def volunteer_edit_view(request, email):
    user = Volunteer.objects.get(user__email=email)
    print(user.user)
    print(request.user)
    if user.user != request.user:
        return redirect('home')
    form = CreateVolunteerForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user:see-profile', slug=user.user.email)
    return render(request, 'user/add_volunteer.html', {'form': form})
