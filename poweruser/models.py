from django.db import models
from django.contrib.auth.models import User

class UserProfileManager(models.Manager):
    def user_exists(self, personal_email):
        try:
            up = UserProfile.objects.get(personal_email = personal_email)        
            user = User.objects.get(email = personal_email)
            return True
        except Exception, e:
            return False

    def save_user(self, name, personal_email):
        default_password = "%s%s" % (name, "123")
        user_object = User.objects.create_user(name, personal_email, default_password)
        print "Actual user object >>>>>>> ", user_object.id
        
        user_profile = UserProfile()
        user_profile.user = user_object
        user_profile.name = name
        user_profile.personal_email = personal_email
        user_profile.save()
        return True

class UserProfile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User)
    name = models.CharField(blank=True, max_length=200)
    personal_email = models.EmailField(blank=False, unique=True)
    description = models.CharField(blank=True, null=True, max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    objects = UserProfileManager()
