from django.db import models

# Create your models here.

class Post(models.Model):
    owner_email = models.CharField(max_length=1000,default="")
    owner_number = models.CharField(max_length=1000,default="")
    concert_name = models.CharField(max_length=1000,default="")
    singer = models.CharField(max_length=1000,default="")
    concert_date = models.IntegerField(default=0)
    post_date = models.IntegerField(default=0)
    owner_pwd = models.IntegerField(default=0)
    now_capacity = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    description = models.CharField(max_length=1000,default="")
    

class Member(models.Model):
    chosen_post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.CharField(max_length=1000,default="")
    pwd = models.IntegerField(default=0)
    number = models.CharField(max_length=1000,default="")
    
    