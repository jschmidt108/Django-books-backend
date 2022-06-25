from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

import json
from django.http import JsonResponse


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer



