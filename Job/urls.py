from django.urls import path
from . import views

app_name = 'Job'

urlpatterns = [
    path('create-proposal/<slug:slug>/', views.create_proposal_view, name='create_proposal'),
    path('create_job/', views.create_job_view, name='create_job'),
    path('proposals/', views.proposal_list_view, name='proposals'),
    path('saved/', views.saved_job_list_view, name='saved-jobs'),
    path('save-job/<slug:slug>/', views.save_job_view, name='save-job'),
    path('<slug:slug>/', views.JobDetailView.as_view(), name='view_job'),
]