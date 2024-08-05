from django.contrib.auth.models import User
import os
import django
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')  # Cambia esto si es necesario
django.setup()




# Crea el usuario
user = User.objects.create_superuser(
    username='thegame',
    email='thegame@thegame.com',
    password='thegame123'
    )
user.save()
