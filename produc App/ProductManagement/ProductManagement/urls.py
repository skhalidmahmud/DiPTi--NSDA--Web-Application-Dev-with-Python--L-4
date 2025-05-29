from django.contrib import admin
from django.urls import path

from ProductManagement.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
