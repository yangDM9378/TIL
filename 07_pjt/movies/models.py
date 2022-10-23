from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)
# 더미 데이터가 actors 받아오게 만들어져있어서...
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='mo')

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
