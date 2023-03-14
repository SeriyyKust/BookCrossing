from django.contrib import admin
from .models import RoomChat, Message


@admin.register(RoomChat)
class RoomChatAdmin(admin.ModelAdmin):
    list_display = ("id", "creator", "companion", "date")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "room", "user", "text", "date")