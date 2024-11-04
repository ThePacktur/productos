from django.contrib import admin
from productoApp.models import Productos, Distribuidor, Factura

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto','descripcion', 'categoria', 'denominacionOrigen', 'cantidadProducto' ]

class DistribuidorAdmin(admin.ModelAdmin):
    list_display = ['telefono', 'email', 'ciudad', 'fechaDespacho', 'fechaRecepcion']
    
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['fechaFacturacion', 'precioUnitario', 'iva', 'descuentoTotal', 'totalApagar']
    
# Register your models here.
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Factura, FacturaAdmin)