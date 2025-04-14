from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.pk}] {self.username} - {self.first_name}"
