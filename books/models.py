from django.db import models

# Create your models here.

class Book_category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        db_table = 'book_category'

    def __str__(self):
        return f'{self.name}'

class Author(models.Model):
    name = models.CharField(max_length=100,blank=True)
    surname = models.CharField(max_length=100,blank=True)
    year=models.CharField(max_length=100,blank=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.name} {self.surname}'
    

    

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    category=models.ForeignKey(Book_category,on_delete=models.CASCADE)
    description=models.CharField(max_length=100,blank=True)
    price=models.CharField(max_length=128,blank=True)
    year=models.CharField(max_length=100,blank=True)
    image=models.ImageField(upload_to='books/',blank=True,null=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return f'{self.name}'
    
class Review(models.Model):
    comment = models.TextField(max_length=256,blank=True)
    star_given = models.CharField(max_length=10,blank=True)
    user = models.CharField(max_length=100,blank=True)
    bookname=models.ForeignKey(to=Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return self.comment