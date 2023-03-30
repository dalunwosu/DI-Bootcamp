import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikestore.settings')
import django
django.setup()

from films.models import Poster
import requests

