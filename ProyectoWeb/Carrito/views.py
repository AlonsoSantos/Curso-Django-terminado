from django.shortcuts import render, redirect
from .carrito import Carrito
from Tienda.models import Producto

def agregarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.agregar(producto=producto)
    return redirect('Tienda')

def eliminarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.eliminar(producto=producto)
    return redirect('Tienda')

def restarProducto(request, productoId):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=productoId)
    carrito.restarProducto(producto=producto)
    return redirect('Tienda')

def limpiarCarrito(request, productoId):
    carrito = Carrito(request)
    carrito.limpiarCarrito()
    return redirect('Tienda')