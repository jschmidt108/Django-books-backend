from rest_framework import serializers
from .models import UserAccount
from books_api.serializers import BookSerializer
# from reviews_api.serializers import ReviewSerializer


### ALLOWS YOU TO CREATE AND CHECK PASSWORDS
from django.contrib.auth.hashers import make_password, check_password



class UserAccountSerializer(serializers.ModelSerializer):
    hasRead = BookSerializer(many=True)
    isReading = BookSerializer(many=True)
    toRead = BookSerializer(many=True)
    # userReviews = ReviewSerializer(many=True)
    class Meta:
        model = UserAccount
        fields = ('id', 'name', 'username', 'email', 'password', 'hasRead', 'isReading', 'toRead')
        #fields = ('id', 'name', 'username', 'email', 'password', 'hasRead', 'isReading', 'toRead', 'userReviews')

    ### THIS HASHES A NEW USERS PASSWORD WHEN THEY CREATE AN ACCOUNT
    def create(self, validated_data):
        user = UserAccount.objects.create(
        name=validated_data['name'],
        username=validated_data['username'],
        email=validated_data['email'],
        hasRead=validated_data['hasRead'],
        isReading=validated_data['isReading'],
        toRead=validated_data['toRead'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    ### THIS MAKES SURE THEIR UPDATED PASSWORDS ARE ALSO HASHED
    def update(self,instance, validated_data):
        user = UserAccount.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user