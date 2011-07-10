from django.db import models
from django.contrib.auth.models import User

class UserProfileManager(models.Manager):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    name = models.CharField(blank=True, max_length=200)
    personal_email = models.EmailField(blank=False, unique=True)
    description = models.CharField(blank=True, null=True, max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    objects = UserProfileManager()
