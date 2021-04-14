
from django.db import models
from posts.models import Post
from user.models import UserProfile


class Comment(models.Model):
    body = models.CharField(max_length=225)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
