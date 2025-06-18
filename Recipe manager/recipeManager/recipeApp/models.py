from django.db import models

# Create your models here.
class recipeModel(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=100)
    ingredients = models.TextField(max_length=100)
    instructions = models.TextField(max_length=100)
    image = models.ImageField(upload_to="media/photos")