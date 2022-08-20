import profile
from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    catspecies = models.CharField(max_length=128)
    catnumber = models.IntegerField(blank=True)
    catimage = models.ImageField(upload_to='profile/', default='default.png')
    userimage = models.ImageField(upload_to='profile/', default='default.png')

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    text = models.TextField(max_length=2000, blank=True)


