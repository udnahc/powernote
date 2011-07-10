from django.contrib import admin
from tagging.models import Tag
from tagging.models import TagType

admin.site.register(Tag)
admin.site.register(TagType)
