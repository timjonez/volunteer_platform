from django.urls import path
from . import views

app_name = 'church'


urlpatterns = [
    path('add/', views.create_church_view, name='add_church'),
    path('<email>/', views.church_detail_view, name='profile'),
]