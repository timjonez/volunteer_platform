from django.shortcuts import render, redirect
from django.db.models import Q
from Job.models import Job, Category


def search_list_view(request):
    if request.method == 'GET':
        search_term = request.GET.get("searchterm", "")
        search_category = request.GET.get('category', "")
        print(search_term)
        if search_term == "" and search_category == "":
            return redirect('home')
        elif search_category == 'all' and search_term == "":
            return redirect('home')
        elif search_term == "" and search_category != "":
            category = Category.objects.filter(category_item=search_category)
            data = Job.objects.filter(category__category_item=search_category)
        elif search_term != "" and search_category == "all":
            category = Category.objects.all()
            data = Job.objects.filter(Q(church__name__icontains=search_term)|
                                      Q(title__icontains=search_term) |
                                      Q(body__icontains=search_term) |
                                      Q(duration__icontains=search_term))
        else:
            category = Category.objects.all()
            data = Job.objects.filter(category__category_item=search_category) 
            data = data.filter(Q(church__name__icontains=search_term)|
                                      Q(title__icontains=search_term) |
                                      Q(body__icontains=search_term) |
                                      Q(duration__icontains=search_term))
    return render(request, 'home.html', {'object_list': data, 'categories': category})
