from django import forms
from productoApp.models import Productos, Distribuidor

class FormProducto(forms.ModelForm):
    
    class Meta:
        model = Productos 
        fields = ('idDistribuidor',  'nombreProducto', 'descripcion', 'categoria', 'denominacionOrigen', 'cantidadProducto')

class FormDistribuidor(forms.ModelForm):

    class Meta:
        model = Distribuidor
        fields = ('idProducto', 'telefono', 'Email', 'fechaDespacho', 'fechaRecepcion', 'cuidad')
        
        