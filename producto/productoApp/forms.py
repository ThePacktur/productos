from django import forms
from productoApp.models import Productos

class FormProducto(forms.ModelForm):
    
    class Meta:
        model = Productos
        fields = '__all__'
        
        