from django.urls import path
from Carrito import views

app_name = 'carrito'

urlpatterns = [
    path('agregarProducto/<int:productoId>', views.agregarProducto, name='agregar'),
    path('eliminarProducto/<int:productoId>', views.eliminarProducto, name='eliminar'),
    path('restarProducto/<int:productoId>', views.restarProducto, name='restar'),
    path('limpiarCarrito', views.limpiarCarrito, name='limpiar'),
]