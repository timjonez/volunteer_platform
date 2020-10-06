from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

WORKER = 'Volunteer'
CHURCH = 'Church'
ROLE = [
    (WORKER, 'Volunteer'),
    (CHURCH, 'Church'),
]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE, max_length=12, default=WORKER)

    REQUIRED_FIELDS = []

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

