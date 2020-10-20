from django.db import models
from phone_field import PhoneField
from address.models import AddressField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from random import randint

from user.models import User


class Church(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    picture = models.ImageField(blank=True)
    description = models.TextField(max_length=1000, blank=True)
    pastor_name = models.CharField(max_length=254)
    phone = PhoneField(help_text='Phone Number')
    address = AddressField(on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) + str(randint(1000, 1000000000))
        super().save(*args, **kwargs)

