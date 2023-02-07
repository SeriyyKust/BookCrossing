from rest_framework import permissions


class OwnerBookPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True if obj.owner == request.user else False
