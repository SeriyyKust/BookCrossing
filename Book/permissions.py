from rest_framework import permissions


class OwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True if obj.owner == request.user else False
