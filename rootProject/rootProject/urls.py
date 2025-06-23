from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('SignUp/',SignUp, name='SignUp'),
    path('Login/',Login, name='Login'),
    path('logOut/', logOut, name='logOut'),
    path('recipe/', include('recipeApp.urls')),
    path('newsPortal/', include('newsPortalAPP.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)