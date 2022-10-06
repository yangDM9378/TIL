from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    title=models.CharField(max_length=200)
    issue_a=models.CharField(max_length=100)
    issue_b=models.CharField(max_length=100)

class Comment(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    acc=((True,'RED TEAM'),(False,'BLUE TEAM'))
    pick=models.BooleanField(choices=acc)
    content=models.CharField(max_length=100)