from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class FollowerModel(models.Model):
    
    follower = models.ForeignKey(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    picture = models.URLField(null=True,blank=True)
    is_favorite = models.BooleanField(default=False)
    