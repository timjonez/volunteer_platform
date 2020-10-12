from django import forms
from .models import Job, Proposal


class CreateJobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ['church', 'slug',]


class CreateProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal
        exclude = ['user', 'job',]