from django.db import models
from django.contrib.auth.models import AbstractUser

class customUserModel(AbstractUser):
    USERTYPE = [
        ('job_seeker','Job Seeker'),
        ('recruiter','Recruiter')
    ]
    userTypes = models.CharField(choices = USERTYPE, max_length = 100, null = True)

class  jobPosts(models.Model):
    user =  models.ForeignKey(customUserModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 100, null = True)
    description = models.TextField(null = True)
    salary = models.IntegerField(null = True)
    location = models.CharField(max_length = 100, null = True)
    deadline = models.DateField(null = True)