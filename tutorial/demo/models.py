from django.db import models

class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

class Book(models.Model):
    title = models.CharField(null=True, blank=False, max_length=36, unique=True, default='')
    description = models.TextField(max_length=256, blank=True)

    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    isPublished = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)

    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE) #prevents assigning the same ISBN to multiple books

    def __str__(self):
       return self.title


class Character(models.Model): #this class must come after the function that returns the title to the Book class
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='authors')
