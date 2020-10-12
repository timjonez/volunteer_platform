from django.shortcuts import render, redirect
from django.views.generic import ListView

from Job.models import Job, Category, Volunteer
from church.models import Church


def home_view(request):
    user = request.user
    if not request.user.is_authenticated:
        context = {
            'object_list':Job.objects.all(),
            'categories': Category.objects.all()
        }
    else:
        if user.role == 'Church':
            church = Church.objects.filter(user_id__email=user.email)
            if len(church) == 0:
                return redirect('church:add_church')
        elif user.role == 'Volunteer':
            volunteer = Volunteer.objects.filter(user_id__email=user.email)
            if len(volunteer) == 0:
                return redirect('user:volunteer')
        context = {
            'object_list':Job.objects.all(),
            'categories': Category.objects.all()
            }


    return render(request, 'home.html', context)

