from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from .utils import ManagerProfile


class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request):
        pk = request.GET.get("id", None)
        manager_profile = ManagerProfile(pk)
        return Response({"profiles": manager_profile.get_serializer_data()}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        manager_profile = ManagerProfile(pk)
        if not manager_profile.has_object():
            return Response({"Errors": "There is no user with this id."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"profile": manager_profile.get_serializer_data()}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        manager_profile = ManagerProfile(pk)
        if not manager_profile.has_object():
            return Response({"Errors": "There is no user with this id."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = manager_profile.update(request.data)
            data_status = data.pop("status")
            if data_status:
                return Response({"profile": data}, status=status.HTTP_200_OK)
            else:
                return Response(data, status=status.HTTP_400_BAD_REQUEST)