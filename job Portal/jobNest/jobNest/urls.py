from django.contrib import admin
from django.urls import path
from userApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('signUp/',signUp,name='signUp'),
    path('logIn/',logIn,name='logIn'),
    path('logOut/',logOut,name='logOut'),
    path('changePassword/', changePassword, name='changePassword'),
    path('addNewJob/', addNewJob, name='addNewJob'),
    path('jobList/', jobList, name='jobList'),

    path('views/<int:id>',views,name='views'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)