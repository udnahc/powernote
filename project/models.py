from django.db import models
from poweruser.models import UserProfile
from tagging.models import Tag
from bookmark.models import Page

class ProjectManager(models.Manager):
    pass

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.ManyToManyField(UserProfile, blank=False)
    name = models.CharField(max_length=200,blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=False,null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    objects = ProjectManager()


class ModuleManager(models.Manager):
    pass

class Module(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    tags = models.ManyToManyField(Tag, blank=False,null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now = True)
    
class AttachmentsManager(models.Manager):
    pass

class Attachments(models.Model):
    id = models.AutoField(primary_key=True)
    file_path = models.FileField(upload_to='docs/%Y/%m/%d')
    description = models.TextField()
   
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now = True)
    objects = AttachmentsManager()


class TicketManager(models.Manager):
    pass

class Ticket(models.Model):
    id = models.AutoField(primary_key = True)
    module = models.ForeignKey(Module)
    project = models.ForeignKey(Project)
    tags = models.ManyToManyField(Tag , blank=True, null=True)
    attachments = models.ManyToManyField(Attachments, blank=True, null=True)
    bookmarks = models.ManyToManyField(Page, blank=True, null=True)

    title = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now = True)
    objects = TicketManager()

