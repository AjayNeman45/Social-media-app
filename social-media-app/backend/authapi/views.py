from functools import partial
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from userinfoapi.models import userProfile
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser

class RegisterPage(APIView):
    def get(self, request):
        NotesList = User.objects.all()
        serializer = UserSerializer(NotesList, many=True)
        return Response({'status' : 200, 'payload' : serializer.data})
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status' : 403, 'error' : serializer.errors,  'messgae' : "Data is invalid"})

        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        userProfille_object = userProfile.objects.create(user=user);
        userProfille_object.save()
        return Response({'status' : 200, "message": "Your Data is added successfully"})

class LoginPage(APIView):
    
    def post(self, request):
        try:
            user_obj = User.objects.get(username =  request.data['username'])
            if user_obj.check_password(request.data['password']):
                token = Token.objects.get(user=user_obj)
                serializer = UserSerializer(user_obj)
                return Response({'status' : 200 ,'token' : str(token), 'user_id': serializer.data['id'], 'message' : "Loged in successfully"})
            return Response({'status':403 , 'message' : "Wrong password"})
        except Exception as e:
            return Response({'status':404 , 'message' : "User dosen't exist with username "+request.data['username']})




        