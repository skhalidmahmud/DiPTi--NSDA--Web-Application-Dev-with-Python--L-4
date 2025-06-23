from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

def recipe(req):
    newRecipe = recipeModel.objects.all()
    context={
        'recipes': newRecipe
    }
    return render(req, 'recipe/recipe.html', context)

@login_required(login_url="/Login/")
def addRecipe(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        ingredients = req.POST.get('ingredients')
        instructions = req.POST.get('instructions')
        recipeImage = req.FILES.get('recipeImage')
        creator = req.POST.get('creator')
        description = req.POST.get('description')
        
        newRecipe = recipeModel(
            name = name,
            ingredients = ingredients,
            instructions = instructions,
            recipeImage = recipeImage,
            creator = creator,
            description = description 
        )
        newRecipe.save()
        return redirect('recipe')
    return render(req, 'recipe/addRecipe.html')

def view_recipe(req, id):
    view = recipeModel.objects.get(id=id)
    context={
        'recipes': view
    }
    return render(req, 'recipe/view_recipe.html', context)

@login_required(login_url="/Login/")
def edit_recipe(req, id):
    edit = recipeModel.objects.get(id=id)
    context={
        'recipes': edit
    }
    if req.method == 'POST':
        edit.id = id
        edit.name = req.POST.get('name')
        edit.ingredients = req.POST.get('ingredients')
        edit.instructions = req.POST.get('instructions')
        if req.FILES.get('recipeImage'):
            edit.recipeImage = req.FILES.get('recipeImage')
            
        edit.creator = req.POST.get('creator')
        edit.description = req.POST.get('description')
        
        edit.save()
        return redirect('recipe')
    return render(req, 'recipe/edit_recipe.html', context)

@login_required(login_url="/Login/")
def delete_recipe(req, id):
    delete = recipeModel.objects.get(id=id).delete()
    return redirect('recipe')