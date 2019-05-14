"""
models
"""
from django.db import models


# Create your models here.
class Post(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)