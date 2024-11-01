# productoApp/forms.py

from django import forms
from productoApp.models import Productos, Distribuidor, Factura
class FormProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['distribuidor', 'factura', 'nombreProducto', 'descripcion', 'categoria', 'denominacionOrigen', 'cantidadProducto']

class FormDistribuidor(forms.ModelForm):
    class Meta:
        model = Distribuidor
        fields = ['telefono', 'email', 'fechaDespacho', 'fechaRecepcion', 'ciudad']

class FormFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['iva', 'fechaFacturacion', 'totalApagar', 'descuentoTotal']
