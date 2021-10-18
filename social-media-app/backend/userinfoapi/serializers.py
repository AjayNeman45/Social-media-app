from postapi.models import Post
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']

class activitySerializer(serializers.ModelSerializer):
    class Meta:
        model = activity
        fields = ['follower']

class userProfileSerializer(serializers.ModelSerializer):
    user = userSerializer(read_only=True)
    class Meta:
        model = userProfile
        fields = ['user','profile_photo','about_me']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['following_count'] = activity.objects.filter(follower=instance.user).count()
        response['followers_count'] = activity.objects.filter(following = instance.user).count()
        response['post_count'] = Post.objects.filter(user = instance.user.id).count()

        # logic for  gettig all followers id 
        queryset = activity.objects.filter(following=instance.user)
        followers_id = []
        for query in queryset:
            followers_id.append(query.follower.id)
        response['followers_id'] = followers_id
        
        # logic for getting all following id 
        queryset = activity.objects.filter(follower=instance.user)
        following_id = []
        for query in queryset:
            following_id.append(query.following.id)
        response['following_id'] = following_id

        return response