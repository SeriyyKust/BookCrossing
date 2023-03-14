from rest_framework import permissions
from .permissions import OwnerPermission
from .models import Book, PhotoBook
from .serializers import BookSerializer, PhotoBookSerializer
from rest_framework import status


class OwnerPermissionMixin:
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            permission_classes = [permissions.IsAuthenticated & OwnerPermission]
        else:
            permission_classes = [permissions.IsAuthenticated]
        #return [permission() for permission in permission_classes]
        return [permission() for permission in [OwnerPermission, ]]


class Manager:

    @staticmethod
    def _create_new_objects_from_serializer(request, serializer):
        """
        Checks for validity and that the owner is correct, then creates the object.
        :param request:
        :param serializer:
        :return: context (The dictionary contains information about the serialized data and the status.)
        """
        context = {}
        if serializer.is_valid():
            if serializer.validated_data['owner'] == request.user:
                serializer.save()
                context["data"] = serializer.data
                context["status"] = status.HTTP_201_CREATED
            else:
                context["data"] = {"owner": "The owner of the book must be the sender of the create request."}
                context["status"] = status.HTTP_400_BAD_REQUEST
        else:
            context["data"] = serializer.errors
            context["status"] = status.HTTP_400_BAD_REQUEST
        return context


class BookManager(Manager):

    @staticmethod
    def get_queryset(param):
        objects = Book.objects.all()
        # State
        state = param.get("state", None)
        if state is not None:
            objects = objects.filter(state=state)
        # Genre
        genre = param.get("genre", None)
        if genre is not None:
            objects = objects.filter(genre=genre)
        return objects

    @staticmethod
    def create_new_objects(request):
        """
        Checks for validity and that the owner is correct, then creates the object.
        :param request:
        :return: context (The dictionary contains information about the serialized data and the status.)
        """
        context = {}
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
            if serializer.validated_data['owner'] == request.user:
                serializer.save()
                context["data"] = serializer.data
                context["status"] = status.HTTP_201_CREATED
            else:
                context["data"] = {"owner": "The owner of the book must be the sender of the create request."}
                context["status"] = status.HTTP_400_BAD_REQUEST
        else:
            context["data"] = serializer.errors
            context["status"] = status.HTTP_400_BAD_REQUEST
        return context


class PhotoManager(Manager):

    @staticmethod
    def get_queryset(param):
        objects = PhotoBook.objects.all()
        # Book
        book_id = param.get("book_id", None)
        if book_id is not None:
            objects = objects.filter(book=book_id)
        return objects

    @staticmethod
    def create_new_objects(request):
        """
        Checks for validity and that the owner is correct, then creates the object.
        :param request:
        :return: context (The dictionary contains information about the serialized data and the status.)
        """
        context = {}
        serializer = PhotoBookSerializer(data=request.data)
        if serializer.is_valid():
            owner = serializer.validated_data['book'].owner
            if owner == request.user:
                serializer.save()
                context["data"] = serializer.data
                context["status"] = status.HTTP_201_CREATED
            else:
                context["data"] = {"owner": "The owner of the book must be the sender of the create request."}
                context["status"] = status.HTTP_400_BAD_REQUEST
        else:
            context["data"] = serializer.errors
            context["status"] = status.HTTP_400_BAD_REQUEST
        return context
