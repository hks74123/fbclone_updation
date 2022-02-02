"""
ASGI config for fbclone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbclone.settings')

import hksfbclone.routing
from channels.auth import AuthMiddlewareStack
 
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack( 
        URLRouter(
        hksfbclone.routing.websocket_urlpatterns
    )
    ),
})
