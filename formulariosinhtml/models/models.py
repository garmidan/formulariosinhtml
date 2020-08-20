from django.db import models
# Creacion de modelos

class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=13)
    telefono = models.CharField(max_length=13)
    correo = models.CharField(max_length=50)
    ip = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=50)