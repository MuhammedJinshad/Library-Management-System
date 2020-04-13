from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.

'''
class customeUser(AbstractUser):
    usertype = models.CharField(max_length=200)
    user = models.ForeignKey(User.on_delete=models.CASCADE)'''