from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movies(models.Model):
    movie_title= models.CharField(max_length=100)
    movie_poster= models.URLField(max_length=256)

class Ratings(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(to=Movies, on_delete=models.CASCADE)
    rating = models.IntegerField()

