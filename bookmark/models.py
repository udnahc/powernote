from django.db import models
from tagging.models import Tag


class PageManager(models.Manager):
    pass

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    page_content = models.TextField(blank=False, null=True)
    url = models.TextField(blank=False, null=True)
    follow_up_page = models.ForeignKey('self')
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now = True)

