from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import RoomChat, Message
from .serializers import RoomChatGetSerializer, RoomChatPostSerializer, MessagePostSerializer, MessageGetSerializer
from rest_framework import permissions
from django.db.models import Q
from .permissions import OwnerRoomPermission
from rest_framework.response import Response
from rest_framework import status


class RoomChatView(ListCreateAPIView, DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = RoomChatGetSerializer

    def get_queryset(self):
        return RoomChat.objects.filter(Q(creator=self.request.user) | Q(companion=self.request.user))

    def create(self, request, *args, **kwargs):
        serializer = RoomChatPostSerializer(data=request.POST)
        if serializer.is_valid():
            new_companion = serializer.validated_data['companion']
            companions = [room.companion for room in RoomChat.objects.filter(Q(creator=self.request.user))]
            creators = [room.creator for room in RoomChat.objects.filter(Q(companion=self.request.user))]
            if new_companion in companions or new_companion in creators:
                return Response("This room already exists", status=status.HTTP_400_BAD_REQUEST)
            serializer.save(creator=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated & OwnerRoomPermission]
    serializer_class = MessageGetSerializer

    def get_queryset(self):
        return Message.objects.filter(room=self.request.GET.get("room"))

    def create(self, request, *args, **kwargs):
        serializer = MessagePostSerializer(data=request.POST)
        if serializer.is_valid():
            room = serializer.validated_data['room']
            rooms = [room for room in RoomChat.objects.filter(Q(creator=self.request.user) |
                                                                 Q(companion=self.request.user))]
            if room not in rooms:
                return Response("The user is not a participant in this dialog.", status=status.HTTP_400_BAD_REQUEST)
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
