from rest_framework import serializers
from .models import Review

from auth_api.serializers import UserAccountSerializer
from books_api.serializers import BookSerializer


class ReviewSerializer(serializers.ModelSerializer):
    review_by_user = UserAccountSerializer()
    review_for_book = BookSerializer()
    class Meta:
        model = Review
        fields = ('id', 'review', 'review_by_user', 'review_for_book')

