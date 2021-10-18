from django.db import models
from django.contrib.auth.models import User
from django.db.models import base
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)
    posted_image = models.ImageField()
    about_post = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "post number {}".format(self.id)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Post id - {} , like by - {} ".format(self.post.id,self.user.id)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Post id - {} , comment by - {} ".format(self.post.id,self.user.id)

