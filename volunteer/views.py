from django.views.generic import ListView
from Job.models import Job


class HomeView(ListView):
    model = Job
    template_name = 'home.html'