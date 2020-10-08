from django.db import models

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
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

