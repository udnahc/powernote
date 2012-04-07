from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.validators import email_re

class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        username = username.strip().lower()
        if email_re.search(username):
            try:
                user = User.objects.get(email=username)
                print "This is the user object returning ", user 
                print "And the id ", user.id
                if user.check_password(password):
                    return user
                return None
            except User.DoesNotExist:
                return None

        
