from django.shortcuts import render

from storeApp.models import *

def home(request):
    return render(request, 'home.html')

def books(request):
    booksData = Book.objects.all()
    context = {
        'books': booksData
    }
    return render(request, 'books.html', context)

def user(request):
    usersData = User.objects.all()
    context = {
        'users': usersData
    }
    return render(request, 'user.html', context)
