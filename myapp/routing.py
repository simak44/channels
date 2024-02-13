from django.urls import path
from myapp import consumers
websocket_urls=[
    path('ws/sc/', consumers.MySynConsumer.as_asgi()),
]