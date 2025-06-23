from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', recipe, name='recipe'),
    path('addRecipe/', addRecipe, name='addRecipe'),
    path('view_recipe/<int:id>', view_recipe, name='view_recipe'),
    path('edit_recipe/<int:id>', edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:id>', delete_recipe, name='delete_recipe'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)