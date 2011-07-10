from django.contrib import admin
from note.models import NoteCategory
from note.models import Note


admin.site.register(NoteCategory)
admin.site.register(Note)
