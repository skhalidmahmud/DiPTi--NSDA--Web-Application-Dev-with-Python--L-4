from django.db import models

class StudentModel(models.Model):
    Student_Name=models.CharField(max_length=100)
    Department_Name=models.CharField(max_length=150)
    City_Name=models.CharField(max_length=100)
    Student_Age=models.IntegerField()


class TeacherModel(models.Model):
    Teacher_Name=models.CharField(max_length=100)
    Department_Name=models.CharField(max_length=150)
    Email=models.EmailField()
    Designation=models.CharField(max_length=150)


class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=100)
    Course_Number=models.IntegerField()
    Course_Credit=models.IntegerField()
    Course_Duration=models.IntegerField()
    




    

