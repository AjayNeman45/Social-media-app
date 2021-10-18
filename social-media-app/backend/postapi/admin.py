from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display=('id','user','posted_image','about_post','created_at')

@admin.register(Like)
class likeAdmin(admin.ModelAdmin):
    list_display=('id','post','user','timestamp')

@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display=('id','post','user','comment_text','timestamp')
