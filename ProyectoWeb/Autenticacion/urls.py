from django.urls import path
from .views import Registro, cerrarSesion, iniciarSesion

urlpatterns = [
    path('', Registro.as_view(), name='Autenticacion'),
    path('cerrarSesion', cerrarSesion, name='CerrarSesion'),
    path('iniciarSesion', iniciarSesion, name='IniciarSesion'),
]