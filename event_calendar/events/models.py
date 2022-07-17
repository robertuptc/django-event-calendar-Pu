from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import (AbstractUser)


class AppUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    password = models.CharField(max_length=200)
    is_active: models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    starts_at = models.DateTimeField(default=timezone.now)
    ends_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='events')