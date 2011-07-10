from django.contrib import admin
from project.models import Project
from project.models import Module
from project.models import Ticket

admin.site.register(Project)
admin.site.register(Module)
admin.site.register(Ticket)

