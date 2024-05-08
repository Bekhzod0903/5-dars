from django.contrib import admin
from .models import Book_category,Author, Review ,Book
# Register your models here.

admin.site.register(Book)
admin.site.register(Book_category)
admin.site.register(Author)
admin.site.register(Review)