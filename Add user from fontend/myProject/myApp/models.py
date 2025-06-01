from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.IntegerField()