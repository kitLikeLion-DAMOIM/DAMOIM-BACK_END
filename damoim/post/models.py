from django.db import models
from django.conf import settings
from group.models import Group

class Post(models.Model):
    title =models.CharField(max_length=100)
    group_id = models.ForeignKey("group.Group",related_name="group", on_delete=models.CASCADE, db_column="group_id",default="")
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title