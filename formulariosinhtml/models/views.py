from django.shortcuts import render
from models.formularios import FormularioRegistro
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from models.models import Usuario
import socket
# Creacion de vistas


def formularioView(request):
    mensaje = 0
    lista = Usuario.objects.all
    nombre_equipo = socket.gethostname()
    ip_equipo = socket.gethostbyname(nombre_equipo)
    if request.method == 'GET':
        form = FormularioRegistro()
    else:
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            cedula = form.cleaned_data['cedula']
            telefono = form.cleaned_data['telefono']
            correo = form.cleaned_data['correo']
            ciudad = form.cleaned_data['ciudad']
            if nombres and apellidos and ip_equipo:
                cedulavalidacion = Usuario.objects.filter(cedula = cedula)
                if cedulavalidacion:
                    mensaje = 2
                    return render(request, "formulario.html", {'form': form,"nombres":nombres,"mensaje":mensaje, "lista":lista})
                else:
                    usuario = Usuario(nombres=nombres, apellidos=apellidos, cedula=cedula, telefono=telefono,correo=correo,ip=ip_equipo,ciudad=ciudad)
                    usuario.save()
                    mensaje = 1
                    return render(request, "formulario.html", {'form': form,"nombres":nombres,"mensaje":mensaje, "lista":lista})
            else:
                return render(request, "formulario.html", {'form': form})
    return render(request, "formulario.html", {'form': form,"lista":lista})

def successView(request):
    return HttpResponse('Registro exitoso !')