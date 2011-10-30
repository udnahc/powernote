from django.db import models
from django import forms

# Create your models here.
class PowerNoteBlog(models.Model):
    author = models.CharField(max_length=200)
    title =  models.CharField(max_length=2000)
    description =  models.TextField()
    pub_date = models.DateTimeField()
