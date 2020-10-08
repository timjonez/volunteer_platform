from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import AddChurchForm
from .models import Church


def create_church_view(request):
    if request.method == 'GET':
        form = AddChurchForm()
    else:
        form = AddChurchForm(request.POST, request.FILES)
        if form.is_valid():
            church = form.save(commit=False)
            church.user = request.user
            church.save()
            return redirect('home')
    return render(request, 'church/add_church.html', {'form': form,})
