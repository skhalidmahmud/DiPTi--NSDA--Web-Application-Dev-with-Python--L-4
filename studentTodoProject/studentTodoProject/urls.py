from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('studentSignUp/', studentSignUp, name='studentSignUp'),
    path('studentLogin/', studentLogin, name='studentLogin'),
    path('logOutStudent/', logOutStudent, name='logOutStudent'),
    path('addToDo/', addToDo, name='addToDo'),
    path('deleteToDo/<int:Todoid>', deleteToDo, name='deleteToDo'),
    path('editTodo/<int:Todoid>', editTodo, name='editTodo'),
    path('studentList/', studentList, name='studentList'),
]
