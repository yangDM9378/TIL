from django.contrib import admin
from .models import Actor, Movie, Review

# Register your models here.
admin.register(Actor)
admin.register(Movie)
admin.register(Review)