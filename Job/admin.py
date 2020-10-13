from django.contrib import admin
from .models import Job, Category, Proposal, SavedJob

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Proposal)
admin.site.register(SavedJob)