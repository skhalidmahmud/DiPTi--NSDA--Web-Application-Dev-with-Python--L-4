from django.contrib import admin
from django.urls import path
from ResumeApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('editCV/<int:id>', editCV, name="editCV"),
    path('deleteCV/<int:id>', deleteCV, name="deleteCV"),
    path('viewCV/<int:id>', viewCV, name="viewCV"),
    path('addUser/',addUser,name="addUser")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)