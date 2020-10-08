from django.urls import path
from .views import search_list_view

app_name = 'search'

urlpatterns = [
    path('', search_list_view, name='search'),
]