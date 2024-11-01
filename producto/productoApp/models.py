from django.db import models

# Create your models here.

class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True, default=1)
    distribuidor = models.ForeignKey('Distribuidor', on_delete=models.CASCADE, default=1)
    factura = models.ForeignKey('Factura', on_delete=models.CASCADE, default=1)
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    categoria = models.CharField(max_length=50)
    denominacionOrigen = models.CharField(max_length=50)
    cantidadProducto = models.IntegerField()

    def __str__(self):
        return  f'Producto: {self.idProducto} - {self.nombreProducto}'
   
class Distribuidor(models.Model):
    idDistribuidor = models.AutoField(primary_key=True, default=1)
    #idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    ciudad = models.CharField(max_length=15)
    fechaDespacho = models.DateField()
    fechaRecepcion = models.DateField()

    def __str__(self):
        return f'Distribuidor: {self.idDistribuidor} - {self.ciudad}'

class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True, default=1)
    #idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    fechaFacturacion = models.DateField()
    precioUnitario = models.FloatField(max_length=15)
    iva = models.FloatField(max_length=15)
    descuentoTotal = models.FloatField(max_length=15)
    totalApagar = models.FloatField(max_length=15)

    def __str__(self):
        return f'Factura: {self.idFactura} - Precio Total: {self.totalApagar} '
    
