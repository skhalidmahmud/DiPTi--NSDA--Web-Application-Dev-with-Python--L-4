from django.shortcuts import render
from recipeApp.models import recipeModel
# Create your views here.
def home(req):
    recipe = recipeModel.objects.all()
    return render(req, "home.html", context={"data":recipe})

def AddRecipe(req):
    return render(req, "AddRecipe.html")