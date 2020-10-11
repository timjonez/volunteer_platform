from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView, create_volunteer_view

app_name = 'user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/volunteer/', create_volunteer_view, name='volunteer'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]