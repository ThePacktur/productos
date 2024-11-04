from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
# Función de validación que verifica si un valor es positivo
def validacion_positivo(value):
    if value < 0:
        raise ValidationError(_('%(value)s debe ser un número positivo.'), params={'value': value},)

class Distribuidor(models.Model):
    idDistribuidor = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    ciudad = models.CharField(max_length=15)
    fechaDespacho = models.DateField()
    fechaRecepcion = models.DateField()

    def clean(self):
        if self.fechaDespacho > self.fechaRecepcion:
            raise ValidationError({
                'fechaRecepcion': _('La fecha de recepción debe ser igual o posterior a la fecha de despacho.')
            })

    def __str__(self):
        return f'Distribuidor: {self.idDistribuidor} - {self.ciudad}'

class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True)
    fechaFacturacion = models.DateField()
    precioUnitario = models.DecimalField(max_digits=15, decimal_places=2, validators=[validacion_positivo])
    iva = models.DecimalField(max_digits=5, decimal_places=2, validators=[validacion_positivo])
    descuentoTotal = models.DecimalField(max_digits=15, decimal_places=2, validators=[validacion_positivo])
    totalApagar = models.DecimalField(max_digits=15, decimal_places=2, validators=[validacion_positivo])

    def clean(self):
        calculo_total = (self.precioUnitario * (1 + self.iva / Decimal('100'))) - self.descuentoTotal
        if self.totalApagar != calculo_total:
            raise ValidationError({
                'totalApagar': _('El total a pagar no coincide con el cálculo total basado en el precio, IVA y descuento.')
            })

    def __str__(self):
        return f'Factura: {self.idFactura} - Precio Total: {self.totalApagar}'

class Productos(models.Model):
    idProducto = models.AutoField(primary_key=True)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    categoria = models.CharField(max_length=50)
    denominacionOrigen = models.CharField(max_length=50)
    cantidadProducto = models.IntegerField(validators=[validacion_positivo])

    def __str__(self):
        return f'Producto: {self.idProducto} - {self.nombreProducto}'
