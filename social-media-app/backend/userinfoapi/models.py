from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.utils.translation import gettext_lazy as _
# Create your models here.

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        _("Image"), upload_to=upload_to, blank=True, null=True)
    about_me = models.CharField(max_length=1000, blank=True, null=True)

class activity(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    date_and_time = models.DateTimeField(auto_now_add=True)
