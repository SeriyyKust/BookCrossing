from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
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

    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ("user", "birthday", "photo", "rating")


class ProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализация допольнительной информации о пользователе (PATCH)
    """

    class Meta:
        model = Profile
        fields = ("birthday", "photo")

    def update(self, instance, validated_data):
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance
