from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import AddChurchForm
from .models import Church
from user.models import User


@login_required
def create_church_view(request):
    existing_churches = Church.objects.filter(user_id__email=request.user)
    user = User.objects.get(email=request.user) 
    if len(existing_churches) != 0:
        return redirect('home')
    elif request.method == 'GET':
        form = AddChurchForm()
    else:
        form = AddChurchForm(request.POST, request.FILES)
        if form.is_valid():
            church = form.save(commit=False)
            church.user = request.user
            church.save()
            user.attached_church = church
            user.save()
            return redirect('home')
    return render(request, 'church/add_church.html', {'form': form,})


def church_detail_view(request, slug):
    church = Church.objects.get(slug=slug)
    return render(request, 'church/church_detail.html', {'church':church,})


@login_required
def church_edit_view(request, slug):
    church = Church.objects.get(slug=slug)
    if church.user != request.user:
        return redirect('home')
    form = AddChurchForm(request.POST or None, instance=church)
    if form.is_valid():
        form.save()
        return redirect('church:profile', slug=slug)
    return render(request, 'church/add_church.html', {'form': form})