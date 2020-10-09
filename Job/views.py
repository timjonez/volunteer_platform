from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

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


class JobDetailView(DetailView):
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        created_date = context['job'].created_date
        days_ago = today - created_date.date()
        context['listed_days_ago'] = days_ago.days
        return context
