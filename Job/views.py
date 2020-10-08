from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from church.models import Church
from .models import Job
from .forms import CreateJobForm


@login_required
def create_job_view(request):
    church = Church.objects.filter(user_id__email=request.user)
    if len(church) != 1:
        return redirect('home')
    elif request.method == 'GET':
        form = CreateJobForm()
    else:
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.church = church[0]
            job.save()
            return redirect('home')
    return render(request, 'Job/add_job.html', {'form': form,})
