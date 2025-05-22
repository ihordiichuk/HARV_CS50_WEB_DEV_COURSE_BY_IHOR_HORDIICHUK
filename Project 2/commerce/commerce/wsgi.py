"""
WSGI config for commerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set default settings module for WSGI-compatible web servers
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'commerce.settings')

# Get the WSGI application callable for deployment
application = get_wsgi_application()
