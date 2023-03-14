from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализация информации о пользователе
    """
    class Meta:
        model = User
        fields = ("id", "username", "email")


class ProfileGetSerializer(serializers.ModelSerializer):
    """
    Сериализация допольнительной информации о пользователе
    """

    user = CustomUserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ("user", "birthday", "photo", "rating")
