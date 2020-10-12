from django.urls import path
from .views import create_job_view, JobDetailView, create_proposal_view

app_name = 'Job'

urlpatterns = [
    path('create-proposal/<slug:slug>/', create_proposal_view, name='create_proposal'),
    path('create_job/', create_job_view, name='create_job'),
    path('<slug:slug>/', JobDetailView.as_view(), name='view_job'),
]