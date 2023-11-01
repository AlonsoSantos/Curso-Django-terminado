from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import send_mail
from django.conf import settings

def contacto(request):
    formulario = formularioContacto()
    if request.method == 'POST':
        formulario = formularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            try:
                asunto = 'Información pagina web'
                mensaje = "El usuario: "+nombre+"\nDice lo siguiente: \n"+contenido+"\nEnviado por: "+email
                email_que_manda = settings.EMAIL_HOST_USER
                email_que_recibe = ["tilijobne@gmail.com"]
                send_mail(asunto,mensaje,email_que_manda,email_que_recibe)
                return redirect('/Contacto/?valido')
            except Exception as e:
                print(e)
    return render(request, 'contacto/contacto.html', {'formulario':formulario})