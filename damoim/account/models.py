from django.db import models

class Account(models.Model):
    user_id= models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name= models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    phonenumber= models.CharField(max_length=20)

    def __str__(self):
        return self.user_id

