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



