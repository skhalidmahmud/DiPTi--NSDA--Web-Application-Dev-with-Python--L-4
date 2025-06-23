from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

def news(req):
    news = newsModel.objects.all()
    return render(req, 'news/news.html', {'news': news})

@login_required(login_url="/Login/")
def deleteNews(req, id):
    delete = newsModel.objects.get(id=id).delete()
    return redirect('news_home')

def viewNews(req, id):
    view = newsModel.objects.get(id=id)
    context={
        'news': view
    }
    return render(req, 'news/view_news.html', context)

@login_required(login_url="/Login/")
def addNews(req):
    if req.method == 'POST':
        Title = req.POST.get('title')
        Content = req.POST.get('content')
        ThumbnailImage = req.FILES.get('thumbnailImage')
        PublishedDate = req.POST.get('publishedDate')
        
        news = newsModel(
            title = Title,
            authorName = req.user.username,
            content = Content,
            thumbnailImage = ThumbnailImage,
            publishedDate = PublishedDate,
        )
        news.save()
        return redirect('news_home')
    return render(req, 'news/addnews.html')

@login_required(login_url="/Login/")
def editNews(req, id):
    edit = newsModel.objects.get(id=id)
    context={
        'news': edit
    }
    if req.method == 'POST':
        edit.Title = req.POST.get('title')
        edit.AuthorName = req.POST.get('authorName')
        edit.Content = req.POST.get('content')
        if req.FILES.get('thumbnailImage'):
            edit.ThumbnailImage = req.FILES.get('thumbnailImage')
        edit.PublishedDate = req.POST.get('publishedDate')
        
        edit.save()
        return redirect('news_home')
    return render(req, 'news/edit_news.html', context)