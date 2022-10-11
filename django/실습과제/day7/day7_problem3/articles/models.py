from email.mime import image
from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True)
    image_thumbnail=ImageSpecField(
        source='image',
        processors=[Thumbnail(100,100)],
        options={'quality':90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    