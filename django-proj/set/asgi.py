"""
ASGI config for set project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

# ******************************************************************************
#  Copyright (c) 2021 Nurul-GC.                                                *
# ******************************************************************************

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'set.settings')

application = get_asgi_application()
