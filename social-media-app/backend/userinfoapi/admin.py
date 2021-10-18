from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(userProfile)
class userProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','profile_photo','about_me')


@admin.register(activity)
class activityAdmin(admin.ModelAdmin):
    list_display = ('id','follower','following','date_and_time')