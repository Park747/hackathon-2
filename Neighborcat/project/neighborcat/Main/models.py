from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from User.models import Profile


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='post_profile')
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField()
    numberview = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post/', default='default.png')
    likes = models.ManyToManyField(User, blank=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
