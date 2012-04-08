from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    demo =  models.ForeignKey(User)
    message = models.TextField()

    def __str__(self):
        return "%s, Feedback - %s" % (self.demo, self.message)
