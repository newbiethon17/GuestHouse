from django.db import models

# Create your models here.

class Post(models.Model):
    owner_email = models.CharField(max_length=1000,default="")
    owner_number = models.IntegerField(default=0)
    concert_name = models.CharField(max_length=1000,default="")
    singer = models.CharField(max_length=1000,default="")
    concert_date = models.IntegerField(default=0)
    post_date = models.IntegerField(default=0)
    pwd = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    description = models.CharField(max_length=1000,default="")
    