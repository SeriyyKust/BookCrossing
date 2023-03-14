from rest_framework import serializers
from .models import RoomChat, Message
from django.contrib.auth.models import User
from django.db.models import Q


class UserRoomChatSerializer(serializers.ModelSerializer):
    """
    Сериализация участника чата
    """

    class Meta:
        model = User
        fields = ("id", "username")


class RoomChatGetSerializer(serializers.ModelSerializer):
    """
    (GET)
    """
    creator = UserRoomChatSerializer()
    companion = UserRoomChatSerializer()

    class Meta:
        model = RoomChat
        fields = ("id", "creator", "companion", "date")


class RoomChatPostSerializer(serializers.ModelSerializer):
    """
    (POST)
    """

    class Meta:
        model = RoomChat
        fields = ("companion", )


class MessageGetSerializer(serializers.ModelSerializer):
    """
    (GET)
    """
    user = UserRoomChatSerializer()

    class Meta:
        model = Message
        fields = ("user", "text", "date")


class MessagePostSerializer(serializers.ModelSerializer):
    """
    (POST)
    """

    class Meta:
        model = Message
        fields = ("room", "text")
