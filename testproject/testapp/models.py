from django.db import models

# Create your models here.

class Post(models.Model):
    owner_email = models.CharField(max_length=100,default="")
    concert_name = models.CharField(max_length=100,default="")
    singer = models.CharField(max_length=100,default="")
    concert_date = models.IntegerField()
    post_date = models.IntegerField()
    