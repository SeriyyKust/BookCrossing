from rest_framework import serializers
from .models import RoomChat, Chat
from django.contrib.auth.models import User


class UserRoomChatSerializer(serializers.ModelSerializer):
    """
    Сериализация участника чата
    """

    class Meta:
        model = User
        fields = ("id", "username")


class RoomChatGetSerializer(serializers.ModelSerializer):
    """
    Сериализация комнат чата (GET)
    """
    creator = UserRoomChatSerializer()
    companion = UserRoomChatSerializer()

    class Meta:
        model = RoomChat
        fields = ("creator", "companion", "date")


class RoomChatPostSerializer(serializers.ModelSerializer):
    """
    Сериализация комнат чата (POST)
    """

    class Meta:
        model = RoomChat
        fields = ("creator", "companion")


class ChatGetSerializer(serializers.ModelSerializer):
    """
    Сериализация сообщения чата
    """
    user = UserRoomChatSerializer()

    class Meta:
        model = Chat
        fields = ("user", "text", "date")


class ChatPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ("room", "text")
