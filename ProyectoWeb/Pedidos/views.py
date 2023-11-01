from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, Producto
from Carrito.carrito import Carrito
from Pedidos.models import LineaPedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail

@login_required(login_url='/Autenticacion/iniciarSesion')
def procesarPedido(request):
    pedido = Pedido.objects.create(usuario=request.user)
    carrito = Carrito(request)
    lineasPedido = list()
    for key, value in carrito.carrito.items():
        producto = Producto.objects.get(id=int(key))
        lineasPedido.append(LineaPedido(
            producto = producto,
            cantidad = value['cantidad'],
            usuario = request.user,
            pedido = pedido
        ))
    LineaPedido.objects.bulk_create(lineasPedido)
    enviarCorreo(
        pedido=pedido,
        lineasPedido=lineasPedido,
        nombreUsuario=request.user.username,
        emailUsuario=request.user.email
    )
    messages.success(request, 'El pedido se ha creado correctamente')
    return redirect('../Tienda')

def enviarCorreo(**kwargs):
    asunto = 'Gracias por tu pedido'
    mensaje = render_to_string('emails/pedido.html',{
        'pedido': kwargs.get('pedido'),
        'lineasPedido': kwargs.get('lineasPedido'),
        'nombreUsuario': kwargs.get('nombreUsuario')
    })
    mensajeTexto = strip_tags(mensaje)
    email_que_manda = settings.EMAIL_HOST_USER
    # email_que_recibe = kwargs.get('emailUsuario')
    email_que_recibe = 'tilijobne@gmail.com'
    send_mail(asunto,mensajeTexto,email_que_manda,[email_que_recibe],html_message=mensaje)