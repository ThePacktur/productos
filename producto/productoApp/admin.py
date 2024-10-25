from django.contrib import admin
from productoApp.models import Productos

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombreProducto','descripcion', 'categoria', 'denominacionOrigen', 'cantidadProducto' ]

# Register your models here.
admin.site.register(Productos, ProductosAdmin)

