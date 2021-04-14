
from django.db import models
from blog.posts.models import Post
from blog.user.models import UserProfile


class Comment(models.Model):
    body = models.CharField(max_length=225)
    creator = models.ForeignKey(
        UserProfile, related_name='profile', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
