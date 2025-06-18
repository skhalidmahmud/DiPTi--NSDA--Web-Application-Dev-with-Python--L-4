from django.shortcuts import render, redirect
from ResumeApp.models import *

# Create your views here.
def home(req):
    data=ResumeModel.objects.all()
    return render(req, "home.html", {'data': data})

def editCV(req, id):
    return render(req, "editCV.html")

def deleteCV(req, id):
    data = ResumeModel.objects.get(id=id).delete()
    return redirect("home")

def viewCV(req, id):
    data = ResumeModel.objects.get(id=id)
    return render(req, "viewCV.html", {'data': data})

def addUser(req):
    if req.method=='POST':
        user = ResumeModel(
            name = req.POST.get("name"),
            image = req.POST.get("image"),
            email = req.POST.get("email"),
            phone = req.POST.get("phone"),
            adress = req.POST.get("adress"),
            summary = req.POST.get("summary"),
            Degree = req.POST.get("Degree"),
            institute = req.POST.get("institute"),
            yearOfGraduation = req.POST.get("yearOfGraduation"),
            companyName = req.POST.get("companyName"),
            position = req.POST.get("position"),
            yearOfExperience = req.POST.get("yearOfExperience"),
            skills = req.POST.get("skills"),
            hobbies = req.POST.get("hobbies"),
            achievements = req.POST.get("achievements"),
        )
        user.save()
        return redirect('home')
    return render(req, "addUser.html")