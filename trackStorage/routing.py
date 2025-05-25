from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/predict/(?P<trip_uid>[^/]+)/$', consumers.TransportConsumer.as_asgi()),
]