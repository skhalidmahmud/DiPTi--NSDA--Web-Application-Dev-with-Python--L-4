from django.contrib import admin
from django.urls import path
from reviewProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='Home'),
    path('AddStudent/', AddStudent,name='AddStudent'),
    path('StudentList', StudentList,name='StudentList'),
    path('AddTeacher/', AddTeacher,name='AddTeacher'),
    path('TeacherList/', TeacherList,name='TeacherList'),
    path('CourseList/', CourseList,name='CourseList'),
    path('AddCourse/', AddCourse,name='AddCourse'),
    path('DeleteStudent/<int:id>/', DeleteStudent,name='DeleteStudent'),
    path('DeleteTeacher/<int:id>/', DeleteTeacher,name='DeleteTeacher'),
    path('DeleteCourse/<int:id>/', DeleteCourse,name='DeleteCourse'),
    path('EditStudent/<int:id>/', EditStudent,name='EditStudent'),

]

