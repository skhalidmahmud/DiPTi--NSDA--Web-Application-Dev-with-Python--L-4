from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    department = models.TextField(max_length=400)
    student_image = models.ImageField(upload_to='static/img')
    created_at = models.DateTimeField(auto_now=True)

class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    status = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)