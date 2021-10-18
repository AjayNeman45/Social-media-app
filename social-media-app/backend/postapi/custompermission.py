from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class tokenCheck(BasePermission):
    def has_permission(self, request, view):
        auth_token = request.META['HTTP_AUTHORIZATION']
        auth_token = auth_token[9:-9]
        try:
            user = User.objects.get(auth_token = auth_token)
            if(user):
                return True
            return False
        except Exception as e:
            print(e)
            return False