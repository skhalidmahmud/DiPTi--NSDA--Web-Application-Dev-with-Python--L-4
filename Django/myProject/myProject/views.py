from django.shortcuts import render

def homePage(req):
    return render(req, 'homePage.html')

def contact(req):
    return render(req, 'contact.html')

def portfolio(req):
    return render(req, 'portfolio.html')