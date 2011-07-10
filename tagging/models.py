from django.db import models

class TagType(models.Model):
    name = models.CharField(max_length=200, blank = False, null=False, unique=True)
    description = models.TextField()

class TagManager(models.Manager):
    pass

class Tag(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    tag_type = models.ForeignKey(TagType, null=False)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)


