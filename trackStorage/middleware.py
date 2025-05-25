from django.http import HttpResponseForbidden
from django.conf import settings
from channels.middleware import BaseMiddleware

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip for non-API endpoints
        if not request.path.startswith('/api/'):
            return self.get_response(request)
            
        api_key = request.headers.get('X-API-KEY')
        app_package = request.headers.get('X-APP-PACKAGE')
        
        if not api_key or not app_package:
            return HttpResponseForbidden("Missing authentication headers")
            
        if settings.ANDROID_APP_API_KEYS.get(app_package) != api_key:
            return HttpResponseForbidden("Invalid API key or app package")
            
        return self.get_response(request)


class WebSocketAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # Only process WebSocket connections
        if scope['type'] != 'websocket':
            return await super().__call__(scope, receive, send)

        # Extract headers (convert from bytes to string)
        headers = dict(scope['headers'])
        api_key = headers.get(b'x-api-key', b'').decode()
        app_package = headers.get(b'x-app-package', b'').decode()

        # Validate
        if not api_key or not app_package:
            await send({
                'type': 'websocket.close',
                'code': 4003,  # Custom forbidden code
                'reason': 'Missing auth headers'
            })
            return

        if settings.ANDROID_APP_API_KEYS.get(app_package) != api_key:
            await send({
                'type': 'websocket.close',
                'code': 4003,
                'reason': 'Invalid credentials'
            })
            return

        # Add auth info to the scope if needed
        # scope['auth'] = {
        #     'app_package': app_package,
        #     'api_key': api_key
        # }
        # 

        return await super().__call__(scope, receive, send)