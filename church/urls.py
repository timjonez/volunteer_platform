from django.urls import path
from .views import create_church_view

app_name = 'church'


urlpatterns = [
    path('add/', create_church_view, name='add_church'),
]