from django.shortcuts import render, redirect
from .serializers import ProductoSerializer, DistribuidorSerializer, FacturaSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from productoApp.models import Productos, Distribuidor, Factura
from productoApp.forms import FormProducto, FormDistribuidor, FormFactura

# Create your views here.

@api_view(['GET','POST'])
def productList(request):
    if request.method == 'GET':
        productos = Productos.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def distribuidorList(request):
    if request.method == 'GET':
        distribuidores = Distribuidor.objects.all()
        serializer = DistribuidorSerializer(distribuidores, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DistribuidorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def facturaList(request):
    if request.method == 'GET':
        facturas = Factura.objects.all()
        serializer = FacturaSerializer(facturas, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = FacturaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




@api_view(['GET','PUT','DELETE'])
def productoDetail(request, pk):
    try:
        producto = Productos.object.get(pk=pk)
    except Productos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def distribuidorDetail(request, pk):
    try:
        distribuidor = Distribuidor.object.get(pk=pk)
    except Distribuidor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DistribuidorSerializer(distribuidor)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = DistribuidorSerializer(distribuidor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def facturaDetail(request, pk):
    try:
        factura = Factura.object.get(pk=pk)
    except Factura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FacturaSerializer(factura)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = FacturaSerializer(factura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def index(request):
    return render(request, 'productoApp/index.html')

def listadoProducto(request):
    productos = Productos.objects.all()
    data = {'productos': productos}
    return render(request, 'productoApp/producto.html', data)

def listadoDistribuidor(request):
    distribuidores = Distribuidor.objects.all()
    data = {'distribuidores': distribuidores}
    return render(request, 'productoApp/distribuidor.html', data)


def listadoFactura(request):
    facturas = Factura.objects.all()
    data = {'facturas' : facturas}
    return render(request, 'productoApp/factura.html', data)

def agregarProducto(request):
    form = FormProducto
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
        return listadoProducto(request)
    data = {'form': form}
    return render(request,'productoApp/agregarProducto.html', data)

def agregarDistribuidor(request):
    form = FormDistribuidor()
    if request.method == 'POST':
        form = FormDistribuidor(request.POST)
        if form.is_valid():
            form.save()
        return listadoDistribuidor(request)
    data = {'form': form}
    return render(request, 'productoApp/agregarDistribuidor.html', data)

def agregarFactura(request):
    form = FormFactura
    if request.method == 'POST':
        form = FormFactura(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return listadoFactura(request)
    data = {'form': form}
    return render(request, 'productoApp/agregarFactura.html', data)


def eliminarProducto(request, pk):
    producto = Productos.objects.get(pk = pk)
    producto.delete()
    return redirect('/productos')

def eliminarDistribuidor(request, pk):
    distribuidor = Distribuidor.objects.get(pk=pk)
    distribuidor.delete()
    return redirect('/distribuidores')

def eliminarFactura(request, pk):
    factura = Factura.objects.get(pk = pk)
    factura.delete()
    return redirect('/facturas')


def actualizarProducto(request, pk):
    producto = Productos.objects.get(pk = pk)
    form = FormProducto(instance=producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=producto)
        if form.is_valid(): 
            form.save()
        return listadoProducto(request)
    data = {'form': form}
    return render(request, 'productoApp/agregarProducto.html', data)

def actualizarDistribuidores(request, pk):
    distribuidor = Distribuidor.objects.get(pk = pk)
    form = FormDistribuidor(instance=distribuidor)
    if request.method == 'POST':
        form = FormDistribuidor(request.POST, instance=distribuidor)
        if form.is_valid():
            form.save()
        return listadoDistribuidor(request)
    data = {'form': form}
    return render(request, 'productoApp/agregarDistribuidor.html', data)

def actualizarFactura(request, pk):
    factura = Factura.objects.get(pk=pk)
    form = FormFactura(instance=factura)
    if request.method == "POST":
        form = FormFactura(request.POST, instance=factura)
        if form.is_valid():
            form.save()
        return listadoFactura(request)
    data = {'form': form}
    return render(request, 'productoApp/agregarFactura.html',data)