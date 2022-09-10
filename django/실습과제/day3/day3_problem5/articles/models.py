from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=15)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    memo=models.TextField(default="")
    def __str__(self):
        return f'{self.id}번글-{self.title}:{self.content}/{self.memo}'