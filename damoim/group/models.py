from django.db import models

class Group(models.Model):
    group_category=models.CharField(max_length=50,null=True)
    logo = models.TextField()
    group_name = models.CharField(max_length=50)
    profile_link = models.TextField()
    location = models.CharField(max_length=100)
    detail = models.TextField()

    def __str__(self):
        return self.group_name