from rest_framework import permissions


class OwnerProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True if obj.user == request.user else False