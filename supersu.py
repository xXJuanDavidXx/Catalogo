import os
import django
from django.conf import settings
from django.contrib.auth.models import User

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalogo.settings')  # Cambia 'miProyecto.settings' por el nombre de tu módulo de configuración
django.setup()

# Crea el usuario
user = User.objects.create_user(
    username='thegame',
    email='thegame@thegame.com',
    password='thegame123'
)

# Asigna permisos de superusuario y miembro del personal
user.is_superuser = True
user.is_staff = True
user.save()
