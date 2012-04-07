from django.db import models
from demosite.models import DemoUser

class Feedback(models.Model):
    demo =  models.ForeignKey(DemoUser)
    message = models.TextField()

    def __str__(self):
        return "%s, Feedback - %s" % (self.demo, self.message)
