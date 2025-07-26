from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from authApp.models import *
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

@login_required(login_url='logIn')
def index(req):
    return render(req, 'index.html')

@login_required(login_url='logIn')
def dashboard_admin(req):
    return render(req, 'dashboard_admin.html')

@login_required(login_url='logIn')
def dashboard_employee(req):
    return render(req, 'dashboard_employee.html')

def signUp(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        password1 = req.POST.get('password1')        
        password2 = req.POST.get('password2')
        
        usernameis = customUserModel.objects.filter(username=req.POST.get('username')).exists()
        if usernameis:
            messages.error(req, 'Username already exists')
            return render(req, 'signUp.html')
        else:
            if password1 == password2:
                user = customUserModel.objects.create_user(
                    username = username,
                    email = email,
                    phone = phone,
                    password = password1,
                    userTypes = 'Admin',
                    )
                return redirect('logIn')

    return render(req, 'signUp.html')

def logIn(req):
    if req.method=='POST':
        customUser = customUserModel.objects.filter(username=req.POST.get('username')).exists()
        if customUser:
            Username = req.POST.get('username')
            Password = req.POST.get('password')
            
            user = authenticate(req, username=Username, password=Password)
            
            if user is not None:
                login(req,user)
                data = customUserModel.objects.get(username=Username)
                if data.userTypes == 'Admin':
                    return redirect('dashboard_admin')
                else:
                    return redirect('dashboard_employee')
        else:
            messages.error(req, 'Username do not exists or Password incurrect')
            return render(req, 'logIn.html')
        
    return render(req, 'logIn.html')

@login_required(login_url='logIn')
def logOut(req):
    logout(req)
    return redirect('logIn')

@login_required(login_url='logIn')
def addEmployee(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')
        departmentName = req.POST.get('departmentName')
        departmentDescription = req.POST.get('departmentDescription')
        fullName = req.POST.get('fullName')
        position = req.POST.get('position')
        dateofjoining = req.POST.get('depardateofjoiningtmentDescription')
        profilePicture = req.FILES.get('profilePicture')
        
        usernameis = customUserModel.objects.filter(username=req.POST.get('username')).exists()
        if usernameis:
            messages.error(req, 'Username already exists')
            return render(req, 'addEmployee.html')
        else:
            if password1 == password2:
                User = customUserModel.objects.create_user(
                    username = username,
                    email = email,
                    phone = phone,
                    password = password1,
                    userTypes = 'Employee',
                    )
                department = departmentModel.objects.create(
                    name = departmentName,
                    description = departmentDescription
                    )
                employerProfile = employerProfileModel.objects.create(
                    employerUser = User,
                    fullName = fullName,
                    department = department,
                    position = position,
                    dateofjoining = dateofjoining,
                    profilePicture = profilePicture
                )
                return redirect('dashboard_admin')    
    return render(req, 'addEmployee.html')

def allEmployee(req):
    data = employerProfileModel.objects.all()
    context = {
        'data':data
    }
    return render(req, 'allEmployee.html', context)

def deleteemployer(req, id):
    employerProfile = employerProfileModel.objects.get(id=id)
    id2 = employerProfile.employerUser.id
    User = customUserModel.objects.get(id=id2).delete()
    return redirect('allEmployee')

def viewemployer(req, id):
    employerProfile = employerProfileModel.objects.get(id=id)
    context = {
        'data':employerProfile
    }
    return render(req, 'viewemployer.html', context)