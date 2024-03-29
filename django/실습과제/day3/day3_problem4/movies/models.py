from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50)
    genre=models.CharField(max_length=10)
    director=models.CharField(max_length=20, default='Unknown')

    def __str__(self):
        return f'{self.id}번글 - {self.title} : ({self.genre})'



# Movie.objects.all().order_by('-id')
# Movie.objects.filter(title__endswith='e')
# Movie.objects.filter(genre='action')