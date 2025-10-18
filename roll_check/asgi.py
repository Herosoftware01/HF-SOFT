"""
ASGI config for roll_check project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roll_check.settings')

# application = get_asgi_application()





# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roll_check.settings')

# import django
# django.setup()

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.core.asgi import get_asgi_application

# from welcome.routing import websocket_urlpatterns

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(websocket_urlpatterns)
#     ),
# })


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roll_check.settings')
django.setup()  # ✅ MUST come before importing Django-dependent code

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import welcome.routing  # ✅ safe to import after django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            welcome.routing.websocket_urlpatterns
        )
    ),
})


