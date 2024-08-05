from django.contrib.auth.models import User

# Crea el usuario
user = User.objects.create_superuser(
    username='thegame',
    email='thegame@thegame.com',
    password='thegame123'

user.save()
