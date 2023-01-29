from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RoomChat, Chat
from .serializers import RoomChatGetSerializer, RoomChatPostSerializer, ChatGetSerializer, ChatPostSerializer
from rest_framework import status
from rest_framework import permissions
from django.db.models import Q


class RoomChatView(APIView):
    """
    Комнаты чатов
    """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room_chats = RoomChat.objects.filter(Q(creator=request.user) | Q(companion=request.user))
        serializer = RoomChatGetSerializer(room_chats, many=True)
        return Response({"rooms": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        room = RoomChatPostSerializer(data={"creator": request.user.id, "companion": request.POST.get("companion_id")})
        if room.is_valid():
            room.save()
            return Response({"room": room.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(room.errors, status=status.HTTP_400_BAD_REQUEST)


class DialogView(APIView):
    """
    Сообщения комнаты чата
    """

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        room = RoomChat.objects.get(pk=request.GET.get("room"))
        print(room)
        if request.user == room.creator or request.user == room.companion:
            chat = Chat.objects.filter(room=room)
            serializer = ChatGetSerializer(chat, many=True)
            return Response({"messages": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"Errors": "The user is not a member of this chat."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        room = RoomChat.objects.get(pk=request.GET.get("room"))
        if request.user == room.creator or request.user == room.companion:
            dialog = ChatPostSerializer(data=request.POST)
            if dialog.is_valid():
                dialog.save(user=request.user)
                return Response({"message": dialog.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(dialog.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Errors": "The user is not a member of this chat."}, status=status.HTTP_400_BAD_REQUEST)
