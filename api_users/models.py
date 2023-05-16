from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=254)
    contrasenia = models.CharField(max_length=254)
    numero = models.CharField(max_length=20)
    domicilio = models.TextField()

    