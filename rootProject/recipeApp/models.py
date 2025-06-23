from django.db import models

class recipeModel(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=400)
    instructions = models.TextField(max_length=400)
    recipeImage = models.ImageField(upload_to='static/recipe/')
    creator = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    createAt = models.DateTimeField(auto_now_add=True)