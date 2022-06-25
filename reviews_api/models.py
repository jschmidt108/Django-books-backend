from django.db import models
from auth_api.models import UserAccount
from books_api.models import Book

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Review(models.Model):
    review = models.TextField()
    review_by_user = models.ForeignKey(UserAccount, null=True, on_delete=models.SET_NULL)
    review_for_book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
