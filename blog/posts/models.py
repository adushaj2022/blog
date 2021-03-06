from django.db import models
from user.models import UserProfile


class Post(models.Model):
    description = models.CharField(max_length=225)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    creator = models.ForeignKey(
        UserProfile, related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
