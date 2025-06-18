from django.shortcuts import render

# Create your views here.
def book_list(req):
    return render (req, 'books/book_list.html')

def book_form(req):
    return render (req, 'books/book_form.html')

def book_confirm_delete(req):
    return render (req, 'books/book_confirm_delete.html')