from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Book(models.Model):
    cover_img = models.TextField(null=True)
    title = models.CharField(max_length=200, null=True)
    author_name = models.CharField(max_length=200, null=True)
    genre = models.CharField(max_length=200, null=True)
    page_count = models.IntegerField(null = True)
    isbn = models.CharField(max_length=128, null=True)
    rating = models.FloatField(null = True)
