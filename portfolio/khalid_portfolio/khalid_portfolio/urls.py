from django.contrib import admin
from django.urls import path
from portfolioApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),

    path('signUp/', signUp, name='signUp'),
    path('logIn/', logIn, name='logIn'),
    path('logOut/', logOut, name='logOut'),
    
    path('updateProfiles/', updateProfiles, name='updateProfiles'),
]
