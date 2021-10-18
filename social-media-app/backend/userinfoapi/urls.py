from django.urls import path
from .views import *

urlpatterns = [
    path("", userProfileView.as_view()),
    path("activity/", activityView.as_view()),
    path("update_profile/", updateUserProfile.as_view()),
    path("update/", updateUser.as_view())
]
