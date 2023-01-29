from django.urls import path
from .views import RoomChatView, DialogView

urlpatterns = [
    path('rooms/', RoomChatView.as_view(), name='rooms_chat'),
    path('dialog/', DialogView.as_view(), name='dialog_chat'),

]
