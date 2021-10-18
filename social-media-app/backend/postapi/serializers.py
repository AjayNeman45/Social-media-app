from userinfoapi.models import userProfile
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import json
from userinfoapi.serializers import userProfileSerializer
from django.shortcuts import get_object_or_404

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name']

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','user','posted_image', 'about_post','created_at']
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        log_user = self.context['request'].user
        if instance.likes.filter(user = log_user):
            response['is_liked'] = True
        else:
            response['is_liked'] = False 

        response['likes_count'] = instance.likes.count()
        response['comments_count'] = instance.comments.count()
        queryset = userProfile.objects.get(user=instance.user.id)
        serializer_data = userProfileSerializer(queryset).data
        response['user'] = serializer_data
        return response

class commentSerializer(serializers.ModelSerializer):
    user = userSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['post','user','comment_text','timestamp']
