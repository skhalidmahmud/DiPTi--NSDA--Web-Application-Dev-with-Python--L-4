from django.shortcuts import render, redirect

# for Authenticaton
from django.contrib.auth import authenticate, login, logout
from myApp.models import *
from django.contrib.auth.decorators import login_required 

def index(req):
    return render(req, 'index.html')

# [Done] Authenticaton (sign up, log in, log out) [Worked]
def signUp(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        userTypes = req.POST.get('userTypes')
        password = req.POST.get('password')
        confurmPassword = req.POST.get('confurmPassword')
        # Add OR delete from custom user model
        
        if password == confurmPassword:
            user = customUserModel.objects.create_user(
                username = username,
                email = email,
                password = password,
                userTypes = userTypes, # Add OR delete from custom user model
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

# [Done] change password [Worked]
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

# [Done] CRUD [Worked]
def addToDo(req):
    if req.method=='POST':
        title = req.POST.get('title')
        description = req.POST.get('description')
        status = req.POST.get('status')
        # Created_at, Updated_at and OneToOne/ForanKey ekhane lagbe na

        data = toDoModel(
            title=title,
            description=description,
            status=status,
            # for OneToOne/ForanKey
            user = req.user
            # if data user er theke na niye amra dite chai [only for Admin type]
            user = 'admin' or password = '123456789' # emn kore likhe dite hobe

            # created_at, updated_at jodi thake to auto hoye jabe, ekhane lagbe na
        )
        data.save()
        return redirect ('listToDo')
    return render(req,"addToDo.html")

def listToDo(req):
    # jodi bole dey: just student list dekhao
    relativeName = customUserModel.objects.filter(userType='Student')
    
    # jodi bole dey: all dekhao
    relativeName = toDoModel.objects.all()

    # jodi bole dey: just 'status' "pending" dekhao
    relativeName = toDoModel.objects.filter(status='pending')

    # jodi bole dey: jei user login korche, tar add kora data dekhao [like FB post]
    relativeName = toDoModel.objects.filter(user=req.user)

    # jodi bole dey: ekhadhik condition thake to 'and' user korle hobe
    relativeName = toDoModel.objects.filter(userType='Student' and status='pending') # if er oita er moto

    context={
        'relativeName':relativeName
    }
    return render(req,"listToDo.html",context)

def deleteToDo(req, id):
    data = toDoModel.objects.get(id=id).delete()
    return redirect ('listToDo')

def viewsToDo(req,id):
    data = toDoModel.objects.get(id=id)
    context={
        'data':data
    }
    return render(req,"viewsToDo.html", context)

def updateToDo(req,id):
    data=toDoModel.objects.get(id=id)
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
        return redirect ('listToDo')

    return render(req,"updateToDo.html",context)

# [ ] forgate password - [done hoy ni]
def sendMail(req):
    userMail = 'forusetmp@gmail.com'
    send_mail(
        'Send Mail',
        'Hello there, this is a test mail.' \
        'Dont warry about this.',
        settings.EMAIL_HOST_USER,
        [userMail]
    )
    return redirect('sendMailPage')

def sendMailPage(req):
    return render(req, 'sendMailPage.html')

def forgatePass(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        user = User.objects.get(email=email)
        otp = random.randint(100000, 999999)
        cache.add(email, otp, timeout=60)

        # cache.set(email, otp, timeout=60)  # Use this if you want to overwrite existing OTP
        
        send_mail(
            'OTP for Password Reset',
            f'Your OTP is {otp}',
            settings.EMAIL_HOST_USER,
            [email]
        )

        return render(req, 'otpVerification.html')
    return render(req, 'forgatePass.html')