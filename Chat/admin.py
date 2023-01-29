from django.contrib import admin
from .models import RoomChat


@admin.register(RoomChat)
class RoomChatAdmin(admin.ModelAdmin):
    list_display = ("creator", "companion", "date")
