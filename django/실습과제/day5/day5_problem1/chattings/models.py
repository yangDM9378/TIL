from django.db import models

# Create your models here.
class Chat(models.Model):
    user=models.CharField(max_length=10)
    content=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    