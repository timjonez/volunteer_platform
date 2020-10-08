from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from church.models import Church

class Category(models.Model):
    category_item = models.CharField(max_length=100, help_text='Category')

    def __str__(self):
        return self.category_item
    
DURATION = [
    ('Once', 'One Time'),
    ('Long', 'Long-term')
]

class Job(models.Model):
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
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

