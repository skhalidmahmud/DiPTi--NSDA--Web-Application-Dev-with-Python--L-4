from django.db import models

class bookModel(models.Model):
    title = models.CharField(max_length=100)
    authorName = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    bookImage = models.ImageField(upload_to='static/book/')
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)