from django.db import models

# Create your models here.

class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True)
    idDistribuidor = models.ForeignKey('Distribuidor', on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    categoria = models.CharField(max_length=50)
    denominacionOrigen = models.CharField(max_length=50)
    cantidadProducto = models.IntegerField(max_length=15)

    def __str__(self):
        return  f'Producto: {self.idProducto}'
   
class Distribuidor(models.Model):
    idDistribuidor = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    ciudad = models.CharField(max_length=15)
    fechaDespacho = models.DateField()
    fechaRecepcion = models.DateField()

    def __str__(self):
        return f'Distribuidor: {self.idDistribuidor}'

class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True)
    fechaFacturacion = models.DateField()
    precioUnitario = models.FloatField()
    iva = models.FloatField()
    descuentoTotal = models.FloatField()

    def __str__(self):
        return f'Factura: {self.idFactura}'
    
