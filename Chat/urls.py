from django.urls import path
from .views import RoomChatView, MessageView

urlpatterns = [
    path('rooms/', RoomChatView.as_view(), name='rooms_chat'),
    path('dialog/', MessageView.as_view(), name='dialog_chat'),

]
