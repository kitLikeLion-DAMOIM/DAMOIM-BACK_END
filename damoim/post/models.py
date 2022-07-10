from datetime import date
from django.db import models
from django.conf import settings

class Post(models.Model):
    title =models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title