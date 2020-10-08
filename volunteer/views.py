from django.views.generic import ListView
from Job.models import Job, Category


class HomeView(ListView):
    model = Job
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context