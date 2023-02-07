from rest_framework import permissions
from rest_framework import generics
from .models import Profile
from .serializers import ProfileGetSerializer
from .permissions import OwnerProfilePermission


class ProfileViewSet(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Profile
    serializer_class = ProfileGetSerializer

    def get_permissions(self):
        if self.request.method in ('PATCH', 'PUT'):
            permission_classes = [permissions.IsAuthenticated & OwnerProfilePermission]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
