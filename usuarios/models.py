from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

    def __str__(self):
        return f"[{self.pk}] {self.username} - {self.first_name}"
