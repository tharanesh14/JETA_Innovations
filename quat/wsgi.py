"""
WSGI config for quat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quat.settings')

application = get_wsgi_application()

python_version = sys.version
print("Python Runtime Version:", python_version)

# This line is not necessary, as the 'application' variable is already defined above.
# app = application
