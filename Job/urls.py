from django.urls import path
from . import views

app_name = 'Job'

urlpatterns = [
    path('create-proposal/<slug:slug>/', views.create_proposal_view, name='create_proposal'),
    path('create_job/', views.create_job_view, name='create_job'),
    path('', views.owner_job_list_view, name='owner-job-list'),
    path('proposals/', views.proposal_list_view, name='proposals'),
    path('<slug:slug>/proposals/', views.proposal_by_job_list_view, name='proposals-by-job'),
    path('manage/<pk>/', views.manage_proposal_view, name='manage-proposal'),
    path('proposal/edit/<pk>/', views.proposal_edit_view, name='edit-proposal'),
    path('delete/<pk>/', views.proposal_delete_view, name='delete-proposal'),
    path('proposal-<pk>/', views.ProposalDetailView.as_view(), name='proposal'),
    path('saved/', views.saved_job_list_view, name='saved-jobs'),
    path('saved-job-<pk>/delete/', views.savedjob_delete_view, name='delete-savedjob'),
    path('save-job/<slug:slug>/', views.save_job_view, name='save-job'),
    path('edit/<slug:slug>/', views.job_edit_view, name='edit-job'),
    path('<slug:slug>/', views.JobDetailView.as_view(), name='view_job'),
]