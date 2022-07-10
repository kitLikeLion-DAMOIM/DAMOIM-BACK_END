from csv import writer
from pyexpat import model
from django.db import models

class Comment(models.Model):
    writer = models.CharField(max_length=10)
    contents = models.TextField()
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.writer