from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from church.models import Church
from user.models import Volunteer

class Category(models.Model):
    category_item = models.CharField(max_length=100, help_text='Category')

    def __str__(self):
        return self.category_item
    
DURATION = (
    ('Once', 'One Time'),
    ('Long', 'Long-term')
)

class Job(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(choices=DURATION, max_length=50, default='Once')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return 'By ' + self.church.name +': '+ self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.church.name +'-'+ self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return 'jobs/' + self.slug


TIMEFRAME = (
    ('One week', 'Less than 1 week'),
    ('One month', 'Less than 1 month'),
    ('three months', '1 to 3 months'),
    ('three and up', 'More than 3 months'),
)

class Proposal(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    date_submitted = models.DateField(auto_now_add=True)
    timeframe = models.CharField(max_length=20, choices=TIMEFRAME, default='One week')
    body = models.TextField()
    files = models.FileField(upload_to='attachments/', blank=True, null=True)
    accepted = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return str(self.user.user.email) + ' + ' + str(self.job)


class SavedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    unique_together = ['job', 'user',]

    def __str__(self):
        return self.job.title
