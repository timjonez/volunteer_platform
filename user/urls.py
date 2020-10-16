from django.urls import path
from django.contrib.auth import views as auth_views

from . import views # SignUpView, create_volunteer_view

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/volunteer/', views.create_volunteer_view, name='volunteer'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('volunteer/<slug>/', views.VolunteerDetailView.as_view(), name='see-profile'),
    path('volunteer/<email>/edit/', views.volunteer_edit_view, name='volunteer-edit'),
]