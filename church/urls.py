from django.urls import path
from . import views

app_name = 'church'


urlpatterns = [
    path('add/', views.create_church_view, name='add_church'),
    path('<slug:slug>/edit/', views.church_edit_view, name='edit-church'),
    path('<slug:slug>/', views.church_detail_view, name='profile'),
]