from django.urls import path
from .views import get_info,get_authors,get_books,get_reviews

urlpatterns = [
    path('', get_info,name='get_info'),
    path('books/<int:pk>', get_books,name='get_books'),
    path('authors/<int:pk>/', get_authors,name='get_authors'),
]
