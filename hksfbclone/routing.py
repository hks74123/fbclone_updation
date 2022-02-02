from django.urls import path
from . import consumers
websocket_urlpatterns=[
    path('ws/sc/<str:groupname>/',consumers.MyASyncConsumer.as_asgi()),
]