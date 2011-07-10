from django.db import models
from bookmark.models import Page
from project.models import Module
from project.models import Project
from project.models import Ticket

class NoteCategory(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class NoteManager(models.Manager):
    
    def update_note(self, note_id, note_category, status, description, is_active, is_ticket_shown):
        note = Note.objects.get(id = note_id)
        note.note_category = NoteCategory.objects.get(id=note_category)
        note.status = status
        note.description = description
        note.is_active = is_active
        note.is_ticket_shown
        note.save()

class Note(models.Model):
#    page_bookmark = models.ManyToManyField(Page)
    ticket = models.ForeignKey(Ticket, null=True, blank=True)
    note_category = models.ForeignKey(NoteCategory)
    url = models.CharField(max_length=500, blank=False, null=False)
    x_location = models.IntegerField(blank=False, null=False)
    y_location = models.IntegerField(blank=False, null=False)
    
    is_ticket_shown = models.BooleanField()
    is_active = models.BooleanField()
    status = models.CharField(max_length=150, null=True)
    description = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now = True)

    objects = NoteManager()
    
    def __str__(self):
        return "Category - %s, URL - %s, Description -  %s " % (self.note_category.name, self.url, self.description)
