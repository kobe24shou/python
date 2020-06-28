from django.db import models

# Create your models here.



class UserInfo(models.Model):

#下面是创建了一张空表
    username=models.CharField(max_length=64)
    sex=models.CharField(max_length=64)
    email=models.CharField(max_length=64)