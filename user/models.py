from django.db import models
from phone_field import PhoneField
from address.models import AddressField
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

WORKER = 'Volunteer'
CHURCH = 'Church'
ROLE = [
    (WORKER, 'Volunteer'),
    (CHURCH, 'Church'),
]

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE, max_length=12, default=WORKER)

    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    intro = models.TextField(max_length=300, blank=True)
    phone = PhoneField(help_text='Phone Number')
    address = AddressField(on_delete=models.CASCADE,)

    def __str__(self):
        return self.user.email

