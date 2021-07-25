from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HireeInfo(models.Model):

    full_name=models.CharField(max_length=30,default="")
    profile_pic = models.ImageField(upload_to='profile')
    Phone_numb=models.CharField(max_length=12,default="")
    Area=models.CharField(max_length=30,default="")
    City = models.CharField(max_length=30, default="")
    pincode = models.CharField(max_length=15, default="")
    gender=models.CharField(max_length=10,default="")
    person=models.ForeignKey(User,default=None,on_delete=models.CASCADE)



    def __str__(self):
        return self.full_name

class HireeSkills(models.Model):
    hiree_skills=models.CharField(max_length=30,default="")
    hiree_exp=models.IntegerField()
    hiree_charge=models.CharField(max_length=20,default="")
    hiree_AvalArea=models.CharField(max_length=30,default="")
    hiree_AvalTime = models.CharField(max_length=30, default="")
    hiree_other=models.CharField(max_length=30,default="")
    person=models.ForeignKey(User,default=None,on_delete=models.CASCADE)





    def __str__(self):
        return self.hiree_skills


