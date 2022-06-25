from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import ReviewSerializer
from .models import Review
import json
from django.http import JsonResponse


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer


