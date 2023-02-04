from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user_id", "birthday", "photo", "rating")
    list_display_links = ("user_id", )
    list_editable = ("birthday", "photo", "rating")
