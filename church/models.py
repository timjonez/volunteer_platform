from django.db import models
from phone_field import PhoneField
from address.models import AddressField
from django.utils import timezone

from user.models import User


class Church(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='uploaded')
    description = models.TextField(max_length=1000, blank=True)
    pastor_name = models.CharField(max_length=254)
    phone = PhoneField(help_text='Phone Number')
    address = AddressField(on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
