from django.db import models
from django.contrib.auth.models import User


# Create your models here.


from django.db import models

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.nombre


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Campo para el número de teléfono

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.phone_number and not self.phone_number.startswith('57'):
            self.phone_number = '57' + self.phone_number
        super().save(*args, **kwargs)
