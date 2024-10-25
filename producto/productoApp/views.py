from django.shortcuts import render, redirect
from productoApp.models import Productos
from productoApp.forms import FormProducto

# Create your views here.

def index(request):
    return render(request, 'productoApp/index.html')

def listadoProducto(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, 'productoApp/producto.html', data)

def agregarProducto(request):
    form = FormProducto
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'productoApp/agregarProducto.html', data)

def eliminarProducto(request,id):
    producto = Productos.objects.get(id = id)
    producto.delete()
    return redirect('/productos')

def actualizarProducto(request, id):
    producto = Productos.objects.get(id = id)
    form = FormProducto(instance=producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'productoApp/agregarProducto.html', data)