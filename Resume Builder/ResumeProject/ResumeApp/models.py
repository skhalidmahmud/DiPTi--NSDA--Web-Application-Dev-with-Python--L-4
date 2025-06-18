from django.db import models

# Create your models here.
class  ResumeModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/img')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    adress = models.TextField(max_length=100)
    summary = models.TextField(max_length=100)
    Degree = models.CharField(max_length=30)
    institute = models.CharField(max_length=100)
    yearOfGraduation = models.IntegerField()
    companyName = models.CharField(max_length=100)
    position = models.CharField(max_length=30)
    yearOfExperience = models.CharField(max_length=10)
    skills = models.TextField(max_length=100)
    hobbies = models.TextField(max_length=100)
    achievements = models.TextField(max_length=100)