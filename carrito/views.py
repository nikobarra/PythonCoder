from django.shortcuts import render, redirect
from .carrito import Carrito
from EcommerceApp.models import Product



# Create your views here.
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect ("Ecommerce")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect ("Ecommerce")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect ("Ecommerce")

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.limpiar_Carrito()
    return redirect ("Ecommerce")



