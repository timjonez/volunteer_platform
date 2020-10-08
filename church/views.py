from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import AddChurchForm
from .models import Church


@login_required
def create_church_view(request):
    existing_churches = Church.objects.filter(user_id__email=request.user)
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
            return redirect('home')
    return render(request, 'church/add_church.html', {'form': form,})
