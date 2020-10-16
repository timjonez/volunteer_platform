from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect

from church.models import Church
from .models import Job, Proposal, SavedJob
from .forms import CreateJobForm, CreateProposalForm
from user.models import Volunteer


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


@login_required
def create_proposal_view(request, slug):
    user = Volunteer.objects.filter(user_id__email=request.user)
    job = Job.objects.filter(slug=slug)
    if user[0].user.role ==  'Church':
        return redirect('home')
    elif request.method == 'GET':
        form = CreateProposalForm
    else:
        form = CreateProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.user = user[0]
            proposal.job = job[0]
            proposal.save()
            return redirect('home')
    return render(request, 'Job/add_proposal.html', {'form': form})

@login_required
def owner_job_list_view(request):
    church = Church.objects.filter(user__email=request.user)
    if church.count() == 0:
        return redirect('home')
    else:
        jobs = Job.objects.filter(church=church[0]).order_by('-created_date')
        return render(request, 'Job/owner_job_list.html', {'object_list': jobs})

@login_required
def job_edit_view(request, slug):
    job = Job.objects.get(slug=slug)
    if job.church.user != request.user:
        return redirect('home')
    form = CreateJobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('job:view_job', slug=job.slug)
    return render(request, 'Job/add_job.html', {'form': form})


class JobDetailView(DetailView):
    model = Job

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().date()
        created_date = context['job'].created_date
        days_ago = today - created_date.date()
        context['listed_days_ago'] = days_ago.days
        return context


class ProposalDetailView(DetailView):
    model = Proposal


@login_required
def proposal_list_view(request):
    user = Volunteer.objects.get(user_id__email=request.user)
    proposals = Proposal.objects.filter(user=user)
    return render(request, 'Job/proposal_list.html', {'object_list': proposals})

@login_required
def proposal_by_job_list_view(request, slug):
    job = Job.objects.get(slug=slug)
    proposals = Proposal.objects.filter(job=job)
    if job.church.user != request.user:
        return redirect('home')
    else:
        return render(request, 'Job/proposal_list.html', {'object_list': proposals})

@login_required
def proposal_edit_view(request, pk):
    proposal = Proposal.objects.get(pk=pk)
    if proposal.user.user != request.user:
        return redirect('home')
    form = CreateProposalForm(request.POST or None, instance=proposal)
    if form.is_valid():
        form.save()
        return redirect('job:proposal', pk=proposal.pk)
    return render(request, 'Job/add_proposal.html', {'form': form})



@login_required
def proposal_delete_view(request, pk):
    proposal = Proposal.objects.get(pk=pk)
    proposal.delete()
    return redirect('job:proposals')


@login_required
def savedjob_delete_view(request, pk):
    job = SavedJob.objects.get(pk=pk)
    job.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def saved_job_list_view(request):
    user = Volunteer.objects.get(user_id__email=request.user)
    jobs = SavedJob.objects.filter(user=user)
    return render(request, 'Job/savedjob_list.html', {'object_list': jobs})


@login_required
def save_job_view(request, slug):
    user = Volunteer.objects.get(user_id__email=request.user)
    job = Job.objects.get(slug=slug)
    saved_job = SavedJob(user=user, job=job)
    saved_job.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def manage_proposal_view(request, pk):
    proposal = Proposal.objects.get(pk=pk)
    accept = request.GET.get('accept')
    if proposal.job.church.user != request.user:
        return redirect('home')
    else:
        if accept == "True":
            print('accepted')
            proposal.accepted = True
            proposal.save()
        elif accept == "False":
            print('reject')
            proposal.accepted = False
            proposal.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
