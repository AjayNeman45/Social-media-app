from userinfoapi.models import userProfile
from userinfoapi.serializers import userProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
# from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from datetime import  datetime

class allPosts(APIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 
    def get(self, request):
        posts = Post.objects.all()
        serialize_data = postSerializer(posts, many=True, context={"request": request}).data
        return Response(serialize_data)
   
class addPost(APIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        serializer = postSerializer(data = request.data, context={'request',request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status' : 201, 'message' : "data added"})
        return Response({'status':403, "message": "you are not authenticated"})
         
class likePost(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk):
        try:
            post = Post.objects.get(id=pk)
        except Exception as e:
            return Response("post not found")
    
        try:
            like = False
            post.likes.get(user=request.user).delete()
        except Exception as e:
            like = True
            new_like = Like.objects.create(user=request.user, post=post)
            new_like.save()

        data = {
            'like': like
        }

        return Response(data)

class commentPosts(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,) 

    serializer_class = commentSerializer
    def post(self,request):
        try:
            print(request.data)
            post_object = Post.objects.get(id=request.data['post'])
            user_object = User.objects.get(id=request.data['user'])
            add_comment = Comment.objects.create(
                comment_text=request.data['comment_text'],
                post=post_object,
                user=user_object)
            
            add_comment.save()
            return Response("comment added")
        except Exception as e:
            return Response("post not found")
    
class allComments(APIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 
    def get(self, request,pk):
        try:
           post = Post.objects.get(id=pk)
           comments = post.comments.all()
           serializer = commentSerializer(comments, many=True)
           return Response(serializer.data)
        except Exception as e:
            print(type(e))
            print(e)
            return Response(status=404)

class userPosts(APIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 

    def get(self, request,username):
        try:
            print(username)
            user = User.objects.get(username = username)
            posts = Post.objects.filter(user=user)
            print(posts)
            serializer_data = postSerializer(posts, many=True, context={"request":request}).data
            return Response(data=serializer_data)
        except Exception as e:
            return Response("user not found")

        