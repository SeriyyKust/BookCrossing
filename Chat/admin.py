from django.contrib import admin
from .models import RoomChat, Chat


@admin.register(RoomChat)
class RoomChatAdmin(admin.ModelAdmin):
    list_display = ("creator", "companion", "date")


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "text", "date")