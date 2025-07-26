from django.contrib import admin
from django.urls import path
from authApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard_admin/', dashboard_admin, name='dashboard_admin'),
    path('dashboard_employee/', dashboard_employee, name='dashboard_employee'),
    path('signUp/', signUp, name='signUp'),
    path('logIn/', logIn, name='logIn'),
    path('logOut/', logOut, name='logOut'),
    path('addEmployee/', addEmployee, name='addEmployee'),
    path('allEmployee/', allEmployee, name='allEmployee'),
    path('viewemployer/<int:id>', viewemployer, name='viewemployer'),
    # path('updateemployer/<int:id>', updateemployer, name='updateemployer'),
    path('deleteemployer/<int:id>', deleteemployer, name='deleteemployer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)