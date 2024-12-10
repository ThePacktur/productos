"""producto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from productoApp import views
router = DefaultRouter()
router.register('products', views.ProductoViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include(router.urls)),#views.ProductList.as_view()),
    #path('products/<int:pk>', views.ProductDetail.as_view()),
    path('distribuidors/', views.DistribuidorList.as_view()),
    path('distribuidors/<int:pk>',views.DistribuidorDetail.as_view()),
    path('factures/', views.FactureList.as_view()),
    path('factures/<int:pk>', views.FactureDetail.as_view()),
    path('productos/', views.listadoProducto),
    path('agregarProducto/',views.agregarProducto),
    path('eliminarProducto/<pk>',views.eliminarProducto),
    path('actualizarProducto/<pk>',views.actualizarProducto),
    path('distribuidores/', views.listadoDistribuidor),
    path('agregarDistribuidor/', views.agregarDistribuidor),
    path('eliminarDistribuidor/<pk>', views.eliminarDistribuidor),
    path('actualizarDistribuidor/<pk>', views.actualizarDistribuidores),
    path('facturas/',views.listadoFactura),
    path('agregarFactura/', views.agregarFactura),
    path('eliminarFactura/<pk>',views.eliminarFactura),
    path('actualizarFactura/<pk>', views.actualizarFactura),
  

]
