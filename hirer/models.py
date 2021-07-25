from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Data(models.Model):

    full_name=models.CharField(max_length=30,default="")
    profile_pic = models.ImageField(upload_to='temp', default='profile.jpg')


    Phone_numb=models.CharField(max_length=12,default="")
    City = models.CharField(max_length=30, default="")
    skills = models.CharField(max_length=15, default="")
    exp=models.IntegerField()
    charge=models.CharField(max_length=15, default="")

    def __str__(self):
        return self.full_name