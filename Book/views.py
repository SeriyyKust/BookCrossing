from rest_framework import viewsets
from .serializers import BookSerializer, PhotoBookSerializer
from .utils import OwnerPermissionMixin, BookManager, PhotoManager
from rest_framework.response import Response


class BookViewSet(OwnerPermissionMixin, viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        # Get without param or Get with param: state or/and genre
        return BookManager.get_queryset(self.request.GET)

    def create(self, request, *args, **kwargs):
        context = BookManager.create_new_objects(request)
        return Response(context["data"], status=context["status"])


class PhotoBookViewSet(OwnerPermissionMixin, viewsets.ModelViewSet):
    serializer_class = PhotoBookSerializer

    def get_queryset(self):
        # Get without param or Get with param: book_id
        return PhotoManager.get_queryset(self.request.GET)

    def create(self, request, *args, **kwargs):
        context = PhotoManager.create_new_objects(request)
        return Response(context["data"], status=context["status"])
