from django.urls import path
from .views import RoomChatView

urlpatterns = [
    path('room/', RoomChatView.as_view(), name='rooms_chat'),
]
