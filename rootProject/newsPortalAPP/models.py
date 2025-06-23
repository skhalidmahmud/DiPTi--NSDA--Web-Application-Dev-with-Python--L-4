from django.db import models

class newsModel(models.Model):
    title = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    thumbnailImage = models.ImageField(upload_to='static/news/')
    publishedDate = models.DateTimeField()