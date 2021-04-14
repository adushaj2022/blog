from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
from django import template


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='uploads/', blank=True, null=True, default='uploads/default.png')

    def __str__(self):
        return self.user.username

    def post_count(self):
        posts = apps.get_model('posts', 'Post')
        return posts.objects.filter(creator_id=self.id).count()

    def follower_count(self):
        relationships = apps.get_model('user', 'Relationship')
        return relationships.objects.filter(following=self).count()

    def followee_count(self):
        relationships = apps.get_model('user', 'Relationship')
        return relationships.objects.filter(followee=self).count()

    def does_follow(self, fid):
        relationships = apps.get_model('user', 'Relationship')
        if relationships.objects.filter(followee=self, following_id=fid).count() == 1:
            return True
        else:
            return False

    num_of_followers = property(follower_count)
    num_of_followees = property(followee_count)
    num_of_posts = property(post_count)


class Relationship(models.Model):
    followee = models.ForeignKey(
        UserProfile, related_name='followee', on_delete=models.CASCADE)
    following = models.ForeignKey(
        UserProfile, related_name='following', on_delete=models.CASCADE)
