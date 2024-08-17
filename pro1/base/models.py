from django.db import models
from django.utils import timezone

# Create your models here.
class registration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.IntegerField()

    def __str__(self):
        return self.username

class login(models.Model):
     email = models.EmailField(max_length=200)
     password = models.CharField(max_length=20)

class Todo(models.Model):
     title = models.CharField(max_length=100)
     details = models.CharField(max_length=300)
     date = models.DateTimeField(default=timezone.now)

     def __str__(self):
        return self.title
