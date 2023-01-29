from django.db import models
from django.contrib.auth.models import User


class RoomChat(models.Model):
    """
    Модель комнаты чата
    """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    companion = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Собеседник",
                                  related_name="companion_user")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
    """
    Модель сообщения чата
    """
    room = models.ForeignKey(RoomChat, on_delete=models.CASCADE, verbose_name="Комната чата")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField(max_length=2024, verbose_name="Сообщение")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"
