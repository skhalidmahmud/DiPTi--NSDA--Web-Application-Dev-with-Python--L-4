from django.shortcuts import render, re
from myApp.models import *

def home(request):
    return render(request, 'home.html')

def addStudent(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        city = request.POST.get('city')
        age = request.POST.get('age')

        new_student = student(
            name = name,
            dept = dept,
            city = city,
            age = age
        )

        new_student.save()
        return render(request, 'addStudent.html')

    return render(request, 'addStudent.html')

def studentList(request):
    return render(request, 'studentList.html')