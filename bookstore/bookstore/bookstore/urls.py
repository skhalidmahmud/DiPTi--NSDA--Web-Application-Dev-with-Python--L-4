from django.contrib import admin
from django.urls import path
from bookstore.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name="bookList"),
    path('book_form/', book_form, name="bookForm"),
    path('book_confirm_delete', book_confirm_delete, name="bookConfirmDelete")
]