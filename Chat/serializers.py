from rest_framework import serializers
from .models import RoomChat
from django.contrib.auth.models import User


class CreatorRoomChatSerializers(serializers.ModelSerializer):
    """
    Сериализация создателя чата
    """

    class Meta:
        model = User
        fields = ("id", "username")


class CompanionRoomCharSerializer(serializers.ModelSerializer):
    """
    Сериализация собеседника чата
    """

    class Meta:
        model = User
        fields = ("id", "username")


class RoomChatSerializers(serializers.ModelSerializer):
    """
    Сериализация комнат чата
    """
    creator = CreatorRoomChatSerializers()
    companion = CompanionRoomCharSerializer()

    class Meta:
        model = RoomChat
        fields = ("creator", "companion", "date")
