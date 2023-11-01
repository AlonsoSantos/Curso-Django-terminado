from django.shortcuts import render, HttpResponse
from Carrito.carrito import Carrito

def home(request):
    carrito = Carrito(request)
    return render(request, 'ProyectoWebApp/home.html')
