from django.db import models

# Create your models here.
class book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    BookCategory = models.CharField(max_length=100)
    PublishDate = models.DateField()
    Description = models.TextField(max_length=100)