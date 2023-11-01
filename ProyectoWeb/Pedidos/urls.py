from django.urls import path
from .views import procesarPedido

urlpatterns = [
    path('', procesarPedido, name='Procesar pedido'),
]