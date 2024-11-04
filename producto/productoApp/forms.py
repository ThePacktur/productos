# productoApp/forms.py

from django import forms
from productoApp.models import Productos, Distribuidor, Factura
class FormProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
class FormDistribuidor(forms.ModelForm):
    class Meta:
        model = Distribuidor
        fields = '__all__'
        widgets = {
            'fechaDespacho': forms.DateInput(attrs={'type': 'date'}),
            'fechaRecepcion': forms.DateInput(attrs={'type': 'date'}),
        }
class FormFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        widgets = {
            'fechaFacturacion': forms.DateInput(attrs={'type': 'date'}),
        }