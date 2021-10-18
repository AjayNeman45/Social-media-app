from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterPage.as_view()),
    path('login/', LoginPage.as_view()),
]
