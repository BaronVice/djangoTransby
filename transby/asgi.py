import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from trackStorage.middleware import WebSocketAuthMiddleware
import trackStorage.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transby.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": WebSocketAuthMiddleware(
        URLRouter(
            trackStorage.routing.websocket_urlpatterns
        )
    ),
})
