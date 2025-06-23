from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from studentApp.models import ToDoModel

def studentSignUp(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')
        
        if password == confirm_password:
            student = User.objects.create_user(username, email, password)
            student.save()
            return redirect('studentLogin')
        
    return render(req, 'studentSignUp.html')

def studentLogin(req):
    if req.method=='POST':
        Username = req.POST.get('username')
        Password = req.POST.get('password')
        
        user = authenticate(req, username=Username, password=Password)
        
        if user is not None:
            login(req, user)
            return redirect('index')
    
    return render(req, 'studentLogin.html')

def logOutStudent(req):
    logout(req)
    return redirect('studentLogin')

@login_required(login_url="/studentLogin/")
def index(req):
    toDoList = ToDoModel.objects.all()
    context={
        'tasks' : toDoList
    }
    return render(req, 'index.html', context)

@login_required(login_url="/studentLogin/")
def addToDo(req):
    if req.method == 'POST':
        Title = req.POST.get('title')
        Description = req.POST.get('description')
        Status = req.POST.get('status')
        Due_date = req.POST.get('due_date')
        
        newToDo = ToDoModel(
            title = Title,
            description = Description,
            status = Status,
            due_date = Due_date
        )
        newToDo.save()
        return redirect('index')
        
    return render(req, 'addToDo.html')

@login_required(login_url="/studentLogin/")
def deleteToDo(req, Todoid):
    deleteTodo = ToDoModel.objects.get(id=Todoid).delete()
    return redirect('index')

@login_required(login_url="/studentLogin/")
def editTodo(req, Todoid):
    toDoList = ToDoModel.objects.get(id=Todoid)
    context={
        'task' : toDoList
    }
    
    if req.method == 'POST':
        toDoList.title = req.POST.get('title')
        toDoList.description = req.POST.get('description')
        toDoList.status = req.POST.get('status')
        toDoList.due_date = req.POST.get('due_date')
        
        toDoList.save()
        return redirect('index')
    return render(req, 'editTodo.html', context)

@login_required(login_url="/studentLogin/")
def studentList(req):
    return render(req, 'studentList.html')