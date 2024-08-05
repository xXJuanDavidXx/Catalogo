import os
import django
from django.core.management import call_command

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')  # Cambia esto si es necesario
django.setup()

# Ejecuta el comando `createsuperuser` con opciones proporcionadas
call_command(
    'createsuperuser',
    username='thegame',
    email='thegame@thegame.com',
    password='thegame123',
    interactive=False
)

