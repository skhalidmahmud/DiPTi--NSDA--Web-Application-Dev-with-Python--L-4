from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('SignUp/',SignUp, name='SignUp'),
    path('Login/',Login, name='Login'),
    path('logOut/', logOut, name='logOut'),
    path('recipe/', include('recipeApp.urls')),
    path('newsPortal/', include('newsPortalAPP.urls')),
]
urlpatterns+=re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
urlpatterns+=re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),