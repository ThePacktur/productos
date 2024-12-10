from django.shortcuts import render, redirect
from .serializers import ProductoSerializer, DistribuidorSerializer, FacturaSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import Http404
from productoApp.models import Productos, Distribuidor, Factura
from productoApp.forms import FormProducto, FormDistribuidor, FormFactura
class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer

# Create your views here.
#class ProductList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#    queryset = Productos.objects.all()
#    serializer_class = ProductoSerializer


#    def get(self, request):
#        return self.list(request)
        
        #productos = Productos.objects.all()
        #serializer = ProductoSerializer(productos, many=True)
        #return Response(serializer.data)



#    def post(self, request):
#        return self.create(request)
        
        
        #serializer = ProductoSerializer(data = request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FactureList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class FactureDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def get(self, request, pk):
        return self.retrieve(request,pk)
    
    def put(self,request, pk):
        return self.update(request,pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

class DistribuidorList(generics.ListCreateAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer

class DistribuidorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer
        



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