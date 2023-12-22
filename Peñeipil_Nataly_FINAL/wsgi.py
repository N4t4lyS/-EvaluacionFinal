"""
WSGI config for Peñeipil_Nataly_FINAL project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Peñeipil_Nataly_FINAL.settings')

application = get_wsgi_application()
