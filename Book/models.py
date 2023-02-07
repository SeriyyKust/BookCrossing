from django.db import models
from django.contrib.auth.models import User


class StateCategory(models.Model):
    title = models.CharField(max_length=16, primary_key=True, verbose_name="Название состояния")

    class Meta:
        verbose_name = "Состояние книги"
        verbose_name_plural = "Состояния книг"

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=64, primary_key=True, verbose_name="Название жанра")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.title[:16]


class Book(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    description = models.CharField(max_length=9192, null=True, blank=True, verbose_name="Описание")
    author = models.CharField(max_length=1024, verbose_name="Автор")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    state = models.ForeignKey(StateCategory, on_delete=models.PROTECT, null=True, blank=True,
                              verbose_name="Состояние книги")
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Жанр")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title[:16]


def get_name_image(instance, filename):
    return "/".join(["books", str(instance.book.owner.username), filename])


class PhotoBook(models.Model):
    title = models.CharField(max_length=128, verbose_name="Название")
    image = models.ImageField(upload_to=get_name_image, verbose_name="Образ")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")

    class Meta:
        verbose_name = "Фото книги"
        verbose_name_plural = "Фото книг"

    def __str__(self):
        return self.title[:16]
