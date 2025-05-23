from django.urls import re_path
from .consumers import PongConsumer

websocket_urlpatterns = [
    # ws://host/ws/pong/<uuid>/
    re_path(r'^ws/pong/(?P<game_id>[0-9a-f-]+)/$', PongConsumer.as_asgi()),
]

