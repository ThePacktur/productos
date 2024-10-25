from django.db import models

# Create your models here.

class Productos(models.Model):
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    denominacionOrigen = models.CharField(max_length=50)
    cantidadProducto = models.IntegerField(max_length=15)
    email = models.CharField(max_length=50)