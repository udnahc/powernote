from django.db import models

class DemoUser(models.Model):
    username = models.CharField(max_length=200)
    personal_email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "Username - %s, Email - %s, Login date -  %s " % (self.username, self.personal_email, self.created_on)
