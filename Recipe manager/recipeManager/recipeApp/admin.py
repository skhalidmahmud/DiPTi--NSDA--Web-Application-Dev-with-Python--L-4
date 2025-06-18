from django.contrib import admin

# Register your models here.
from .models import recipeModel

admin.site.register(recipeModel)