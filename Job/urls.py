from django.urls import path
from .views import create_job_view, JobDetailView

app_name = 'Job'

urlpatterns = [
    path('create_job/', create_job_view, name='create_job'),
    path('<slug:slug>/', JobDetailView.as_view(), name='view_job'),
]