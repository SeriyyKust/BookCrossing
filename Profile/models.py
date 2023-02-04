from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def get_name_photo_file(instance, filename):
    return "/".join(["user_photos", str(instance.user_id), filename])


class Profile(models.Model):
    """
    Additional information about the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата Рождения")
    photo = models.ImageField(null=True, blank=True, upload_to=get_name_photo_file, verbose_name="Фото")
    rating = models.FloatField(max_length=5.0, default=0.0, verbose_name="Рейтинг")

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
