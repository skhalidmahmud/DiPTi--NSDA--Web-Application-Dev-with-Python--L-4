from django.contrib.auth.models import AbstractUser
from django.db import models

class customUserModel(AbstractUser):
    USERTYPE = [
        ('Admin','Admin'),
        ('Employee','Employee')
    ]
    phone = models.CharField(max_length = 100, null = True)
    userTypes = models.CharField(choices = USERTYPE, max_length = 100, null = True)

class departmentModel(models.Model):
    name = models.CharField(max_length = 50, null = True)
    description = models.TextField(null = True)

class employerProfileModel(models.Model):
    employerUser = models.OneToOneField(customUserModel, on_delete = models.CASCADE, null = True)
    fullName = models.CharField(max_length = 50, null = True)
    department = models.ForeignKey(departmentModel, on_delete = models.CASCADE, null = True)
    position = models.TextField(null = True)
    dateofjoining = models.DateField(null=True)
    profilePicture = models.ImageField(upload_to='static/img/DP', null = True)