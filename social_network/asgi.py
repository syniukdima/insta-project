import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

from chats.consumers import PersonalChatConsumer
from our_post.consumers import CommentConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_network.settings')

django_asgi_app = get_asgi_application()

# записуємо url для різних websocket
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
                path('ws/comment/<int:id>/', CommentConsumer.as_asgi()),
            ]))
    )
})
