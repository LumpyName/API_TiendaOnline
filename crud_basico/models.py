from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nombre_de_usuario = models.CharField(max_length=150, unique=True)  # El nombre de usuario debe ser único
    password = models.CharField(max_length=255)  # Se recomienda almacenar contraseñas de manera segura (ver notas abajo)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)  # Subir foto de perfil
    correo_electronico = models.EmailField(unique=True)  # Correo electrónico único

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

