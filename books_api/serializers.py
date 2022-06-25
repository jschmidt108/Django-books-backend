from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'cover_img', 'title', 'author_name', 'genre', 'page_count', 'isbn', 'rating',)



