from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=600)
    precio = models.PositiveIntegerField(50)

    def __str__(self):
        return self.nombre