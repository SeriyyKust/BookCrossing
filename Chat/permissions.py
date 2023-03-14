from rest_framework import permissions
from .models import RoomChat
from django.db.models import Q


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


class OwnerRoomPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        room = get_or_none(RoomChat, pk=request.GET.get('room', None))
        rooms = [room for room in RoomChat.objects.filter(Q(creator=request.user) |
                                                          Q(companion=request.user))]
        if room in rooms:
            return True
        else:
            return False
