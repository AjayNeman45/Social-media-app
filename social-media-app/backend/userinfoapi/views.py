from rest_framework import status
from rest_framework.serializers import Serializer
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser

class userProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,) 
    def get(self,request):
        queryset = userProfile.objects.all()
        serialize_data = userProfileSerializer(queryset, many=True, context={'request':request}).data
        return Response(serialize_data)

class updateUser(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,) 
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        try:
            user_obj = User.objects.get(id = request.user.id)
            print(user_obj)
            print(request.data['username'])
            serializer = userSerializer(user_obj, data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(Serializer.errors)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class updateUserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,) 
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        user = User.objects.get(id = request.user.id)
        profile = userProfile.objects.get(user=user)
        serialize = userProfileSerializer(profile, data=request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        print(serialize.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class activityView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        try:
            follower_user = User.objects.get(id= request.data['follower'])
            following_user = User.objects.get(id=request.data['following'])
            queryset = activity.objects.get(follower=follower_user, following=following_user)
            queryset.delete()
            return Response({"message":follower_user.username +" unfollow " + following_user.username})
        except Exception as e:
            follower_user = User.objects.get(id=request.data['follower'])
            following_user = User.objects.get(id=request.data['following'])
            activity.objects.create(follower=follower_user , following=following_user)
            return Response({"message":follower_user.username + " started following "+ following_user.username})

