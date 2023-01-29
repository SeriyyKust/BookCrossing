from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RoomChat
from .serializers import RoomChatSerializers


class RoomChatView(APIView):
    """
    Комнаты чата
    """
    def get(self, request):
        room_chats = RoomChat.objects.all()
        serializer = RoomChatSerializers(room_chats, many=True)
        return Response(serializer.data)
