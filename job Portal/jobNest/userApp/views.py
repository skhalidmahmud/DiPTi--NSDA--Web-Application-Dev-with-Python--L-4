from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required 

@login_required(login_url='logIn')
def index(req):
    return render(req, 'index.html')

def signUp(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        userTypes = req.POST.get('userTypes')
        password = req.POST.get('password')
        confurmPassword = req.POST.get('confirm_password')
        
        if password == confurmPassword:
            user = customUserModel.objects.create_user(
                username = username,
                email = email,
                password = password,
                userTypes = userTypes
                )
            return redirect('logIn')
    return render(req, 'signUp.html')

def logIn(req):
    if req.method=='POST':
        Username = req.POST.get('username')
        Password = req.POST.get('password')
        
        user = authenticate(req, username=Username, password=Password)
        
        if user is not None:
            login(req, user)
            return redirect('index')
        
    return render(req, 'logIn.html')

@login_required(login_url='logIn')
def logOut(req):
    logout(req)
    return redirect('logIn')

@login_required(login_url='logIn')
def changePassword(req):
    if req.method=='POST':
        oldPassword = req.POST.get('oldPassword')
        newPassword = req.POST.get('newPassword')
        confirmPassword = req.POST.get('confirmPassword')
        if newPassword == confirmPassword:
            if req.user.check_password(oldPassword):
                req.user.set_password(newPassword)
                req.user.save()
                logout(req)
                return redirect('logIn')
    return render(req, 'changePassword.html')

@login_required(login_url='logIn')
def addNewJob(req):
    if req.method=='POST':
        title = req.POST.get('title')
        description = req.POST.get('description')
        salary = req.POST.get('salary')
        location = req.POST.get('location')
        deadline = req.POST.get('deadline')

        data = jobPosts(
            user=req.user,
            title=title,
            description=description,
            salary=salary,
            location=location,
            deadline=deadline
        )
        data.save()
        return redirect ('index')
    return render(req, 'addNewJob.html')

@login_required(login_url='logIn')
def jobList(req):
    data = jobPosts.objects.filter(user=req.user)
    context={
        'data':data
    }
    return render(req,"jobList.html",context)

@login_required(login_url='logIn')
def delete(req, id):
    data = jobPosts.objects.get(id=id).delete()
    return redirect ('jobList')

@login_required(login_url='logIn')
def views(req,id):
    data = jobPosts.objects.get(id=id)
    context={
        'data':data
    }
    return render(req,"views.html", context)

@login_required(login_url='logIn')
def update(req,id):
    data=jobPosts.objects.get(id=id)
    context={
        'data':data
    }
    if req.method=='POST':
        data.id=id
        data.title=req.POST.get('title')
        data.description=req.POST.get('description')
        data.status=req.POST.get('status')
        data.created_at=req.POST.get('created_at')
        data.updated_at=req.POST.get('updated_at')

        data.save()
        return redirect ('jobList')

    return render(req,"update.html",context)