from django.db import models
from books_api.models import Book
# from reviews_api.models import Review
from django.contrib.postgres.fields import JSONField

# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    hasRead = models.ManyToManyField(Book, related_name='books_read', blank=True)
    isReading = models.ManyToManyField(Book, related_name='books_reading', blank=True)
    toRead = models.ManyToManyField(Book, related_name='books_wantToRead', blank=True)
    # userReviews = models.ManyToManyField(Review)



