from django.urls import path
from .views import create_job_view

app_name = 'Job'

urlpatterns = [
    path('create_job/', create_job_view, name='create_job'),
]