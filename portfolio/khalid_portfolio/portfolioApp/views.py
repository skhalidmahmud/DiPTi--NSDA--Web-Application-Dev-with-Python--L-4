from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required

def signUp(request):
    if request.method == 'POST':
        form = customUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('logIn')
    else:
        form = customUserForm()
    context = {'form': form}
    return render(request, 'signUp.html', context)

def logIn(req):
    if req.method=='POST':
        customUser = customUserModel.objects.filter(username=req.POST.get('username')).exists()
        if customUser:
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
def index(req):
    return render(req, 'index.html')

@login_required()
def updateProfiles(request):
    portfolio = get_object_or_404(portfolioModel, user=request.user)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('index')  # or any page you want
    else:
        form = PortfolioForm(instance=portfolio)

    return render(request, 'updateProfiles.html', {'form': form})