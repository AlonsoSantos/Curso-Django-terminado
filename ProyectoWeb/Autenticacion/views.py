from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

class Registro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'autenticacion/autenticacion.html', {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request, 'autenticacion/autenticacion.html', {'form':form})

def cerrarSesion(request):
    logout(request)
    return redirect('Home')

def iniciarSesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombreUsuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            usuario = authenticate(username=nombreUsuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, 'Usuario no válido')
        else:
            messages.error(request, 'Información incorrecta')
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form':form})