from django.contrib import admin
from .models import Genre, PhotoBook, Book, StateCategory


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title", )


@admin.register(PhotoBook)
class PhotoBookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "book")
    list_display_links = ("id", )
    list_editable = ("title", "image", "book")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "author", "owner", "state", "genre", "cover")
    list_display_links = ("id", )
    list_editable = ("title", "description", "author", "owner", "state", "genre", "cover")


@admin.register(StateCategory)
class StateCategory(admin.ModelAdmin):
    list_display = ("title", )
