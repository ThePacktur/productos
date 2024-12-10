from django import forms
from productoApp.models import Productos, Distribuidor, Factura
from django.core.exceptions import ValidationError

class FormProducto(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombreProducto', 'descripcion', 'categoria', 'denominacionOrigen', 'cantidadProducto', 'distribuidores', 'facturas']
        widgets = {
            'nombreProducto': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'denominacionOrigen': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'cantidadProducto': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required'}),
            'distribuidores': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'facturas': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }


class FormDistribuidor(forms.ModelForm):
    class Meta:
        model = Distribuidor
        fields = '__all__'
        widgets = {
            'fechaDespacho': forms.DateInput(attrs={'type': 'date'}),
            'fechaRecepcion': forms.DateInput(attrs={'type': 'date'}),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de Teléfono',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo Electrónico',
                'required': 'required'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad',
                'required': 'required'
            }),
            'fechaDespacho': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fechaRecepcion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise ValidationError('El número de teléfono debe contener solo dígitos.')
        if len(telefono) != 10:
            raise ValidationError('El número de teléfono debe tener exactamente 10 dígitos.')
        return telefono

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Distribuidor.objects.filter(email=email).exists():
            raise forms.ValidationError(('Este correo electrónico ya está en uso.'))
        return email

    def clean(self):
        super().clean()
        fecha_despacho = self.cleaned_data.get('fechaDespacho')
        fecha_recepcion = self.cleaned_data.get('fechaRecepcion')
        if fecha_despacho and fecha_recepcion and fecha_despacho > fecha_recepcion:
            self.add_error('fechaRecepcion', 'La fecha de recepción debe ser igual o posterior a la fecha de despacho.')


class FormFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        widgets = {
           
            'fechaFacturacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'precioUnitario': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio Unitario',
                'required': 'required'
            }),
            'iva': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'IVA (%)',
                'required': 'required'
            }),
            'descuentoTotal': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descuento Total',
                'required': 'required'
            }),
        }
    def clean(self):
        super().clean()
        fecha_facturacion = self.cleaned_data.get('fechaFacturacion')
        fecha_despacho = None
        distribuidor_id = self.cleaned_data.get('distribuidor_id')

        # Verificar si hay un distribuidor relacionado para obtener su fecha de despacho
        if distribuidor_id:
            distribuidor = Distribuidor.objects.filter(id=distribuidor_id).first()
            if distribuidor:
                fecha_despacho = distribuidor.fechaDespacho

        if fecha_facturacion and fecha_despacho:
            if fecha_facturacion < fecha_despacho:
                self.add_error('fechaFacturacion', 'La fecha de facturación no puede ser anterior a la fecha de despacho.')

        # Validar relación entre envío y facturación
        fecha_recepcion = None
        if distribuidor_id:
            fecha_recepcion = distribuidor.fechaRecepcion

        if fecha_recepcion and fecha_facturacion and fecha_recepcion < fecha_facturacion:
            self.add_error('fechaFacturacion', 'La fecha de facturación debe ser anterior o igual a la fecha de recepción.')