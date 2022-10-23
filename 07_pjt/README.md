### 07_pjt
# DB 설계를 활용한  REST API 설계
## 개발 도구 및 환경세팅
### Models.py
```python
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
```
- Actor/Movie/Review model에 준비된 데이터 넣기
```bash
$ python manage.py loaddata movies/actors.json movies/movies.json movies/reviews.json
```
- 문제 발생
데이터를 넣을때 ManyToMany field를 Actor에서 Movie 참조하게 만들경우 더비 데이터 자체가 actors로 받아오게 만들어져 오류가 발생한다.

## serializer.py
```python
from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields ='__all__'

class ActorSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields ='__all__'

class MovielistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieSerializer(serializers.ModelSerializer):
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    actors=ActorSerializer(many=True, read_only=True)
    
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content',)
    review_set=ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    movie=MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'



class ReviewlistSerializer(serializers.ModelSerializer):
    movie=MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
```
- serializer을 재정의하여 원하는 필드 가져오기