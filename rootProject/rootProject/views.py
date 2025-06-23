from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(req):
    return render(req, 'index.html')

def SignUp(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password1')
        confirm_password = req.POST.get('password2')
        
        if password == confirm_password:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('Login')
    return render(req, 'SignUp.html')

def Login(req):
    if req.method=='POST':
        Username = req.POST.get('username')
        Password = req.POST.get('password')
        
        user = authenticate(req, username=Username, password=Password)
        
        if user is not None:
            login(req, user)
            return redirect('index')
        
    return render(req, 'Login.html')

def logOut(req):
    logout(req)
    return redirect('index')