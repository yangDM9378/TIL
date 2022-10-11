from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField,ImageSpecField

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    synopsis = models.TextField()
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200,200)]
    )
    img_thumbnail=models.ImageField(blank=True)
    image_thumbnail=ImageSpecField(
        source='img_thumbnail',
        processors=[Thumbnail(100,100)],
        options={'quality':90},

    )