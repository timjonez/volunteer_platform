from django.urls import path
from . import views #create_job_view, JobDetailView, create_proposal_view,

app_name = 'Job'

urlpatterns = [
    path('create-proposal/<slug:slug>/', views.create_proposal_view, name='create_proposal'),
    path('create_job/', views.create_job_view, name='create_job'),
    path('proposals/', views.ProposalListView.as_view(), name='proposals'),
    path('<slug:slug>/', views.JobDetailView.as_view(), name='view_job'),
]