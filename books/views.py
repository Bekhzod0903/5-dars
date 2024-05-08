from django.shortcuts import render
from .models import Book_category,Author, Review ,Book
from .form import ProductForm
# Create your views here.

def get_info(request):
    categoriess = Book_category.objects.all()
    context = {
        'categories': categoriess
    }
    return render(request, 'index.html', context=context)

def get_reviews(request):
    review = Review.objects.all()
    context = {
       'reviews': review
    }
    return render(request, 'index.html', context=context)


def get_books(request, pk):
    book = Book.objects.get(category=pk)
    context = {
        'books': book
    }
    return render(request, 'books.html', context=context)

def get_authors(request, pk):
    authors = Author.objects.get(pk=pk)
    context = {
        'author': authors
    }
    return render(request, 'author.html', context=context)