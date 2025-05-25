from django.contrib import admin
from django.urls import path

from myProject.views import homePage, contact, portfolio
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    
    
]