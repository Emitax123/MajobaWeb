# routing.py

from django.urls import path
from .consumers import ModelUpdatesConsumer

websocket_urlpatterns = [
    path("ws/", ModelUpdatesConsumer.as_asgi()),
]
