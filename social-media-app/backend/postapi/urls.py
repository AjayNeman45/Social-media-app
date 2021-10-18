from django.urls import path
from .views import *

urlpatterns = [
    path('all_posts/', allPosts.as_view()),
    path('user_posts/<username>', userPosts.as_view()),
    path('add_post/', addPost.as_view()),
    path('like_post/<pk>/', likePost.as_view()),
    path('comment_post/', commentPosts.as_view()),
    path('all_comments/<int:pk>', allComments.as_view()),
]