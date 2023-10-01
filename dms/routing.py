from django.urls import path
from .consumers import RoomConsumer

websocket_urlpatterns = [
    path('wss/chat/<str:slug>/', RoomConsumer.as_asgi()),
    # path('ws/chat/yy/', RoomConsumer.as_asgi())
]