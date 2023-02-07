from rest_framework import serializers
from .models import Book, PhotoBook


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "title", "description", "author", "owner", "state", "genre")


class PhotoBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoBook
        fields = ("id", "title", "image", "book")
